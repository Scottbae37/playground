package nameinverter

import (
	"fmt"
	"strings"
)

type NameInverter struct {
}

func (n NameInverter) Invert(name string) string {
	nameParts := n.breakingIntoPartsIgnoringWhitespace(name)
	if n.hasOnlyFirstName(nameParts) {
		return nameParts[0] // First name
	}
	return n.invert(n.withoutHonorifics(nameParts))
}

func (n NameInverter) breakingIntoPartsIgnoringWhitespace(name string) []string {
	s := strings.Trim(name, " ")
	names := strings.Split(s, " ")
	return names
}

func (n NameInverter) hasOnlyFirstName(nameParts []string) bool {
	return len(nameParts) < 2
}

func (n NameInverter) withoutHonorifics(nameParts []string) []string {
	if IsHonorific(nameParts[0]) {
		return nameParts[1:]
	}
	return nameParts
}

func (n NameInverter) invert(nameParts []string) string {
	lastName := nameParts[1]
	firstName := nameParts[0]
	postNominal := n.findAndMergerPostnominal(nameParts)

	return strings.Trim(fmt.Sprintf("%s, %s %s", lastName, firstName, postNominal), " ")
}

func (n NameInverter) findAndMergerPostnominal(nameParts []string) string {
	var postNominal string
	for _, s := range nameParts[2:] {
		postNominal += s + " "
	}
	return postNominal
}
