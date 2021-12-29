package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	//conf := config.New("filename.yaml")
	//log.Printf("%d\n", conf.Port)
	//log.Println("Hello golang")
	f := func(c rune) bool {
		return !unicode.IsLetter(c) && !unicode.IsNumber(c)
	}
	fmt.Printf("%q", strings.FieldsFunc("af,,,;;; fa'sad',11", f))
}
