#! /bin/bash

git submodule update --init config/alacritty/themes
cp .zshrc ~/.zshrc
cp -r config/* ~/.config/
