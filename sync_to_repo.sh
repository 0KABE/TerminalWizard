#! /bin/bash

mkdir -p config

cp ~/.zshrc ./.zshrc

cp -r ~/.config/alacritty ./config
cp -r ~/.config/zellij ./config
