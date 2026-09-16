###  Overall Integration Architecture

- Purpose #informative
- Overview #informative
	- Technology Stack
		- layer responsibilities
- Provided Services #normative
- Required Services #normative
- State Model #normative
- Security Model #normative
- Security Analysis #informative
- Design Rationale #informative

### Per Layer

1. Purpose #informative
2. Provided Services #normative
	- interface specification
	- guaranteed behaviour
	- limitations
3. Required Services #normative
	- interface specification
	- required behaviour
	- limitations
	- _when a requirement is a service provided by another layer in the stack, simply refer to it rather than respecifying/redefining it_
4. System Overview #informative
5. State Model #normative
	- objects
	- state machines / lifecycle
	- algorithms?
	- invariants
6. Protocol #normative
	- data model
	- protocol state machine
	- wire format
	- algorithms
	- failure semantics
7. Security Model #normative
	- trust model
	- adversary model
	- threat model
	- security boundaries
	- public-facing metadata
	- _assumptions, guarantees & limitations are documented under 'Required Services' and 'Provided Services'_
8. Security Analysis #informative
9. Design Rationale #informative
- Versioning #normative

### Per Implementation

- Implementation Documentation #informative
- API Reference #normative
- Testing Documentation #informative
- Design Rationale #informative
- Versioning #normative



### Future ToDos

- preformance expectations
- traceability: give normative specs stable identifiers
- compatibility
- conformance