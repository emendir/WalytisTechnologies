### Configure Host Docker-Net Interface Addr in IPFS Config

Kubo doesn't always automatically listen on the virtual interface connected to the docker network (e.g. `172.1.0.1/16`).
You can force kubo to listen to this in its config file: https://github.com/ipfs/kubo/blob/master/docs/config.md#addressesappendannounce

Quic Transports may cause problems in automated tests with docker.
You can disable them for the docker interface on the host.

For example, in `~/.ipfs/config`:
```json
{
	"Addresses": {
		"AppendAnnounce": [
			"/ip4/172.17.0.1/tcp/4001",
			"/ip6/fe80::4891:1dff:fe4a:bdea/tcp/4001"
		],
		"NoAnnounce": [
			"/ip4/172.17.0.1/udp/4001/quic-v1",
			"/ip4/172.17.0.1/udp/4001/quic-v1/webtransport",
			"/ip6/fe80::4891:1dff:fe4a:bdea/udp/4001/quic-v1",
			"/ip6/fe80::4891:1dff:fe4a:bdea/udp/4001/quic-v1/webtransport"
		],
	}
}
```