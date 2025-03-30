default:
    just --list

export DEST_DIR="":
    #!/usr/bin/env bash +x
    set -euo pipefail
    EXPORT_DIR="{{ if DEST_DIR!= '' { DEST_DIR } else { "~/.config" } }}"
    BACKUP_DIR="{{ justfile_directory() }}/backup-$(date)"
    echo "Export config files to '$EXPORT_DIR/'"
    just backup_configs "$BACKUP_DIR"
    mkdir -p "$EXPORT_DIR"
    cp -r config/* $EXPORT_DIR

backup SRC_DIR="":
    #!/usr/bin/env bash
    set -euo pipefail
    BACKUP_DIR="{{ if SRC_DIR != '' { SRC_DIR } else { justfile_directory() } }}/config"
    echo "Backup config files in '$BACKUP_DIR/'"
    mkdir -p "$BACKUP_DIR"
    cp -r ~/.config/fish "$BACKUP_DIR"
    cp -r ~/.config/kitty "$BACKUP_DIR"
