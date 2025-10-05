# The Endra Tech Stack

The Endra stack is a layered set of decentralised communications technologies that power the [Endra protocol](1-IntroToEndra.md), a fully peer-to-peer (P2P) messaging system with multiple devices per user, ephemeral cryptography, etc.
It is the flagship product compilation of the open-source public-domain [Walytis Technologies](../ReadMe.md) project.

The raison d'état of of Endra stack begins with this question: How does one manage private message sharing, user identities, and key distribution in a P2P network with multiple devices per user?
The Endra stack combines modularised solutions to each of these questions in a layered tech stack designed to enable developers to easily build peer-to-peer distributed applications.

### Endra Tech Stack Components
#### Overview

| Layer                                                                     | Data Features                                                                       | Networking Features                                                  |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [Endra](../Endra/1-IntroToEndra.md)                                       | - organisation of identities, contacts & chats                                      | - near-instant messaging                                             |
| [Walytis-Mutability](../WalytisMutability/1-IntroToWalytisMutability.md)  | - mutable blocks (for editable messages)                                            |                                                                      |
| [Walytis-Offchain](../WalytisOffchain/1-IntroToWalytisOffchain.md)        | - private encrypted blocks<br>- contact authentication                              |                                                                      |
| [Walytis-Identities](../WalytisIdentities/1-IntroToWalytisIdentities.md)  | - identities<br>- cryptographic key management                                      | - multi-device identities<br>- multi-controller key management       |
| [Walytis](../Walytis/Meaning/IntroductionToWalytis.md)                    | - distributed database<br>- new blocks notification<br>- data integrity maintenance | - identification of database peers                                   |
| [IPFS](https://ipfs.tech)/[libp2p](https://libp2p.io/) (by Protocol Labs) | - file sharing                                                                      | - persistent peer addressing<br>- P2P routing<br>- NAT-hole-punching |


- **[Endra](../Endra/1-IntroToEndra.md):** a fully distributed, peer-to-peer encrypted messaging protocol, built on Walytis and its blockchain-overlays
- **[WalytisIdentities](../WalytisIdentities/1-IntroToWalytisIdentities.md), [WalytisOffchain](../WalytisOffchain/1-IntroToWalytisOffchain.md), [WalytisMutability](../WalytisMutability/1-IntroToWalytisMutability.md):** blockchain-overlays - systems providing an interface with additional features to Walytis databases
- **[Walytis](../Walytis/Meaning/IntroductionToWalytis.md):** a database blockchain - a lightweight, non-linear & flexible blockchain for distributed databases, built on IPFS
- **[IPFS](https://ipfs.tech):** Interplanetary File System - a peer-to-peer communications and content sharing protocol, built on libp2p, developed by Protocol Labs
- **[libp2p](https://libp2p.io/):** a peer-to-peer OSI layer 3 communications protocol used as an overlay over the internet protocol, developed by Protocol Labs

#### The Internet Protocol - The Networking Foundation

The Internet Protocol is a central part of most modern networks.
Whether it's the public internet, local home networks, mobile broadband - all these networks use the Internet Protocol to relay packets of data between computers to transport them from sender to recipient.
It's almost more useful to ask what doesn't use the IP: The Deep Space Network which connects Mars rovers and other probes to Earth doesn't, and closer to home most Bluetooth devices and some smart-home systems don't use it either.

Interestingly, the [Berty messenger](https://berty.tech/), another peer-ro-peer IPFS messenger, does leverage Bluetooth alongside IP! Sadly, that technology isn't (yet) modularly pluggable to IPFS on all platforms.

#### The InterPlanetary File System (IPFS) & libp2p - The P2P Engine
##### libp2p
[libp2p](https://libp2p.io/) is an internet overlay protocol.
This means it uses the internet protocol (IP) and has a similar role to the IP, in that it allows computers to address each other and figure out how to send packets of data to each other.
The crucial difference is that libp2p peer addresses never change as the peer's host computer moves around a network, unlike in the IP, where the computer's IP address is determined by its location in the network.
Many components of the Walytis tech stack use its publish-subscribe and TCP tunnelling features to allow peers to communicate with each other.
##### IPFS
Build on top of libp2p, IPFS' main feature is peer-to-peer file sharing and content addressing.
Currently, all Walytis technologies access libp2p features through an IPFS software wrapper.

#### The Walytis Database Blockchain - The Data Sharing Layer

Walytis is a unique blockchain built on top of IPFS & libp2p, but in this context it's best to think about it simply as a peer-to-peer distributed database.

IPFS gives peers to access an ocean of files.
Walytis provides a way to structure files/blocks into an extensible dataset, ensuring no block/file in the dataset can ever be lost or forgotten, and ensuring some sense of chronological relationship between them, as well as notifying peers when new files/blocks are added.

#### WalytisIdentities - The Identity and Key Management System

WalytisIdentities uses Walytis to bring to life digital identities that can be controlled from many devices or by other identities and manages ephemeral cryptographic keys associated with those identities, in line with the [World-Wide-Web-Consoritum's (W3C's) Decentralised Identifiers (DIDs) specifications](https://www.w3.org/TR/did-core/).


#### WalytisOffchain - The Content Encryption and Authentication Module

WalytisOffchain is an abstracted overlay for the Walytis blockchain which stores its blocks not on the underlying Walytis blockchain, but in a local encrypted store for each peer.
Peers share this encrypted content securely and authenticate received blocks' authors using WalytisIdentities.

#### WalytisMutability - The Data Mutability and Version-Control Layer

WalytisMutability is an abstracted overlay for the Walytis blockchain which allows for editing and deleting its abstracted blocks, with the ability to see the version history of all blocks, including deleted ones.
Under the hood, every edit or deletion is achieved by adding a new metadata block to the underlying blockchain.

#### Endra - The Messaging Protocol

Endra combines Walytis' peer-to-peer distributed database, WalytisIdentities' identity & cryptography management, WalytisOffchain's secure data storage & transmission, and WalytisMutability's database editing abstraction to form a messaging protocol with concepts such as user-account, user-device, chat-room, send-message etc.

It can be used for more than just instant messaging - shared calendars, project management tools and an endless amount of distributed communications systems could be built using it.