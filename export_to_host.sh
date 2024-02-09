#! /bin/bash

BACKUP_DIR="backup-$(date)"
echo "backup config files in '$BACKUP_DIR/'"

./sync_to_repo.sh "$BACKUP_DIR"

git submodule update --init config/alacritty/themes
cp .zshrc ~/.zshrc
cp -r config/* ~/.config/
