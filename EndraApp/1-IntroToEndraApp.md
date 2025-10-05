# Endra App
_A P2P encrypted messenger supporting multiple devices per user._

Endra is a messenger that provides end-to-end encrypted peer-to-peer communications, with modern identity-management supporting multiple devices per user account and multiple user accounts can be installed on the same device.

### Features

- peer-to-peer: with no server infrastructure, this messaging system runs without the backing of any company, organisation or other forms of IT administration other than the internet
- end-to-end encryption: uses ephemeral keys, is algorithm-agnostic & future-proof
- multiple devices per profile (user account)
- multiple profiles per device

## How it Works

The [Endra protocol](../Endra/1-IntroToEndra.md) is built from a modular set of components composing the [Endra Stack](../Endra/2-EndraStack.md).
Each of these components provides a certain set of features, and when they are combined, they provide all that is needed for a fully featured peer-to-peer messaging protocol.

### Runtime

The Endra app and the entirety of the [Walytis Technologies](../ReadMe.md) is written in Python.
The only part of the stack that isn't is IPFS/libp2p, where the Go implementation is used.
The GUI framework used is [kivy](https://kivy.org/).

For the Endra App portable executable, the entire Endra stack (including IPFS) is embedded into a python library.
Alternatively, the source code can be run using separate IPFS and Walytis services running in the background of the operating system.

## OS Compatibility & Download

The Endra app is designed to be cross-platform for desktop and mobile.
So far, it has been tested on Linux (Ubuntu 24), Android, and Windows 11.

Package build pipelines have been developed for the below listed formats, and can be [downloaded here](https://github.com/emendir/EndraApp/releases).
### Linux
- flatpak for x86-64 and arm64

Coming soon: Nix, AUR
### Android
- APK for arm-64
### MacOS
Coming soon...

### iOS
probably coming later, in [Phase IV of the Endra Roadmap](../RoadMap.md#Phase%20IV%20-%20Transform%20into%20Production-Grade%20Software), unless

### Windows
- portable EXE for x86_64

## Source Code

This project's repository is hosted on the following platforms:
- https://github.com/emendir/EndraApp