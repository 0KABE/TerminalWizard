# TerminalWizard

TerminalWizard for Shell environment and dotfiles

## Initialization

For the first time, run the following command. It will install the necessary tools and set up the environment.

* macOS
    ```bash
    ./init_macOS.sh
    ```

## Backup to the repository

Copy the current user's configs into the repository.

```bash
just backup
```

## Export configs to the host

Automatically back up the host's configs, and overwrite them with configs in the repository.
You can restore the configs from the folder named according to the time of execution.

```bash
just export
```
