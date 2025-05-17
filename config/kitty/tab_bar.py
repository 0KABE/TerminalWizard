import logging
import subprocess
import sys
from datetime import datetime, timezone, timedelta

from kitty.fast_data_types import Screen, add_timer, get_boss, get_options
from kitty.rgb import Color
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    Formatter,
    TabBarData,
    as_rgb,
    draw_attributed_string,
    draw_title,
)
from kitty.utils import color_as_int

ICON = "  "
ICON_FG = as_rgb(0x717374)
SEPARATOR_FG = as_rgb(0xFFFFFF)
BAT_TEXT_COLOR = as_rgb(0x999F93)
CLOCK_FG = as_rgb(0x7FBBB3)
UTC_FG = as_rgb(0x717374)
OPTS = get_options()

UNPLUGGED_ICONS = {
    10: "󰁺",
    20: "󰁻",
    30: "󰁼",
    40: "󰁽",
    50: "󰁾",
    60: "󰁿",
    70: "󰂀",
    80: "󰂁",
    90: "󰂂",
    100: "󱟢",
}
PLUGGED_ICONS = {
    1: "󰂄",
}
UNPLUGGED_COLORS = {
    15: as_rgb(color_as_int(OPTS.color1)),
    16: as_rgb(color_as_int(OPTS.color15)),
}
PLUGGED_COLORS = {
    15: as_rgb(color_as_int(OPTS.color1)),
    16: as_rgb(color_as_int(OPTS.color6)),
    99: as_rgb(color_as_int(OPTS.color6)),
    100: as_rgb(0xA7C080),
}
BATTERY_STATUS_CMD = 'pmset -g batt | head -n 1 | cut -d \\\' -f2'
BATTERY_PERCENT_CMD = 'pmset -g batt | grep -Eo "\\d+%" | cut -d% -f1'

# config logger to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def _get_battery_status():
    s_result = subprocess.run(BATTERY_STATUS_CMD, shell=True, capture_output=True)
    if s_result.stderr:
        raise subprocess.CalledProcessError(
            returncode=s_result.returncode, cmd=s_result.args, stderr=s_result.stderr
        )

    status = ""
    if s_result.stdout:
        status = s_result.stdout.decode("utf-8").strip()

    p_result = subprocess.run(BATTERY_PERCENT_CMD, shell=True, capture_output=True)
    if p_result.stderr:
        raise subprocess.CalledProcessError(
            returncode=p_result.returncode, cmd=p_result.args, stderr=p_result.stderr
        )

    percent = ""
    if p_result.stdout:
        percent = int(p_result.stdout.decode("utf-8").strip())

    if status.startswith('Battery Power'):
        icon_color = UNPLUGGED_COLORS[
            min(UNPLUGGED_COLORS.keys(), key=lambda x: abs(x - percent))
        ]
        icon = UNPLUGGED_ICONS[
            min(UNPLUGGED_ICONS.keys(), key=lambda x: abs(x - percent))
        ]
    else:
        icon_color = PLUGGED_COLORS[
            min(PLUGGED_COLORS.keys(), key=lambda x: abs(x - percent))
        ]
        icon = PLUGGED_ICONS[min(PLUGGED_ICONS.keys(), key=lambda x: abs(x - percent))]

    percent_cell = (BAT_TEXT_COLOR, " " + str(percent) + "%")
    icon_cell = (icon_color, icon)
    return icon_cell, percent_cell


def _draw_icon(draw_data: DrawData, screen: Screen, is_first: bool):
    # only draw icon for the first tab
    if not is_first:
        return

    fg, bg = screen.cursor.fg, screen.cursor.bg
    screen.cursor.fg = as_rgb(color_as_int(ICON_FG))
    screen.cursor.bg = as_rgb(color_as_int(draw_data.default_bg))
    screen.draw(ICON)
    screen.cursor.fg, screen.cursor.bg = fg, bg
    screen.cursor.x = len(ICON)


status_last_updated = datetime.min
cached_status = None


def _status_should_update() -> bool:
    global status_last_updated
    if datetime.now() - status_last_updated >= timedelta(seconds=5):
        status_last_updated = datetime.now()
        return True
    else:
        return False


def _get_status():
    global cached_status
    if not _status_should_update():
        return cached_status

    battery_status, battery_percent = _get_battery_status()
    separator = " ⋮ "
    clock = datetime.now().strftime("%H:%M")
    utc = datetime.now(timezone.utc).strftime(" (UTC %H:%M)")

    cached_status = [
        battery_status,
        battery_percent,
        (SEPARATOR_FG, separator),
        (CLOCK_FG, clock),
        (UTC_FG, utc)
    ]
    logging.info(f'cells={cached_status}')
    return cached_status


def _draw_status(draw_data: DrawData, screen: Screen, is_last: bool):
    # only draw status for the last tab
    if not is_last:
        return

    cells = _get_status()
    right_status_length = sum(len(cell[1]) for cell in cells)
    draw_attributed_string(Formatter.reset, screen)
    screen.cursor.x = screen.columns - right_status_length
    for color, status in cells:
        screen.cursor.fg = color
        screen.draw(status)


def draw_tab(draw_data: DrawData,
             screen: Screen,
             tab: TabBarData,
             before: int,
             max_title_length: int,
             index: int,
             is_last: bool,
             extra_data: ExtraData) -> int:
    _draw_icon(draw_data, screen, index == 1)
    draw_title(draw_data, screen, tab, index, max_title_length)
    _draw_status(draw_data, screen, is_last)
    return screen.cursor.x
