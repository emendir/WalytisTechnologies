## Goals

- ensure confidentiality, authenticity and integrity of messages
- ensure authenticity and integrity of Group-Identities, User-Identities and Device-Identities

### Notable Non-Goals

Here are some notable security and privacy concerns which Endra does not address:
- device IP addresses are not hidden - tunnel you devices traffic to a trusted VPN server if you need this privacy - this may be addressed in the future (see below)
- existence of users and devices is not actively hidden - this may be addressed in the future by creating a version of the IPFS blockchain that natively supports access-control and encryption

## Attack Vectors

### Network
- Most of the cryptographic processes described in [5-Cryptography](5-Cryptography.md) are designed to protect against network-communications-based attack vectors, such as passive interception and active initiation of communications in any layer of the EndraStack.

#### Spam & DDoS

#TODO
_The following spam and DDoS mitigations have not yet been implemented_
- The addresses for communication endpoints at the Walytis and WalytisIdentities levels will be rotated regularly, and shared secretly among members similarly to Identity-Control Keys.
- Multiple redundant communication endpoints will be used in parallel so that if one is compromised, it can be immediately be deactivated.
### Device

- As described in [Cryptography - Data Storage](5-Cryptography.md#Data%20Storage), data storage on users' devices is encrypted.
- This is managed in a less sophisticated fashion than for networked data because the latter is assumed to be at greater risk.
- For example, no key renewal is currently implemented for the encryption of local storage.

### IP Address Privacy

#### Approaches Proposals
_not implemented, not planned, only under consideration_
#### Multi-IPFS-Networking
- allow a node to use multiple IPFS private networks at once (requires new feature in Walytis)
- keep all sensitive devices in a private network, so that they can't communicate with other peers directly (requires manual configuration)
- have one trusted member in both the private and public IPFS network, forwarding messages between the sensitive devices and all other peers normally (requires manual configuration)

#### Untrusted Relays

- Use private IPFS networks for sensitive devices as above
- Extend WalytisIdentities data transmission protocol to support forwarding messages via relay nodes. These relay nodes are not trusted with message content or identity control keys, but are trusted not to share sensitive devices' IP addresses.