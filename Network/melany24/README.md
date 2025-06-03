# Melany24 (Go version)

##  Description

This program is a simple ICMP Echo Request (ping) scanner written in Go.  
It scans a local `/24` subnet by sending ICMP packets to each address from `.1` to `.254`.  
Any host that replies to the ping is considered active and its IP is printed.

Originally, this tool was a shell script but has been rewritten in Go for better performance. 

---

##  Features

- Concurrent scanning of all IPs in a subnet
- ICMP Echo Request (like the `ping` command)
- Fast response detection using goroutines
- Prints active hosts

---

##  Requirements

- **Go 1.23 or later**
- Root privileges (needed to send raw ICMP packets)
- Local network with a reachable `/24` subnet (e.g., `192.168.1.0/24`)

---

##  Installation

1. Make sure Go is installed:
   ```bash
   go version
   ```

2. Clone the repository or copy the source code into a file named `icmp_scanner.go`.

3. Initialize Go modules (if needed):
   ```bash
   go mod init melany24.go
   go get golang.org/x/net/icmp
   go get golang.org/x/net/ipv4
   ```

---

## 🚦 Usage

Run the program as root (ICMP needs admin rights):

```bash
sudo go run melany24.go
```

Example output:

```
Active host: 192.168.1.1
Active host: 192.168.1.14
Active host: 192.168.1.38
...
```

---

##  Limitations

- Only works on `/24` subnets (hardcoded prefix)
- Requires root access
- No error handling for invalid or unreachable subnets

---

##  License
MIT
Feel free to modify the source for your own fun!
