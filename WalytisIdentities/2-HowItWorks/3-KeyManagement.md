The key management system described in [1-CoreConcepts](1-CoreConcepts.md) poses many challenges.
Here is how WalytisIdentities makes this work.

### Communication Keys

The cryptographic algorithm and public keys used by a WalytisIdentity for securing communications with other peers are published in a DID document on its blockchain.

### Identity Control Keys

To authenticate published DID-documents, a set of cryptographic keys called identity-control-keys (or simply control keys) are used.
A set of control keys comprises multiple public-private key pairs for different cryptographic algorithms.
The cryptographic algorithms used are documented in [8-CryptographicAlgorithms](8-CryptographicAlgorithms.md).
Currently, the control-keys are also used as communication-keys, but in future versions of WalytisIdentities they may become distinct.
These keys' public parts are published on the identity's blockchain in dedicated blocks (`ControlKeyBlock`).
Ownership of these control keys means ownership of the identity.

For security, identity-control-keys are regularly renewed.
New keys' public parts is published on the identity's blockchain and signed by its predecessor keys, forming an uninterruptedly authenticated lineage of keys.
In other words, key continuity is ensured across key renewal via key succession signatures.

WalytisIdentities' control key-management system's scope is limited to ensuring there is always one currently valid ephemeral set of identity-control-keys.
DID-Document management is independent of control-key management: At any time, a DID-document can be created, signed and published with the current control key.


### Key Renewal Procedure

Renewing identity-control-keys is a little tricky when an Identity has multiple controllers.
Here's how this is achieved to ensure all controllers always have ownership of the currently valid identity-control-keys:

1. Once the current identity-control-key have reached a certain age, one of the identity controllers will at random generate a new set of keys and share them with the other identity controllers.
2. Once all the identity controllers have the new keys or a threshold key age is reached, one of the identity controllers will at random publish a new block of type `ControlKeyBlock` on the blockchain, declaring the old and new keys' public parts, and signs this information with the old control keys. With this publication the old control keys are deprecated and all other identities are informed of this new control keys.


### Private Key Storage

With so many cryptographic keys being generated automatically over time, WalytisIdentities needs to manage storing them.
Each software instance of a WalytisIdentity stores all the keys it ever generated in an encrypted local database.
When instantiating a WalytisIdentity object in software, a master key needs to be provided for unlocking this local encrypted key storage database.
