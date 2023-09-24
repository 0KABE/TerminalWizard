# Initialize ZSH

## Install ZSH

* macOS
  * `brew install zsh`

## Install Oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Themes

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

Type `p10k configure` to customize the theme style

### Oh-my-zsh Plugins

#### Install plugins

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/Pilaton/OhMyZsh-full-autoupdate.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/ohmyzsh-full-autoupdate
```

#### Enable plugins

Open `~/.zshrc` config and modify the `plugins` variable as the following

```bash
plugins=(
    git 
    docker 
    docker-compose 
    zsh-syntax-highlighting 
    zsh-autocomplete
    zsh-autosuggestions 
    ohmyzsh-full-autoupdate
)
```
