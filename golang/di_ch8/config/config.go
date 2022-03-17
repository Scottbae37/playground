package config

import (
	"github.com/jinzhu/configor"
	"time"
)

var ConfigInst *config

type config struct {
	ServerAddress string        `env:"ADDRESS" default:"0.0.0.0"`
	ServerPort    int           `env:"PORT" default:"8888"`
	ReadTimeout   time.Duration `env:"READ_TIMEOUT" default:"1000000000"`
	DbPort        int32         `env:"DB_PORT" default:"3333"`
	DbSource      string        `env:"DB_SOURCE" default:"maas:123d@tcp(10.77.222.222:5345)/mdaas_b_?charset=utf8&parseTime=True"`
}

func init() {
	ConfigInst = new(config)
	if err := configor.New(&configor.Config{Debug: true}).Load(ConfigInst); err != nil {
		panic(err)
	}
}
