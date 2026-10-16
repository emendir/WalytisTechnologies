# Blockchain Configuration

A blockchain configuration WILL define any of the following fields:

| Name                         | Description                                                | Format/Type                      |
| ---------------------------- | ---------------------------------------------------------- | -------------------------------- |
| `max content length`         | maximum number of bytes a block's content may have         | positive integer or null         |
| `max custom metadata length` | maximum number of bytes a block's custom metadata may have | positive integer null            |
| `max number of parents`      | maximum number of parents a block may have                 | integer greater than `1` or null |
