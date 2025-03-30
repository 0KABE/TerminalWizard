# macOS-Config

macOS configuration for Shell environment and tools.

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
