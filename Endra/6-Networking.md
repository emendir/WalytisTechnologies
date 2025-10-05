Endra's networking is based entirely on libp2p, a peer-to-peer networking protocol developed by ProtocolLabs.
Currently, this runs over TCP/IP, but will hopefully support other OSI layer 3 & 4 protocols such as bluetooth as well.

## Network Requirements

- TCP/IP
- _Are bootstrap peers strictly required? #TODO_

## Used LibP2P/IPFS Features

- pubsub
- tunnels (IPFS libp2p stream-mounting)
- IPFS files

## Peer Discovery & Routing

- foundation: IPFS/libp2p
- Peering Acceleration:
	- custom bootstrap nodes
	- remembering relevant peers' recent multi-addresses

## Offline Communications

- _Are bootstrap peers strictly required? #TODO_

### Isolated Networks

### Bridging Isolated Networks to the Internet

_not bridging as in a network bridge_

## Data Transmission

See [How Data is Shared](4-Data-Storage-and-Sync.md#How%20Data%20is%20Shared).

