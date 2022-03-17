package server

import (
	"example.com/v1/config"
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
	"time"
)

func NewBefore(r *mux.Router) http.Server {
	srv := http.Server{
		Addr:         fmt.Sprintf("%s:%d", config.ConfigInst.ServerAddress, config.ConfigInst.ServerPort),
		ReadTimeout:  config.ConfigInst.ReadTimeout,
		WriteTimeout: 10 * time.Second,
		IdleTimeout:  120 * time.Second,
		Handler:      r,
	}
	return srv
}
