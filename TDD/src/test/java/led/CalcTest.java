package led;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalcTest {
    Calc cut;

    @After
    public void tearDown() throws Exception {

        cut = null;
    }

    @Before
    public void setUp() throws Exception {
        cut = new Calc();

    }

    @Test
    public void testAdd() throws Exception {
        //Setup
        int a, b;
        a = 1;
        b = 2;
        int result, expected;
        expected = 3;

        //Exercise
        result = cut.add(a, b);
        //Verify
        assertEquals(expected, result);
        //Tear down
    }
    @Test
    public void testAdd_should_return_neg5(){
       int a, b;
       a = -1;
       b =-2;
       int result = cut.add(a,b);

       assertEquals(-3, result);
    }

    @Test
    public void testAdd_shouldReturn0_withSameValueButWithOppositeSign() throws Exception {
        //setup
        int a = 5, b = -a;
        int expected = 0;
        int actual;
        //exercise
        actual = cut.add(a, b);
        //verify
        assertEquals(expected, actual);
        //tear-down
    }

}
