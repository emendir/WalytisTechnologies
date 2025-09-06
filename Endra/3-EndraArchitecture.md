# Endra Architecture

| Endra Object              | Walytis Tech Class                                       | Description                                         |
| ------------------------- | -------------------------------------------------------- | --------------------------------------------------- |
| User Identity / Profile   | GroupDidManager                                          | a user account                                      |
| Device Identity / Profile | GroupDidManager                                          | a device associated with a user account             |
| Message                   | MutaBlock                                                | a message created by a User Identity                |
| Correspondence            | GroupDidManager/<br>PrivateBlockchain/<br>MutaBlockchain | a collection of messages by specific set Identities |

- A **User Identity** has one or more devices (**Device Identities**).
- A **Correspondence** has one or more members (**User Identities**).
- A **Message** has one author (**User Identity**) author and one **Correspondence**.

```mermaid

erDiagram
    USER_IDENTITY {
        DeviceIdentity[] deviceIdentities
    }

    DEVICE_IDENTITY {
        UserIdentity user
    }

    CORRESPONDENCE {
        UserIdentity[] members
    }

    MESSAGE {
        UserIdentity author
        Correspondence correspondence
    }

    %% Relationships
    USER_IDENTITY ||--o{ DEVICE_IDENTITY : "user's devices"

    CORRESPONDENCE ||--o{ USER_IDENTITY : " correspondence's members"

    MESSAGE ||--|| USER_IDENTITY : "message author"
    MESSAGE }o--|| CORRESPONDENCE : "correspondence's messages"
```

### Notable Features

- With its **Correspondences** (analog to 'chats' or 'chat-rooms' in other messengers), Endra does NOT differentiate between chats that have only two members and chats that have more than two members ('direct chats' and 'group chats').