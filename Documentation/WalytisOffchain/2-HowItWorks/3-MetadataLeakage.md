# Metadata Leakage

## Categories of Confidentiality

For modelling the protection level of data, we will categorise data into the following:
- **Exposed**: visible to an outside observer
- **Protected**: shared encryptedly with authorised peers
- **Secret**: shared with full encryption to identity members

An outside observer may be any node on the network that can intercept IP traffic to and from a WalytisOffchain node.

### Exposed

- IP address
- IPFS peer ID
- sender and receiver addresses of peer communication packets

### Protected

_Not yet implemented. Currently, the items listed here are exposed. Walytis has already been rearchitected to allow for secured communications._

- IDs of running blockchains
- Walytis block IDs and content
	- control keys' public parts
	- DID documents
	- member join/leave events
	- super join/leave events
	- key ownership declarations (for preparing next public key)

### Secret

- control keys' private parts
- courier keys
- WalytisOffchain block content

## Note on IPFS

It is assumed that IPFS does NOT protect:
- the addresses of its communications endpoints for IPFS-PubSub and IPFS-Tunneling (LibP2PStreamMounting)
- sharing of IPFS content
- peer ID

From these, an outside observer might determine the following:
- IDs of all blockchains being run
- all Walytis blocks of known blockchains (if IpfsBlockshare is used)
