#!/usr/bin/env bash +x

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

# Underline
UBlack='\033[4;30m'       # Black
URed='\033[4;31m'         # Red
UGreen='\033[4;32m'       # Green
UYellow='\033[4;33m'      # Yellow
UBlue='\033[4;34m'        # Blue
UPurple='\033[4;35m'      # Purple
UCyan='\033[4;36m'        # Cyan
UWhite='\033[4;37m'       # White

init_brew() {
  echo -e "${UGreen}Init Homebrew${Color_Off}"
  if ! command -v brew &> /dev/null; then
    yes | /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || exit 1
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> $HOME/.profile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> $HOME/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
  fi
}

init_fish() {
  echo -e "${UGreen}Init Fish Shell${Color_Off}"
  if ! command -v fish &> /dev/null; then
    brew install fish starship fisher
    fish -c "echo 'if status is-interactive
      /opt/homebrew/bin/brew shellenv | source
      starship init fish | source
    end' > $HOME/.config/fish/config.fish"
    echo "/opt/homebrew/bin/fish" | sudo tee -a /etc/shells
    chsh -s /opt/homebrew/bin/fish
    echo 'restart your operating system to apply changes'
  fi
}

init_terminal() {
  echo -e "${UGreen}Init Terminal${Color_Off}"
  brew install kitty
}

init_generic_tools() {
  echo -e "${UGreen}Init Generic Tools${Color_Off}"
  brew install git just
}

init_brew
init_fish
init_terminal
init_generic_tools
