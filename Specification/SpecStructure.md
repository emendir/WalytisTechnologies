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

- Purpose #informative
- Overview #informative
- Required Services #normative
	- interface specification
	- required behaviour
	- limitations
	- _when a requirement is a service provided by another layer in the stack, simply refer to it rather than respecifying/redefining it_
- Provided Services #normative
	- interface specification
	- guaranteed behaviour
	- limitations
- State Model #normative
	- objects
	- state machines / lifecycle
	- algorithms?
	- invariants
- Protocol #normative
	- data model
	- protocol state machine
	- wire format
	- algorithms
	- failure semantics
- Security Model #normative
	- trust model
	- threat model
	- adversary model
	- security boundaries
	- public-facing metadata
	- _assumptions, guarantees & limitations are documented under 'Required Services' and 'Provided Services'_
- Security Analysis #informative
- Design Rationale #informative
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