
# Walytis Identities


WalytisIdentities is a peer-to-peer cryptographic identity management system that uses ephemeral keys and supports multiple controllers per identity.

## Purpose
The purpose of this system is to enable secure communications between identities with multiple controllers in peer-to-peer networks, providing the means to:
- encrypt messages so that they can be decrypted only by a specific identity
- verify the authenticity of received messages, ensuring they were authored by a specific identity
## Core Functionality
To achieve this goal in a sustainably secure fashion, WalytisIdentities' core task lies in managing the ephemeral cryptographic keys belonging to digital identities:
- it automatically renews keys at regular intervals
- it publishes the new public keys in a verifiable manner
- it securely distributes the private keys to all controllers of the identity

## Features

- fully peer-to-peer: no servers of any kind involved
- multi-controller support: a Walytis Identity can be managed by any number of controllers
- identity nesting: Walytis Identities can be controlled by other Walytis Identities
- ephemeral cryptography: regular key renewal, algorithm-agnostic, room for future algorithms

## Use cases

WalytisIdentities was developed to empower developers to build peer-to-peer distributed applications that require secure communications with encryption and authentication.
A classic example of such a use case is a peer-to-peer messenger, which is being developed in the [Endra Project](https://github.com/emendir/Endra).

## Underlying Technologies
- [Walytis Database-Blockchain](../Walytis/Meaning/IntroductionToWalytis.md): a blockchain that serves as a p2p distributed database
- [IPFS](https://ipfs.tech): the peer-to-peer network layer which Walytis is built on
### DID Compatibility

WalytisIdentities implements the [World-Wide-Web-Consoritum's (W3C's) Decentralised Identifiers (DIDs) specifications](https://www.w3.org/TR/did-core/).

In the context of W3C's DID architecture, walytis_identities is a [DID method](https://www.w3.org/TR/did-core/#methods),
meaning that walytis_identities is a system for creating DIDs and managing DID-Documents.
walytis_identities achieves this using the Walytis blockchain.



## Source Code

This project's repository is hosted on the following platforms:
- https://github.com/emendir/WalytisIdentities