
| Name                     | Description                                                                      | Format/Type          |
| ------------------------ | -------------------------------------------------------------------------------- | -------------------- |
| `generation number`      | length of shortest chain to the last convergence blocks in this block's ancestry | non-negative integer |
| `number of ancestors`    | how many ancestors this block has had since the last convergence blocks          | non-negative integer |
| `last convergence block` | identifier of last convergence block                                             | Block Identifier     |

## Generation Number

For Genesis Blocks, Generation Number IS `0`.

For Post-Genesis Blocks, Generation number IS equal to the lowest value of all the Generation Numbers of the blocks referenced by the Parent Identifiers plus one.

$$
g(b) =
\begin{cases}
0 & \text{if } b \text{ is genesis},\\
1 + \min\limits_{p \in P(b)} g(p) & \text{otherwise}.
\end{cases}
$$

Where:
- $b$ is a block.
- $P(b)$ is the set of parent blocks of $b$.
- $g(b)$ is the generation number of $b$.

## Number of Ancestors

For Genesis Blocks, Number of Ancestors IS `0`.

For Post-Genesis Blocks, the field Number of Ancestors IS equal to the number of blocks in the union of the sets of the ancestries of all the blocks referenced by the Parent Identifiers plus the Number of Parents.

$$
A(b) = P(b) \cup \bigcup_{p \in P(b)} A(p)

$$

Where:

- $b$ is a block.
- $P(b)$ is the set of parent blocks of $b$.
- $A(b)$ is the set of all ancestors of $b$.
- $a(b)$ is the number of ancestors of $b$.