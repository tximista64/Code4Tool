# KAWAII IP FETCHER

##  Description

Initially written in python3 **KAWAII IP FETCHER** is a small and playful Go program that:

- Fetches your **public IP address**
- Retrieves your **geolocation information** using an external API
- Displays an ASCII art banner using `figlet`
- Prints a cute "white rabbit" matrix-style message

---

##  Features

- Public IP lookup via [icanhazip.com](https://icanhazip.com)
- Geolocation lookup via [geolocation-db.com](https://geolocation-db.com)
- ASCII art rendering using `figlet`
- Lightweight and beginner-friendly

---

##  Requirements

- **Go 1.16+**
- **figlet** (for ASCII art banner)

You can install `figlet` on Debian-based systems using:

```bash
sudo apt install figlet
```
---

##  Installation

1. Clone the repository:

```bash
git clone https://github.com/tximista64/Code4Tool
```
2. Enter in the dir

```bash 
cd Network/kawaii_ip_fetcher/
```

3. Run it

```bash
 go run kawaii_ip_fetcher.go
```

---

##  Dependencies

    net/http — HTTP client

    encoding/json — for parsing JSON

    os/exec — to call figlet

---

## Example Output

```bash
 _  __    ___        ___    ___ ___   ___ ____
| |/ /   / \ \      / / \  |_ _|_ _| |_ _|  _ \
| ' /   / _ \ \ /\ / / _ \  | | | |   | || |_) |
| . \  / ___ \ V  V / ___ \ | | | |   | ||  __/
|_|\_\/_/   \_\_/\_/_/   \_\___|___| |___|_|

 _____ _____ _____ ____ _   _ _____ ____
|  ___| ____|_   _/ ___| | | | ____|  _ \
| |_  |  _|   | || |   | |_| |  _| | |_) |
|  _| | |___  | || |___|  _  | |___|  _ <
|_|   |_____| |_| \____|_| |_|_____|_| \_\


Follow the white rabbit

 (\ /)
 ( . .)
C(")(")

Your IP address is: 64.64.64.64
Geolocation data:
postal         : 64210
latitude       : 43.4376° N
longitude      : -1.5913° W
IPv4           : 64.64.64.64
state          : Lapurdi
country_code   : EH
country_name   : Euskal Herria
city           : Bidarte
```

---

## License
MIT
Feel free to modify the source for your own fun!
