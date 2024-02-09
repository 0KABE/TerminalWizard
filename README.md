# macOS-Config

macOS configuration for ZSH, Oh-my-zsh, Tmux, etc...

## Sync to the repository

Copy the current user's configs into the repository.

```bash
./sync_to_repo.sh
```

## Export configs to the host

Automatically back up the host's configs, and overwrite them with configs in the repository.
You can restore the configs from the folder named according to the time of execution.

```bash
./export_to_host.sh
```
