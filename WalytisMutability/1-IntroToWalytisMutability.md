### Walytis Blockchain Overlay Features

WalytisMutability is an overlay for the Walytis blockchain, providing an abstracted blockchain with features that the core Walytis blockchain itself does not have.

Compared to the Walytis blockchain, WalytisOffchain has the following unique features:
- mutability: blocks can be edited or deleted on the abstracted overlay blockchain
- block history: old versions of blocks and deleted blocks will always be retrievable

Thanks to the modular architecture of the Walytis Technologies, WalytisMutability can be combined with WalytisOffchain which provides encryption & authentication.


## How it Works
### Block Creation

- On the underlying Walytis blockchain, a new block is added with the WalytisMutability block's content as its content, and a block topic of `MutaBlock-Original`.
- The ID of this Walytis block becomes the ID of the WalytisMutability block.

### Block Editing

- On the underlying Walytis blockchain, a new block is added with the WalytisMutability block's new content as its content, and two block topics: `MutaBlock-Update` and the block ID of the WalytisMutability block being edited. 

### Block Deletion

- On the underlying Walytis blockchain, a new block is added with the meaningless placeholder content and two block topics: `MutaBlock-Deletion` and the block ID of the WalytisMutability block being edited.