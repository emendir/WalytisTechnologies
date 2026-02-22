# Running EndraApp From Source

## Getting Started
1. Download the source code:
```sh
git clone https://github.com/emendir/EndraApp
cd EndraApp
```

2. Load python virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate
```

3. Install Prerequisites:

```sh
./install_prereqs.sh
```

4. Run:
```sh
python src/main.py
```

[You can configure the way EndraApp runs using environment variables.](4-EnvironmentVariables.md)

## Running for Development

For speedy starting and termination of the app, on Linux, [install Brenthy](https://github.com/emendir/BrenthyAndWalytis) to run Walytis & IPFS as a systemd service.
Then run Endra with:

```sh
USE_BRENTHY=1 python tests/test_app.py
```

Pressing Ctrl+C in the terminal should promptly close the Endra app.

Rerunning the app this way overwrites the app's appdata with a cache stored in `tests/appdata`, so that it doesn't matter if the app crashes and corrupts its appdata.

To save the current appdata, close the endra app and run:

```sh
tests/update_appdata.sh
```

From now on, every time you run `tests/test_app.py`, the new appdata state will be loaded.

To reset the appdata, run:

```sh
rm -rf tests/appdata
```
