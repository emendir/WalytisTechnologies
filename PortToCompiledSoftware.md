Currently, all components of [Walytis Technologies](ReadMe.md) that make up the [Endra stack](Endra/2-EndraStack.md) are written in Python.
Once they reach maturity, they will be rewritten in a compiled language, for the reasons described below.

## Reasons and Aims

- improve portability and compatibility with a wide range of programming languages and frameworks
- improve performance

## Candidate Languages

### Rust
- better portability, easier to integrate in other languages and frameworks
	- better WASM support
	- runtime-free
	- smaller binary size
	- better fine-grained control over dependencies
- higher performance
- more powerful toolchains
- easier to interoperate with python for gradual migration
- wider and deeper cryptography ecosystem

### Go
- canonical IPFS/libp2p implementation
- easier code semantics
- slightly easier toolchains for mobile


## Scope

### Inclusions
- the Walytis Technologies software libraries that make up the [Endra stack](Endra/2-EndraStack.md)

### Notable Exclusions
- testing framework
- GUI app (to be rewritten in a better cross-platform GUI framework, maybe Flutter, for example)