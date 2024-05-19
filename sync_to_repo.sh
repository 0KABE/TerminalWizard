#! /bin/bash

BASE_DIR="${1:-.}"
echo "copy configs => $BASE_DIR/"

mkdir -p "$BASE_DIR/config"
cp ~/.zshrc "$BASE_DIR/.zshrc"
cp -r ~/.config/alacritty "$BASE_DIR/config"
cp -r ~/.config/zellij "$BASE_DIR/config"
cp -r ~/.config/fish "$BASE_DIR/config"
cp -r ~/.config/kitty "$BASE_DIR/config"
cp -r ~/.config/omf "$BASE_DIR/config"
