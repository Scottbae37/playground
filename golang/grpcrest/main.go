package main

import (
	"github.com/Scottbae37/playground/golang/grpcrest/config"
	"log"
)

func main() {
	conf := config.New("filename.yaml")
	log.Printf("%d\n", conf.Port)
	log.Println("Hello golang")
}
