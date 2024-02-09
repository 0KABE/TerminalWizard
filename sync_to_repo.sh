#! /bin/bash

# This script copy the current user's configs into the repositry
mkdir -p config

cp ~/.zshrc ./.zshrc

cp -r ~/.config/alacritty ./config
cp -r ~/.config/zellij ./config
