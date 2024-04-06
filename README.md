# cidrtool

`cidrtool` is a simple command line tool to manipulate CIDR blocks.

## Usage

### Expand netblock

`cidrtool --expand` reads a list of CIDR blocks from stdin and expands them to a list of IP addresses.

```shell
echo "192.168.0.0/16" | cidrtool --expand
```

### Collapse netblocks

`cidrtool --collapse4` or `--collapse6` reads a list of IP v4 or v6  addresses from stdin and collapses them to a list of CIDR blocks.

```shell
echo "192.0.2.0/25
192.0.2.128/25" | cidrtool --collapse4
```

## Requirements

`cidrtool` requires Python 3. In particular, `/usr/bin/env python3` must be a usable Python 3 interpreter. 

## Installation

### Debian/derivatives via apt repository

Install my Debian repository, if you haven't already:

```shell
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://dist.cdzombak.net/deb.key | sudo gpg --dearmor -o /etc/apt/keyrings/dist-cdzombak-net.gpg
sudo chmod 0644 /etc/apt/keyrings/dist-cdzombak-net.gpg
echo -e "deb [signed-by=/etc/apt/keyrings/dist-cdzombak-net.gpg] https://dist.cdzombak.net/deb/oss any oss\n" | sudo tee -a /etc/apt/sources.list.d/dist-cdzombak-net.list > /dev/null
sudo apt-get update
```

Then install `cidrtool` via `apt-get`:

```shell
sudo apt-get install cidrtool
```

### macOS via Homebrew

```shell
brew install cdzombak/oss/cidrtool
```

## License

`cidrtool` is licensed under the LGPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Author

Chris Dzombak
- [dzombak.com](https://dzombak.com)
- [github.com/cdzombak](https://github.com/cdzombak)
