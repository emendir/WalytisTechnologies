# Cryptography

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
_See [WalytisIdentities-KeyManagement](../WalytisIdentities/2-HowItWorks/3-KeyManagement.md)._

- Each Identity has its own Identity-Key (also called Identity-Control Key) used for authentication and encryption.
- Identities are nested (e.g. Groups have multiple Users, Users have multiple devices), each with their own Identity-Keys. A Super-Identity always has one or more Member-Identities.
- Identity-Keys are ephemeral and regularly renewed.
- Identity-Key continuity is ensured via key succession signatures.
- During key renewal of a Super-Identity, private keys are securely shared among its Member-Identities via direct transmissions using a triple-layer encryption scheme (see [Data Transmission](#Data%20Transmission)).
- This cryptography is algorithm agnostic (supports multiple different cryptographic algorithms).
- In the future, multiple different cryptographic algorithms will be used at the same time to provide resistance to zero-day vulnerabilities in cryptographic algorithms #TODO.


### Data Transmission
_See [WalytisIdentities-SecureDataTransmission](../WalytisIdentities/2-HowItWorks/7-SecureDataTransmission.md)._

- Sensitive information is transmitted  directly between users' devices.
- This always happens in the context of a nested identity: two Identities who are both members of the same Super-Identity. 
- Sensitive content is encrypted with three groups of keys from different owners/scopes:
	- Super-Identity's key: to ensure the message can only be read by someone who knows the Super-Identity's private keys
	- Key of the recipient Identity: to ensure the message can only be read by someone who knows the intended recipient Identity's private keys
	- Ephemeral session-specific key: to maintain confidentiality should the above Identity-Keys both be compromised, as well as to provide perfect forward secrecy and post-compromise security should this ephemeral key itself be compromised also.
- For each of the three key ownership/scope groups listed above, multiple keys for different cryptographic algorithms are used to provide resistance to zero-day vulnerabilities in cryptographic algorithms (hybrid cryptography). The cryptographic algorithms used are documented in [8-CryptographicAlgorithms](8-CryptographicAlgorithms.md).

- In the farther future, I might add support for sensitive data transmission via untrusted relays using something like double-ratchet cryptography. #TODO

### Data Storage

- All private content (e.g. messages) are stored locally on each node/peer's filesystem in an SQLite database (to be encrypted in the near future). #TODO
- All private keys are stored locally on each node/peer's filesystem encrypted in a JSON file. 

### Data Indexing and Provenance

- Meaning:
	- ensuring that information is forever organised and discoverable
	- keeping track of what data exists in a dataset, when it was produced and changed
- Endra relies on the blockchain technology in its Walytis databases to ensure data cannot be lost/hidden or fraudulently changed. Essentially, every new piece of data is organised into a block, which references the cryptographic hashes of previous blocks, so that each block is part of a chain that records the existence indirectly the content of all previous blocks. To learn more, see [Block-Chaining](../Walytis/Technical/Block-Chaining.md) and [WalytisBlockchainSecurity](../Walytis/Technical/WalytisBlockchainSecurity.md).

## Post-Compromise Recovery

_What security goals are compromised to what extent by various cryptographic breaches._

#TODO


