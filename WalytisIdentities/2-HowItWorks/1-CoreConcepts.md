### W3C's DID-Specification
WalytisIdentities implements the [World-Wide-Web-Consoritum's (W3C's) Decentralised Identifiers (DIDs) specifications](https://www.w3.org/TR/did-core/) because those specifications align its approach to managing identities and their cryptographic cores.
In the DID specification's model, WalytisIdentities is a [DID method](https://www.w3.org/TR/did-core/#methods),

The concepts discussed here which lie at the core of what WalytisIdentities is and how it works match the DID specification, and I have included the homologous terminology of the specification in rounded brackets and italicised font for reference where it differs. 
The full scope of the DID specification comprises much more than what WalytisIdentities implements as described here.


### Core Concepts
- **Digital Identity _(DID subject)_**: An identity the sense required in the context of secure communications, for example when saying "Identity A encrypts a message so that only Identity B can decrypt it, and Identity B verifies that the received message was indeed authored by Identity A"
- Identity ID (DID): A globally unique persistent identifier, identifying a digital identity. In WalytisIdentities, this is a string that starts with `did:walytisidentities:` followed by a case-sensitive letters.
- **Identity Controller** _(DID Controller)_: An entity that has full control over a digital identity by owning its private keys, giving it the power to decrypt messages addressed to the digital identity and to sign messages, proving they were authored by the digital identity. A digital identity can have many controllers. The controllers can be humans, other digital identities, user-devices - in WalytisIdentities they are whichever parts of the system store and handle cryptographic keys.
- **public-private key cryptography**: The well established cryptography system that is the basis of most modern secured communications, used for encryption and authentication. WalytisIdentities uses a cryptography library _(cryptographic suite)_ called [MultiCrypt](https://github.com/emendir/multi_crypt) that supports multiple cryptographic algorithms, and keys belonging to identities are renewed regularly.
- **DID Documents:** A publication declaring the DID, the current cryptographic keys _(verification method)_ and optionally the identity controllers _(DID controllers)_.


