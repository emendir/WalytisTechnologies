The key management system described in [1-CoreConcepts](1-CoreConcepts.md) poses many challenges.
Here is how WalytisIdentities makes this work.

### Communication Keys

The cryptographic algorithm and public keys used by a WalytisIdentity for securing communications with other peers are published in a DID document on its blockchain.

### Identity Control Keys

To authenticate published DID-documents, a set of cryptographic keys called control-keys are used.
Currently, the control-keys are also used as communication-keys, but in future versions of WalytisIdentities they may become distinct.
These keys' public parts are published on the identity's blockchain in dedicated blocks (`ControlKeyBlock`).
Ownership of these control keys means ownership of the identity.

For security, these keys are regularly renewed.
Each new key's public part is published on the identity's blockchain, signed by its predecessor key, forming an uninterruptedly authenticated lineage of keys.

WalytisIdentities' control key-management system's scope is limited to ensuring there is always one currently valid ephemeral control key.
DID-Document management is independent of control-key management: At any time, a DID-document can be created, signed and published with the current control key.


### Key Renewal Procedure

Renewing control keys is a little tricky when an Identity has multiple controllers.
Here's how this is achieved to ensure all controllers always have ownership of the currently valid control key:

1. Once the current control key has reached a specific age, one of the identity controllers will at random generate a new key and share it with the other identity controllers.
2. Once all the identity controllers have the new key or a threshold key age is reached, one of the identity controllers will at random publish a new block `ControlKeyBlock` on the blockchain, declaring the old and new keys' public parts, and signs this information with the old control key. With this publication the old control key is deprecated and all other identities are informed of this new control key.


### Private Key Storage

With so many cryptographic keys being generated automatically over time, WalytisIdentities needs to manage storing them.
Each software instance of a WalytisIdentity stores all the keys it ever generated in an encrypted local database.
When instantiating a WalytisIdentity object in software, a master key needs to be provided for unlocking this local encrypted key storage database.