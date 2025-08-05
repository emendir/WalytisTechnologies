## Usage of the Walytis Database-Blockchain

The foundations of communication between nodes running WalytisIdentities is Walytis blockchains.
Walytis is a blockchain that serves as a p2p distributed database.
Every Walytis Identity has its own dedicated blockchain on which it publishes its cryptographic public keys and lists of its controllers.
The data on this blockchain is read by the Identity's controllers and by other identities that wish to interact with it.
A Walytis Identity's identifier (DID) is  `did:walytisidentities:` followed by its blockchain's ID.


## Data Stored on an Identity's Blockchain
- cryptographic key (public key and algorithm)
- list of this identity's controllers (DID and blockchain invitation)
- list of identities of which this identity is a controller
- this identity's DID document

All of the above data can change over time.
To learn how this data authenticated when published, see [3-KeyManagement](3-KeyManagement.md)