package main

import (
	"fmt"
	"net"
	"os"
	"time"

	"golang.org/x/net/icmp"
	"golang.org/x/net/ipv4"
)

func ping(ip string, c chan<- string) {
	conn, err := icmp.ListenPacket("ip4:icmp", "0.0.0.0")
	if err != nil {
		c <- ""
		return
	}
	defer conn.Close()

	msg := icmp.Message{
		Type: ipv4.ICMPTypeEcho,
		Code: 0,
		Body: &icmp.Echo{
			ID:   os.Getpid() & 0xffff,
			Seq:  1,
			Data: []byte("hello"),
		},
	}
	msgBytes, _ := msg.Marshal(nil)

	dst, _ := net.ResolveIPAddr("ip4", ip)
	conn.SetDeadline(time.Now().Add(1 * time.Second))
	_, err = conn.WriteTo(msgBytes, dst)
	if err != nil {
		c <- ""
		return
	}

	reply := make([]byte, 1500)
	_, _, err = conn.ReadFrom(reply)
	if err == nil {
		c <- ip
	} else {
		c <- ""
	}
}

func main() {
	subnet := "192.168.1."
	results := make(chan string)

	for i := 1; i < 255; i++ {
		go ping(fmt.Sprintf("%s%d", subnet, i), results)
	}

	for i := 1; i < 255; i++ {
		host := <-results
		if host != "" {
			fmt.Println("Host actif :", host)
		}
	}
}

