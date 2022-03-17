package main

import (
	"example.com/v1/config"
	"example.com/v1/order"
	"example.com/v1/server"
	"github.com/gorilla/mux"
	"log"
)

func main() {
	router := mux.NewRouter()
	serv := server.NewBefore(router)
	orderRepo := order.NewRepository()
	log.Println(serv)
	log.Println(orderRepo)
	log.Println(config.ConfigInst)
}
