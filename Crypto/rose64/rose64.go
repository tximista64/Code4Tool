package main

import (
	"bufio"
	"encoding/base64"
	"fmt"
	"os"

	"github.com/common-nighthawk/go-figure"
)

func main() {
	fmt.Println("\033[1;35mPlease enter your Base64 to decode\033[0m") // Texte en magenta clair et gras

	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')

	decoded, err := base64.StdEncoding.DecodeString(input)
	if err != nil {
		fmt.Println("Error decoding Base64:", err)
		return
	}

	fmt.Println(string(decoded))

	myFigure := figure.NewFigure("DONE", "", true)
	myFigure.Print()
}

