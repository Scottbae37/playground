package solution;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static junit.framework.TestCase.assertEquals;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;

public class FizzBuzzTest {

    private FizzBuzz cut;

    @BeforeEach
    public void setUp() {
        cut = new FizzBuzz();
    }

    @Test
    public void test_0_is_0() {
        assertEquals("0", cut.of(0));
    }

    @Test
    public void test_1_is_1() {
        assertEquals("1", cut.of(1));
    }

    @Test
    public void test_2_is_2() {
        assertEquals("2", cut.of(2));
    }

    @Test
    public void test_3_is_Fizz() {
        assertThat(cut.of(3), is("Fizz"));
    }

    @Test
    public void test_4_is_4() {
        assertThat(cut.of(4), is("4"));
    }

    @Test
    public void test_5_is_Buzz() {
        assertThat(cut.of(5), is("Buzz"));
    }

    @Test
    public void test_6_is_Fizz() {
        assertThat(cut.of(6), is("Fizz"));
    }

    @Test
    public void test_9_is_Fizz() {
        assertThat(cut.of(9), is("Fizz"));
    }

    @Test
    public void test_10_is_Buzz() {
        assertThat(cut.of(10), is("Buzz"));
    }

    @Test
    public void test_15_is_FizzBuzz() {
        assertThat(cut.of(15), is("FizzBuzz"));
    }

    @Test
    public void acceptanceTest() {
        assertThat(cut.of(3 * 3 * 3 * 5 * 5 * 5 * 5 * 3 * 5), is("FizzBuzz"));
    }
}
