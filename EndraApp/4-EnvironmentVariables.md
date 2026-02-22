# Environment Variables

Whether you're running EndraApp from source, an executable binary, or an installed package, you can change certain aspects of its behaviour by configuring environment variables.
Not all of these configurations are compatible with all operating systems and packaging types.

- `USE_BRENTHY` (`0` or `1`, defaults to `0`): Instead of running an embedded IPFS and Walytis node, use the separately running system services for IPFS and Walytis. This enables faster loading times. To set up IPFS & Walytis in this way, [install Brenthy](https://github.com/emendir/BrenthyAndWalytis)
- `IPFS_TK_MODE` (`EMBEDDED` or `HTTP`): **NOT YET IMPLEMENTED** (as of v0.6.3) If you don't want to use Brenthy but do want to use a separate IPFS daemon, set this variable to `HTTP`
- `KIVY_NO_CONSOLELOG` (`0` or `1`, defaults to `0`): stop kivy logging to console
- `USE_PANGO` (`0` or `1`, defaults to `0`): Use the Pango text provider to enable broader character & emoji text rendering support
- `WALY_LOG_DIR` (`DISABLED` or valid directory path, defaults to `DISABLED`): **NOT YET IMPLEMENTED** (as of v0.6.3) disable logging to files or enable, setting the logging directory
- `IPFS_PUBSUB_LOGGING` (`0` or `1`, defaults to `0`): **NOT YET IMPLEMENTED** (as of v0.6.3) enable/disable logging to IPFS pubsub channels
