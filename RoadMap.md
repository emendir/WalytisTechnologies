
## ✅ Phase I - Reinvent Blockchain ([Walytis](Walytis/Meaning/IntroductionToWalytis.md)) (2019-2024)
- [x] proof of concept
- [x] automated testing
- [x] beta maturity
- [x] documentation

## ✅ Phase II - Develop Functional Endra Stack and App (2024-2025)

- [x] identity management ([WalytisIdentities](WalytisIdentities/1-IntroToWalytisIdentities.md))
- [x] access control and confidentiality ([ToWalytisOffchain](WalytisOffchain/1-IntroToWalytisOffchain.md)) 
- [x] mutability ([WalytisMutability](WalytisMutability/1-IntroToWalytisMutability.md))
- [x] GUI app ([EndraApp](EndraApp/1-IntroToEndraApp.md))
	- [x] linux standalone package
	- [x] mobile

## Phase III - Achieve Protocol Maturity (2025-)

- [ ] Endra Protocol: improve reliability and speed (to degree necessary for production-grade messaging)
	- [ ] develop chaotic simulation test
- [ ] WalytisOffchain: make appropriate for large files (with progress tracking)
- [ ] Endra Protocol: develop message format (to support various rich text formats & multimedia)
- [ ] Endra App: develop build pipelines for Windows & MacOS
- [ ] WalytisOffchain: private IPFS repos with ephemeral swarm keys
- [ ] Endra Protocol & App: support for audio & video calls

## Phase IV - Transform into Production-Grade Software
### Endra Stack

[rewrite Endra stack libraries in a compiled language](PortToCompiledSoftware.md)
- [ ] Walytis
- [ ] WalytisIdentities
- [ ] WalytisOffchain
- [ ] WalytisMutability
- [ ] EndraProtocol

### Endra App
- [ ] rewrite GUI app in a better GUI framework, with build pipelines for:
	- [ ] Linux flatpak
	- [ ] Linux nix
	- [ ] Android
	- [ ] Windows
	- [ ] MacOS
	- [ ] iOS

## Parallel Projects

- P2P git server _(prototyping, unpublished)_
- P2P CalDAV server _(not yet started)_
- P2P filesystem synchronisation/NextCloud alternative _(working prototype)_
