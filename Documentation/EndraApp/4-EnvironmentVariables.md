# Environment Variables

Whether you're running EndraApp from source, an executable binary, or an installed package, you can change certain aspects of its behaviour by configuring environment variables.
Not all of these configurations are compatible with all operating systems and packaging types.

### Walytis & IPFS Operation Modes

- `USE_BRENTHY` (`0` or `1`, defaults to `0`): When set to `1`, instead of running an embedded IPFS and Walytis node, EndraApp uses the separately running system services for IPFS and Walytis. This enables faster loading times. To set up IPFS & Walytis for this, [install Brenthy](https://github.com/emendir/BrenthyAndWalytis)
- `IPFS_TK_MODE` (`EMBEDDED` or `HTTP`): If you don't want to use Brenthy but do want to use a separate IPFS daemon, set this variable to `HTTP`

### Appdata

- `ENDRA_APPDATA_DIR` path of folder to store appdata in
- See `WALY_LOG_DIR` below for configuring logging path

### Logging

- `WALY_LOG_DIR` (`DISABLED`, `ENDRA_APPDATA` or valid directory path, defaults to `DISABLED`): disable logging to files or enable, setting the logging directory. If set to `ENDRA_APPDATA`, it is stored in a subfolder named `logs` in Endra's appdata folder.
- `ENDRA_PUBSUB_LOGGING` (`0` or `1`, defaults to `0`): enable/disable logging to IPFS pubsub channels
- `KIVY_NO_CONSOLELOG` (`0` or `1`, defaults to `0`): stop kivy from taking control of console logging

### UI

- `USE_PANGO` (`0` or `1`, defaults to `0`): Use the Pango text provider to enable broader character & emoji text rendering support