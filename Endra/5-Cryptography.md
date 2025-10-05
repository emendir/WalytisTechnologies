Due to the modular nature of Endra's communications architecture, different cryptographic processes are managed by different layers in the [EndraStack](2-EndraStack.md).
This page provides an overview of cryptographic processes in Endra, while the details are explained in the dedicated documentation for the component modules:
- [WalytisOffchain: Content Encryption, Authentication & Storage](../WalytisOffchain/1-IntroToWalytisOffchain.md)
- [WalytisIdentities: Key Managerment](../WalytisIdentities/2-HowItWorks/3-KeyManagement.md)

## Purpose

Cryptographic technologies are employed by Endra to provide three essential features:
- Authenticity: the ability to know who authored information
- Confidentiality: the ability to ensure that only intended recipients have access to sensitive information
- Integrity: the ability to ensure that recipients see only and all relevant data in the original form it was authored

## Areas of Application
### Identity Management

- Key continuity via key succession signatures
- Identities are nested (Groups have multiple Users, Users have multiple devices), each with their own Identity-Keys
- Private keys are securely shared among members via direct transmissions (to be strengthened in the near future with triple-layer encyrption: old group key, member key & spontaneously generated ephemeral key)
- algorithm agnostic (supports multiple different cryptographic algorithms)
- See [WalytisIdentities-KeyManagement](../WalytisIdentities/2-HowItWorks/3-KeyManagement.md).


### Data Transmission

- Sensitive information is transmitted  directly between users' devices.
- Encrypted with key of GroupDidManager
- Will be strengthened in the near future with two more layers of encryption: member's key and spontaneously generated ephemeral key

- In the farther future, I might add support for sensitive data transmission via untrusted relays using double-ratchet cryptography.

### Data Storage

- All private content (e.g. messages) are stored locally on each node/peer's filesystem in an SQLite database (to be encrypted in the near future).
- All private keys are stored locally on each node/peer's filesystem encrypted in a JSON file. 

### Data Indexing and Provenance

- Meaning:
	- ensuring that information is forever organised and discoverable
	- keeping track of what data exists in a dataset, when it was produced and changed
- Endra relies on the blockchain technology in its Walytis databases to ensure data cannot be lost/hidden or fraudulently changed. Essentially, every new piece of data is organised into a block, which references the cryptographic hashes of previous blocks, so that each block is part of a chain that records the existence indirectly the content of all previous blocks. To learn more, see [Block-Chaining](../Walytis/Technical/Block-Chaining.md) and [WalytisBlockchainSecurity](../Walytis/Technical/WalytisBlockchainSecurity.md).



