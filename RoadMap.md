## Summary

The goal of the WalytisTechnologies project is to provide robust peer-to-peer alternatives to server-based communications and productivity tools.

### Achieved

- P2P messenger: A working prototype with builds across desktop and mobile, supporting:
	- group chats & multiple devices per user
	- fully peer-to-peer with conventional and post-quantum end-to-end encryption

### To Do

- P2P messenger:
	- develop maturity
	- audio and video calls
- P2P versioned filesystem sharing
- P2P calendar synchronisation
- P2P git repository synchronisation
- P2P project management

## ✅ Phase I - Reinvent Blockchain ([Walytis](Walytis/Meaning/IntroductionToWalytis.md)) (2019-2024)

- [x] Architecture: proof of concept prototype for non-linear blockchain
- [x] DevOps: automated testing for blockchain
- [x] DevOps: beta maturity for blockchain
- [x] Docs: functionality explanation
- [x] Docs: gettings started

## ✅ Phase II - Develop Functional Endra Stack and App (2024-2025)

- [x] Architecture: identity management ([WalytisIdentities](WalytisIdentities/1-IntroToWalytisIdentities.md))
- [x] Architecture: access control and confidentiality ([WalytisOffchain](WalytisOffchain/1-IntroToWalytisOffchain.md)) 
- [x] Architecture: data mutability ([WalytisMutability](WalytisMutability/1-IntroToWalytisMutability.md))
- [x] DevOps: GUI app ([EndraApp](EndraApp/1-IntroToEndraApp.md))
	- [x] linux standalone executable
	- [x] mobile

## Phase III - Achieve Maturity for Endra Protocol (2025-)

- [x] Architecture: encryption overkill
	- [x] triple-layered encryption (ephemeral, user-level & group-level)
	- [x] hybrid classical & post-quantum encryption
- [ ] Architecture: develop message format (to support various rich text formats & multimedia)
	- [x] extensible message format architecture
	- [x] images
	- [ ] video
	- [x] file attachments
- [ ] Architecture: message relay via untrusted peers
- [ ] Feature: support for audio & video calls
- [ ] Feature: transmission/sharing for large files (with progress tracking)
- [ ] Feature: multiple access levels: identity control, read/write, read-only
- [ ] Performance: improve reliability and speed (to degree necessary for production-grade messaging)
- [ ] Security: minimise metadata leakage
- [x] Packaging: develop build pipelines for Linux Flatpak, Windows, MacOS & Android
- [ ] Testing: develop chaotic simulation test
- [ ] Docs: write protocol specifications for all layers of the Endra Stack

## Phase IV - Build Production-Grade Software

### Endra Stack

- [ ] DevOps: [decide whether to rewrite Endra stack libraries in a compiled language](PortToCompiledSoftware.md)
- [ ] Feat: user-facing backup features
- [ ] Feat: GUI quality-of-life features:
	- [ ] add devices/users via QR-scanning
	- [ ] user profile metadata
	- [ ] search

### Endra App

- [ ] rewrite GUI app in a better GUI framework, with build pipelines for:
	- [ ] Linux flatpak
	- [ ] Linux nix
	- [ ] Linux AUR
	- [ ] Android
	- [ ] Windows
	- [ ] MacOS
	- [ ] iOS

## Ecosystem Expansion

- P2P versioned filesystem shared _(proof of concept working prototype done)_
- P2P git repository synchronisation _(proof of concept working prototyping done)_
- P2P calendar synchronisation _(not yet started)_

These tools will provide the basis for:
- P2P project management _(not yet started)_
