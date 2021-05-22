package nameinverter

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestNameInverter_Invert(t *testing.T) {
	tests := []struct {
		name  string
		input string
		want  string
	}{
		{name: "Empty name returns empty string", input: "", want: ""},
		{name: "Empty name returns empty string", input: "  ", want: ""},
		{name: "First returns first", input: " John ", want: "John"},
		{name: "First last returns last, first", input: " John Smith", want: "Smith, John"},
		{name: "Honorifics first name last name returns last, first", input: "Mr. John Smith", want: "Smith, John"},
		{name: "Honorifics first name last name returns last, first", input: "Mrs. John Smith", want: "Smith, John"},
		{name: `should invert "John Smith Sr." to "Smith, John Sr."`, input: "John Smith Sr.", want: "Smith, John Sr."},
		{name: `should invert "John Smith Sr. PhD." to "Smith, John Sr. PhD."`, input: "John Smith Sr. PhD.", want: "Smith, John Sr. PhD."},
		{name: `Acceptance test should invert "Mr. John Smith Sr. PhD." to "Smith, John Sr. PhD."`, input: "Mr. John Smith Sr. PhD.", want: "Smith, John Sr. PhD."},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			assert.Equal(t, NameInverter{}.Invert(test.input), test.want)
		})
	}
}
