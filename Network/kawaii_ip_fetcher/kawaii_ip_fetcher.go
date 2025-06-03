package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os/exec"
	"strings"
)

// Fonction pour insérer une ligne vide
func nl() {
	fmt.Println()
}

// Fonction pour générer un ASCII art (en appelant `figlet`)
func figlet(text string) string {
	out, err := exec.Command("figlet", text).Output()
	if err != nil {
		return text // fallback si figlet n'est pas installé
	}
	return string(out)
}

func main() {
	title := "KAWAII IP FETCHER"
	fmt.Println(figlet(title))

	// Obtenir l'adresse IP publique
	resp, err := http.Get("https://ipv4.icanhazip.com/")
	if err != nil {
		fmt.Println("Error fetching IP:", err)
		return
	}
	defer resp.Body.Close()

	ipBytes, _ := ioutil.ReadAll(resp.Body)
	ip := strings.TrimSpace(string(ipBytes))

	// Géolocalisation
	url := "https://geolocation-db.com/jsonp/" + ip
	geoResp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error fetching geolocation:", err)
		return
	}
	defer geoResp.Body.Close()

	body, _ := ioutil.ReadAll(geoResp.Body)
	jsonp := string(body)
	start := strings.Index(jsonp, "(") + 1
	end := strings.LastIndex(jsonp, ")")
	jsonStr := jsonp[start:end]

	var result map[string]interface{}
	if err := json.Unmarshal([]byte(jsonStr), &result); err != nil {
		fmt.Println("Error parsing JSON:", err)
		return
	}

	// Affichage final
	matrix := "Follow the white rabbit"
	ascii1 := ` (\ /) `
	ascii2 := ` ( . .) `
	ascii3 := `C(")(") `

	fmt.Println(matrix)
	nl()
	fmt.Println(ascii1)
	fmt.Println(ascii2)
	fmt.Println(ascii3)
	nl()
	fmt.Println("Your IP address is:", ip)
	fmt.Println("Geolocation data:")
	for k, v := range result {
		fmt.Printf("%-15s: %v\n", k, v)
	}
}

