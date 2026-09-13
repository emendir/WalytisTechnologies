# Style Guide

### Normative Statement Categories and Identifiers

This specification uses the following classes of normative statements, which are each assigned identifiers consisting of a category prefix and sequence number:
- `D` identifies dependency statements.
- `P` identifies protocol-semantic statements.
- `I` identifies implementation requirements.

 The identifier is normative and may be used to reference the statement elsewhere in this specification.

### Normative Declarations of Dependency Requirements and Assumptions

Formulate positive assumptions as requirements and negative assumptions as assumptions.
Separate these two categories.
Use RFC 2119 requirement level vocabulary for the requirements.
Do NOT use RFC 2119 requirement level vocabulary for the assumptions. Use the term 'might' instead of 'may'.

For Example:
```
## Dependencies

### Network

#### Requirements

D000 The underlying network MUST provide IP connectivity using at least one supported IP version.

#### Assumptions:

D000 The IP network endpoint provided might operate behind a NAT.
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


## General Syntax

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