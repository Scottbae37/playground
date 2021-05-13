package config

type Config struct {
	Port int `yaml:"port"`
}

func New(filename string) *Config {

	return &Config{}
}
