
## What Endra Data is Stored Where

On the database-blockchains of Devices, Users, and Groups, the following information is stored (in addition to the identity management data stored by the WalytisIdenties system):
- Groups:
	- chat messages
- Users:
	- user profile (not yet implemented)
- Devices:
	- 
To lean how Identity information is stored (DIDs, cryptographic keys, relationships between users and devices and groups), see the WalytisIdentities documentation for [DidManager](../WalytisIdentities/2-HowItWorks/4-DidManager.md), [GroupDIDManager](../WalytisIdentities/2-HowItWorks/5-GroupDidManager.md) and [DidManagerWithSupers](../WalytisIdentities/2-HowItWorks/6-DidManagerWithSupers.md).

## How Endra Data is Stored

The above data is stored using the WalytisOffchain overlay for privacy and WalytisMutability for mutability.
Let's explain this here using the example of chat messages, though the other data listed above is stored in the same manner.

- Layer Endra: message - the user-generated and -consumed content of the message
- Layer WalytisMutability: message versions - each edit, deletion and restoration event for a message is recorded as a separate block, all time-stamped and linked to the original block belonging to the message
- Layer WalytisOffchain: offchain storage - each message version block, including the message content, endra metadata and mutability metadata is stored offchain in a local database ((to be encrypted in the near future) on each device and transmitted between peers in an encrypted and authenticated fashion.
- Layer Walytis: here, for each offchain-block, only the time-stamp, author-DID and signatures of their offchain-stored content are stored.

## How Data is Shared

Due to the modular layered nature of the [Endra Stack](2-EndraStack.md), the way data is transmitted is complicated and multi-faceted.

- Layer WalytisOffchain: encrypted content stored off-chain is [transmitted between peers](../WalytisOffchain/1-IntroToWalytisOffchain.md) over [IPFS TCP](https://docs.ipfs.tech/reference/kubo/rpc/#api-v0-p2p-forward) tunnels using the [IPFS-DataTransmission protocol from IPFS-Toolkit](https://github.com/emendir/IPFS-Toolkit-Python#ipfs-datatransmission) . This data is only transmitted to peers upon authentication and is encrypted for transmission.
- Layer Walytis: Walytis blocks are shared as IPFS files. The existence of blocks [is communicated via](../Walytis/Technical/LeafBlockBroadcasts.md) [IPFS-PubSub](https://docs.ipfs.tech/concepts/libp2p/#publish-subscribe).


## Sensitive and Unsensitive Data

#TODO