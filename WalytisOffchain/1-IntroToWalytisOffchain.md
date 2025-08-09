
### Walytis Blockchain Overlay Features

WalytisOffchain is an overlay for the Walytis blockchain, providing an abstracted blockchain with features that the core Walytis blockchain itself does not have.

Compared to the Walytis blockchain, WalytisOffchain has the following unique features:
- WalytisOffchain blocks are only accessible to a tightly controlled set of peers.
- Block content is stored only in local encrypted databases, only metadata declaring their existence is stored on the underlying Walytis blockchain.
- Block content is securely shared between authorised peers.
- Blocks are also signed by their author, to prove their authenticity.

## How it Works

#### Authorised Peer and Cryptographic Key Management
WalytisOffchain is built on WalytisIdentities, a peer-to-peer cryptographic identity management system that uses ephemeral keys and supports multiple controllers per identity.
Each WalytisOffchain blockchain is a unique WalytisIdentities identity, and the authorised peers are the WalytisIdentities identity's identity controllers.

#### Offchain Block Management

When a WalytisOffchchain block is created:
- On the underlying Walytis blockchain, a block containing metadata of WalytisOffchain block is added, comprising:
	- ID of the author
	- signature of the author on the WalytisOffchain block content
- In a local encrypted database, the private content is stored, identified by the block ID of the Walytis block containing its metadata.
- Other peers notice the metadata block on the underlying Walytis blockchain, and ask each other to share with them the WalytisOffchain-block's content.
- When a peer asks another peer for the content of a block and the latter has it, the latter ensures the requesting peer is an authorised peer, and transmits to them the block content encrypted with the WalytisOffchain blockchain's WalytisIdentities cryptographic key.


## Source Code

This project's repository is hosted on the following platforms:
- https://github.com/emendir/WalytisOffchain