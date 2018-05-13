package org.bjs;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.Date;

public class FakeTimeServiceTest {
    private FakeTimeService cut;

    @Before
    public void setUp() throws Exception {
        cut = new FakeTimeService();
    }

    @After
    public void tearDown() throws Exception {
        cut = null;
    }

    @Test
    public void test_new_does() throws Exception {
        //setup
        
        //exercise

        //verify

        //tear-down
    }

    @Test
    public void test_getTime_returns_time_as_it_set() throws Exception {
        //setup
//        cut.set
        //exercise

        //verify

        //tear-down
    }
}
