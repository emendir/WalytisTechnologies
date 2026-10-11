WalytisIdenties is built with the future vulnerability of cryptographic algorithms in mind.
It provides two approaches to protecting against compromised algorithms:
- In the short term, hybrid cryptography ensures the compromise to a single algorithm is not enough to compromise operation, because all cryptographic operations, both encryption and signing, are performed with multiple algorithms in parallel
- In the long term, WalyitsIdentities can easily implement novel algorithms to replace deprecated ones.
## Hybrid Cryptography

As of `walytis_identities` `v0.4.0`, the following cryptographic algorithms are used compounded with each other for identity control and secure data transmission:
- Conventional cryptography:
	- `ECIES-secp256k1` (encryption and signing) (provided by the [ECIES](https://github.com/ecies/py) and [coincurve](https://github.com/ofek/coincurve) libraries)
- Post-Quantum cryptography (provided by [liboqs from the Open-Quantum-Safe project](https://github.com/open-quantum-safe))
	- `ML-KEM-1024` (encryption only)
	- `ML-DSA-87` (signing only)

Group-DID-Manger invitation codes only use `ECIES-secp256k1` for verifying the authenticity of the inviter, but the communication security is immediately upgraded to the same set of algorithms listed above for secure data transmission.


## Cryptographic Flexibility

WalytisIdentities can easily replace deprecated cryptographic algorithms with newer ones.
The library which contains various algorithms used is [MultiCrypt](https://github.com/emendir/multi_crypt)