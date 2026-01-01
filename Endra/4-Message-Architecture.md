
# Message Architecture

_This document describes the internal structure of messages._

## Overview

A message has one block on a compound WalytisIdentities-WalytisOffchain-WalytisMutability blockchain, where WalytisIdentities handles encrypted and authenticated transmission, WalytisOffchain offchain storage and transmission, and WalytisMutability editing and versioning message content.

The content of a message is a container for one or more **content parts**.
Each represents a discrete piece of content such as text, images, or audio, and is self-describing via a MIME-compatible media type.

---

### Key Design Goals

For message handling:
- confidentiality: message content should be stored and transmitted securely
- authenticity: messages should be authenticated
- integrity: each device of each user should always have complete un-tampered-with access to all messages ever written
- versioned mutability: messages should be editable, leaving a history of all edits

For message content:
- Support heterogeneous content within a single message
- Provide room for metadata from higher-layer systems
- Be forward-compatible and extensible
- Be data-size efficient in storage and transmission.
- Support efficient overview of all embedded and attached files

---

### Context

- A chat has one or more members, each with one or more devices.
- A message has one or more content blocks, which represent different versions of the message content resulting from edits to the message.
- A content block is immutable. A message being able to have multiple content blocks is what makes the message mutable.
- There is always one active/current content block, which is the content version with the latest timestamp. The rest are treated as history.

---

## Message Content Structure

### Message Content Block

A message content block consists of one or more content parts of mixed media types.

A message content block consists of:
- content block ID
- message metadata (JSON)
- an ordered mixed-type list of content parts

#### Content Part Types

There are different types of content parts which differ in the way the payload and metadata is stored.

##### Embedded Content Part

Simply embeds the payload, media type and rendering metadata.

It consists of:
- content part ID
- rendering metadata (JSON)
- media type (MIME string)
- payload (binary data)

##### Referenced Content Part

Refers to an embedded content part from any message in the same chat.

It consists of:
- content part ID
- referred content block ID and part ID
##### Attached Content Part

Refers to a payload and media type from a file attachment, embeds rendering metadata.

A referenced content part consists of:
- content part ID
- rendering metadata (JSON)
- attachment ID

### Message Attachment Block

A message attachment block contains a payload for a message part which is stored separately from a message content block.

An attachment consists of:
- attachment ID
- media type (MIME string)
- payload (binary data)
- payload size (number of bytes)
- payload hash (algorithm and hash encoded into a string)
- derived properties (JSON)
- user attributes (JSON)


### Notes

- Multiple content parts with the same media type may appear within a single message.
- Content parts are self-contained and independent (excepting part metadata semantics).
- Content part references refer to any part of any message in the current chat.
- Content block IDs are valid and unique within the scope of a chat.
- Content part IDs are valid and unique within the scope of a content block.
- Attachment IDs are valid and unique within the scope of a chat.
- Data stored in Message-metadata SHOULD not be renderable.
- Content part payloads SHOULD be renderable.
- Applications SHOULD render content parts, content part references, and content attachment parts in the same way.
- Applications MAY ignore content parts with media types which they are not programmed to parse.
- Applications MAY ignore content part rendering metadata which they are not programmed to parse and render the content anyway.
- Media type MUST be authoritative for decoding the payload, content part metadata MUST not influence decoding.
- Attachments' derived properties SHOULD be able to be derived deterministically from the payload and media type, SHOULD be media-type specific and SHOULD not influence rendering.
- Attachments' user attributes SHOULD not influence rendering.


---

### Advantageous Features

The message architecture is designed to be extensible:
- New media types can be introduced without changes to the core format.
- Older clients can safely ignore unknown content parts.
- Multiple content parts of the same media type allow for rich message composition.
- Content part references avoid duplicating data across edits to messages and quotes from older messages.
    

This message architecture provides room for application developers to add more features to messages, such as:

- new media types
- message importance/urgency specifiers, via message metadata
- rendering instructions for images, via content part metadata
- compressed content part payloads, via new media types

---

### Message Part Examples

A message containing formatted text and an image might contain the following content parts and references:

1. Embedded Content Part: `text/markdown` - `{"is_quote": true}` - `TEXT_DATA_UTF8`
2. Referenced Content Part: `MESSAGE_ID` - `MESSAGE_PART_ID`
3. Attached Content Part: `{"caption": "Pink Sunset"}` - ATTACHMENT_ID

- Attachment: `image/png` - 10000 bytes - `BINARY_DATA` - `{"height": 100, "width": 100, "title": None}` - `{"filename": "my_image.png", "title_override": "Pink Sunset"}`
---

## Message Content Encoding

Message blocks and message attachment blocks are each, in the entirety of the [content structure described above](#Message%20Content%20Block%20Structure), encoded into binary using Protobuff, following a predefined Protobuff-Schema.
This encoding system is also versioned, so that if the flexibility of the message content structure described above were not to be enough for future developments, the message content structure and encoding could be updated relatively easily.
