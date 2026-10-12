# Style Guide

### Normative Statement Categories and Identifiers

This specification uses the following classes of normative statements, which are each assigned identifiers consisting of a category prefix and sequence number:
- `R` identifies dependency statements (incl. limitations).
- `G` identifies guarantee statements (incl. limitations).
- `P` identifies protocol-semantic statements.
- `I` identifies implementation requirements.

 The identifier is normative and may be used to reference the statement elsewhere in this specification.

### Normative Declarations of Dependency Requirements and Limitations

Formulate positive assumptions as requirements and negative assumptions as limitations.
Separate these two categories.
Use RFC 2119 requirement level vocabulary for the requirements.
Do NOT use RFC 2119 requirement level vocabulary for the limitations. Use the term 'might' instead of 'may' in normal sentence case.

For Example:
```
## Dependencies

### Network

#### Requirements

R000 The underlying network MUST provide IP connectivity using at least one supported IP version.

#### Limitations:

R000 Any given peer might not have the newest blocks at a given point in time.
```

### Normative Declarations of Guarantees and Limitations

Use the following RFC 2119 inspired vocabulary and formatting for guarantees:
- **WILL** describes behaviour guaranteed by this specification. It is a statement of the externally observable behaviour of a conforming implementation, rather than an instruction to the implementer.
- **MAY** describes optional behaviour defined by this specification.
Do NOT use the above or RFC 2119 requirement level vocabulary for the limitations. Use the term 'might' instead of 'may' in normal sentence case.

For Example:
```
## Provided Services

### Blockchain

#### Guarantees

G000 The block content associated with a block identifier WILL NOT ever change over time.

#### Limitations

G000 Any given peer might not have the newest blocks at a given point in time.
```

### Normative Declarations of Protocol Semantics and Behaviour

Use factual statements.
Do NOT use RFC 2119 requirement level vocabulary.


For Example:
```
P000 Messages with incorrect signatures are ignored.
```

### Normative Declarations of Requirements for Implementations

```
I000 The implementation MUST tolerate unexpected termination and subsequent restart.
```

## Basic Language

### Spelling

Use Australian spelling.

### Syntax and Punctuation

### Prose Lists

Use the serial comma (aka. Oxford comma).

### Bulleted Lists

When writing lists, do NOT join list elements with commas, full-stops or  coordinating conjunction such as "and" or "or".

Instead of:
```
The operating environment MUST provide

- access to persistent local storage,
- access to the network and
- a source of cryptographically secure random data.
```

Write:
```
The operating environment MUST provide the following:

- the ability to execute the system implementation as a persistent process or service
- access to persistent local storage
- access to the network
- a source of cryptographically secure random data
```