# Walytis Technologies

_A collection of tools for real-world peer-to-peer communications, built around the Walytis blockchain._


The Walytis Technologies are open-source modular systems built to enable developers to easily develop peer-to-peer distributed applications.

### Flagship
The flagship product of these modular systems is the [Endra Tech Stack](Endra/2-EndraStack.md), which combines all the Walytis technologies to produce the [Endra messaging protocol](Endra/1-IntroToEndra.md) and the the [Endra messenger application](./EndraApp).

### Core
At the core of these systems lies Walytis, a flexible, lightweight, nonlinear blockchain, serving as a peer-to-peer distributed database.
It was the initial invention that led to the rest of the Walytis technologies, which include blockchain overlays that provide additional database features and other tools like cryptographic identity management and secure communications.

### Dependencies
All Walytis technologies rely fully on IPFS, the InterPlanetary File System and libp2p, which are developed by ProtocolLabs.
They are the peer-to-peer networking foundation for all Walytis technologies.

## Components Overview

Currently, the Walytis Technologies project comprises the following components, with more coming soon: 
- [Walytis](Walytis/Meaning/IntroductionToWalytis.md): A flexible, lightweight, nonlinear database-blockchain, built on IPFS.
- [WalytisIdentities](WalytisIdentities/1-IntroToWalytisIdentities.md): P2P multi-controller cryptographic identity management, built on Walytis.
- [WalytisOffchain](WalytisOffchain/1-IntroToWalytisOffchain.md): Secure access-controlled database-blockchain, built on WalytisIdentities.
- [WalytisMutability](WalytisMutability/1-IntroToWalytisMutability.md): A Walytis blockchain overlay featuring block mutability.
- [Endra](Endra/1-IntroToEndra.md): A P2P encrypted messaging protocol with multiple devices per user, built on Walytis.
- [EndraApp](EndraApp/1-IntroToEndraApp.md): A P2P encrypted messenger supporting multiple devices per user, built on Walytis.

To learn how these components work together, see the documentation for the [Endra Tech Stack](Endra/2-EndraStack.md).

## Technology Type

The Walytis technologies are networking software designed to be run in the environment of an operating system.

Their core, the Walytis blockchain, as well as their essential dependency IPFS, can be run either as separate services in the background of the operating system, or be embedded into applications as libraries to produce standalone and even portable application executables.

These systems are modular, allowing developers to choose and combine those components which they need for their use cases. 

### Programming Languages

Currently, all Walytis technologies are built in Python.
In the future, they [will be rewritten into a compiled language](PortToCompiledSoftware.md) to make them easier to use in other languages, perhaps even with WebAssembly support. 

### Target Devices
These systems are built to be cross-platform for desktop, mobile and server computers.
So far, they've been tested on Linux and Android.

## Project Status & [Roadmap](RoadMap.md)

The components of Walytis Technologies are all in alpha or beta phase.
This means they're fully functional and demonstrable, but still under very active development and are not ready for production use-cases.

Currently, the main focus of development is to improve the performance and reliability of the [Endra stack](Endra/2-EndraStack.md), as well as multimedia and audio & video calls for the Endra Protocol & App.

Once these components reach maturity, [they will be rewritten in a compiled language](PortToCompiledSoftware.md), mainly to improve portability and performance.

For more details,  see the [Walytis Technologies Roadmap](RoadMap.md).


## Open-Source in the Public Domain

I dedicate the Walytis Technologies to the public domain.
They are open source and free to use, derive from and build upon without conditions.

### About the Developer

Walytis and the derived technologies listed here are developed by the author of this documentation, a human, publishing open-source works under the name of _Emendir_. 

## Financial Support

To financially support me in my work on this and other projects, you can make donations with the following currencies:

- **Bitcoin:** `BC1Q45QEE6YTNGRC5TSZ42ZL3MWV8798ZEF70H2DG0`
- **Ethereum:** `0xA32C3bBC2106C986317f202B3aa8eBc3063323D4`
- [**Fiat** (via Credit or Debit Card, Apple Pay, Google Pay, Revolut Pay)](https://checkout.revolut.com/pay/4e4d24de-26cf-4e7d-9e84-ede89ec67f32)

