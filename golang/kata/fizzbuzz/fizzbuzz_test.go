package fizzbuzz

import (
	"container/list"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/suite"
	"log"
	"testing"
)

func TestFizzBuzzSuite(t *testing.T) {
	suite.Run(t, &TestSuite{})
}

type TestSuite struct {
	suite.Suite
	cut FizzBuzz
}

func (s *TestSuite) SetupTest() {
	log.Println("SetupTest")
	s.cut = FizzBuzz{}
}

func (s TestSuite) TestOf0is0() {
	assert.Equal(s.T(), "0", s.cut.Of(0))
}

func (s TestSuite) TestOf1is1() {
	assert.Equal(s.T(), "1", s.cut.Of(1))
}

func (s TestSuite) TestOf3isFizz() {
	assert.Equal(s.T(), "Fizz", s.cut.Of(3))
}

func (s TestSuite) TestOf5isBuzz() {
	assert.Equal(s.T(), "Buzz", s.cut.Of(5))
}

func (s TestSuite) TestOf6isFizz() {
	assert.Equal(s.T(), "Fizz", s.cut.Of(6))
}

func (s TestSuite) TestOf10isBuzz() {
	assert.Equal(s.T(), "Buzz", s.cut.Of(10))
}

func (s TestSuite) TestOf15isFizzBuzz() {
	assert.Equal(s.T(), "FizzBuzz", s.cut.Of(15))
}

func (s TestSuite) TestAcceptanceTest() {
	assert.Equal(s.T(), "FizzBuzz", s.cut.Of(3*3*3*5*5*5*5))
}

func (s TestSuite) TestN() {
	input := []int{20, 7, 23, 19, 10, 15, 25, 8, 13}
	var ans []int = sol(input)

	log.Println(ans)
}

func sol(nums []int) []int {
	// 2개를 제거해 100을 만들기
	// 제거할 위치를 담는 애
	sum := 0
	l := list.New()
	for _, num := range nums {
		sum += num
		l.PushBack(num)
	}
	return solve(l, sum)
}

func solve(l *list.List, sum int) []int {

}
