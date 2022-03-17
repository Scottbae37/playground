package order

import (
	"example.com/v1/config"
	"log"
)

type Repository struct {
	db interface{}
}

func NewRepository() *Repository {
	return &Repository{}
}

func (r *Repository) Connect() {
	r.db = mockedDbConn(config.ConfigInst.DbSource, config.ConfigInst.DbPort)
}

func mockedDbConn(dbSource string, dbPort int32) interface{} {
	log.Println(dbSource, dbPort)
	return nil
}
