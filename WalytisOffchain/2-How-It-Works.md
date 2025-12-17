## Relationship Between Private Content and Blockchain

Each WalytisOffchain blockchain is based on a [GroupDidManager](../WalytisIdentities/2-HowItWorks/5-GroupDidManager.md) blockchain that provides identities, authentication and encrypted communication, as well as generic blockchain for storing references to the private content.
The programmer may choose to let these two blockchains be the same.

Private content is NOT stored on the blockchain, it is stored offchain (see [Storage of Private Content](#Storage%20of%20Private%20Content)).
It is, however linked to by the blocks on the blockchain in the following way:
- Each piece of private data is associated with a block on the blockchain, being identified by that block's block ID.
- The associated block contains the following information about the private content:
	- author DID
	- signature of the author on the private content
## Storage of Private Content

Each WalytisOffchain blockchain's private content is stored locally on the device of each peer in a dedicated SQLite database.

### Database Structure

The SQLite database storing a private blockchain's private content contains a single table called 
`BlockContent` with the following fields:
- `block_id` of type blob (binary): the ID of the private content and it's associated block on the blockchain
- `content` of type blob (binary): the private content, encrypted
- `key_id` of type text (string): the key ID of the compound multi-algorithm key used to encrypt the content for storage.

### Storage Encryption

- Private content is stored in the SQLite database encrypted in multiple layers with a KeyGroup object, a compound key comprising multiple keys of different algorithms.
- Each key group is used only a limited number of times, so that if one should get compromised, the blast radius of compromised private content blocks is limited.
- The private keys are managed using a KeyStore object, which stores the private keys in a JSON file encrypted with a single root key that is stored in the KeyStore of the private blockchain's GroupDidManager.


## Transmission of Private Content

- Sensitive offchain-stored content is shared among the members of the WalytisOffchain database-blockchain's GroupDidManager.
- To securely transmit this sensitive data among peers, WalytisOffchain uses [WalytisIdenties' DataTransmission](../WalytisIdentities/2-HowItWorks/7-SecureDataTransmission.md) which ensures data is transmitted with compounded encryption using multiple keys of different algorithms only to authorised peers. WalytisIdentities also takes care of the key management for this, see [WalytisIdentities-KeyManagement](../WalytisIdentities/2-HowItWorks/3-KeyManagement.md).