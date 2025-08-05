
# Endra Protocol

_A peer-to-peer encrypted messaging protocol supporting multiple devices per user._

Endra can be used for more than just instant messaging - shared calendars, project management tools and an endless amount of distributed communications systems can be built using it.

See the [EndraApp](../EndraApp/1-IntroToEndraApp.md) project for a GUI messaging application for desktop and mobile implementing Endra.

## Features

- fully peer to peer, no servers of any kind
- can function independently of internet connectivity
- full end-to-end encryption ephemeral keys, algorithm-agnostic & future-proof
- multiple devices per profile (user account)
- multiple profiles per device
- can be used as a library for embedding into other applications
- will become part of an expandable ecosystem incl. calendar and file-sharing
- [app for desktop and mobile](https://github.com/emendir/EndraApp) (tested on Linux (Ubuntu x86-64) and Android (arm-64))

### How it Works

The Endra protocol is built from a modular set of components forming the [Endra Stack](./2-EndraStack.md).
Each of these components provides a certain set of features, and when they are combined, they provide all that is needed for a fully featured peer-to-peer messaging protocol.

#### Overview of the [EndraStack](./2-EndraStack.md)

- [IPFS](https://ipfs.tech):  A P2P communication and content addressing protocol developed by ProtocolLabs.
- [Walytis](../Walytis/Meaning/IntroductionToWalytis.md): A flexible, lightweight, nonlinear database-blockchain, built on IPFS.
- [WalytisIdentities](../WalytisIdentities/1-IntroToWalytisIdentities.md): P2P multi-controller cryptographic identity management, built on Walytis.
- [WalytisOffchain](../WalytisOffchain/1-IntroToWalytisOffchain.md): Secure access-controlled database-blockchain, built on WalytisIdentities.
- [WalytisMutability](../WalytisMutability/1-IntroToWalytisMutability.md): A Walytis blockchain overlay featuring block mutability.
- [Endra](../Endra/1-IntroToEndra.md): A P2P encrypted messaging protocol with multiple devices per user, built on Walytis.
- [EndraApp](../EndraApp/1-IntroToEndraApp.md): A P2P encrypted messenger supporting multiple devices per user, built on Walytis.

Learn more about the [EndraStack here](./2-EndraStack.md).