package fizzbuzz

import "strconv"

type FizzBuzz struct {
}

func (f *FizzBuzz) Of(n int) string {
	// Corner case
	if n == 0 {
		return "0"
	}
	return f.of(n)
}

func (f *FizzBuzz) of(n int) string {
	s := ""
	if n%3 == 0 {
		s += "Fizz"
	}
	if n%5 == 0 {
		s += "Buzz"
	}
	if !isEmpty(s) {
		return s
	}
	return strconv.Itoa(n)
}

func isEmpty(s string) bool {
	return len(s) < 0
}
