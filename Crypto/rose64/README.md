# 🌹 rose64

## Description

Initially written in python  **rose64** is a minimalist and playful Base64 decoder written in Go. The program prompts the user to input a Base64-encoded string, decodes it, and prints the result. It also includes a decorative ASCII art header rendered using the `go-figlet` library (external dependency).

## Features

- Decodes Base64-encoded strings
- Displays fancy ASCII art with the message "DONE"
- Lightweight and terminal-friendly

## Requirements

- Go (version 1.23 or later)
- External dependency: [`github.com/common-nighthawk/go-figure`](https://github.com/common-nighthawk/go-figure)

Install the dependency using:

```bash
go get github.com/common-nighthawk/go-figure
```

## Usage

Run the program:

```bash
go run rose64.go
```

Sample output:

```bash
Enter your Base64 to decode:
SGVsbG8sIFdvcmxkIQ==
Hello, World!
 ____     ___    _   _   _____
 |  _ \   / _ \  | \ | | | ____|
 | | | | | | | | |  \| | |  _|
 | |_| | | |_| | | |\  | | |___
 |____/   \___/  |_| \_| |_____|
```

## License

This project is licensed under the MIT License. Nevermind you probably won't  fork this thing

