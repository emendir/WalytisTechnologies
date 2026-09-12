
To achieve the level of metadata protection defined in [_Metadata Leakage_](../../WalytisOffchain/2-HowItWorks/3-MetadataLeakage.md#Metadata%20Leakage), WalytisIdentities protects the traffic of the [Walytis layer](../../Endra/2-EndraStack.md#The%20Walytis%20Database%20Blockchain%20-%20The%20Data%20Sharing%20Layer) which WalytisIdentities is built on by taking control of the [IPFS/libp2p layer](../../Endra/2-EndraStack.md#IPFS) which [Walytis layer](../../Endra/2-EndraStack.md#The%20Walytis%20Database%20Blockchain%20-%20The%20Data%20Sharing%20Layer) is built on.

WalytisIdentities gives its Walytis layer, to replace Walytis' IPFS layer, a wrapper around libp2p with the following features:
- file sharing: encrypted and limited to authorised WalytisIdentities peers
- pubsub: unencrypted, authenticated by WalytisIdentities peers
- tuntran: encrypted and authenticated communications via the TunTran protocol

## Authorised Peers

By default, authorised peers are set to all members and supers of the WalytisIdentity.
In the future, this may be extended to a user-defined list of "observers".