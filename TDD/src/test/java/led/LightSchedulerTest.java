package led;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class LightSchedulerTest {
    private static final int EVERYDAY = 1;
    private static final int MONDAY = 2;

    LightScheduler cut;
//    SpyLedController spyLedController;
//    FakeTimeService fakeTimeService;
    @Before
    public void setUp() throws Exception {
        cut = new LightScheduler();
//        spyLedController = new SpyLedController();
//        fakeTimeService = new FakeTimeService();
    }
    @After
    public void tearDown() throws Exception {
        cut = null;
//        spyLedController = null;
//        fakeTimeService = null;
    }
/*
    @Test
    public void test_does_nothing_schedule_on_everyday_when_not_time_yet() throws Exception {
        //setup
        cut.makeSchedule(3, EVERYDAY, 1200);
        FakeTimeService fakeTimeService = new FakeTimeService();
        fakeTimeService.setDay(MONDAY);
        fakeTimeService.setMinute(1199);

        cut.setLedControllableImpl(spyLedController);

        //exercise
        cut.wakup();

        //verify
        assertEquals(LIGHT_ID_UNKNOWN, spyLedController.getLastControlledLedId());
        assertEquals(LIGHT_STATE_UNKNOWN, spyLedController.getLastLedState());
        //tear-down
    }
*/

    @Test
    public void test_new_does_nothing_with_ledcontroller() throws Exception {
        //setup

        //exercise

        //verify
//        assertEquals(LIGHT_ID_UNKNOWN, spyLedController.getLastControlledLedId());
//        assertEquals(LIGHT_STATE_UNKNOWN, spyLedController.getLastLedState());
        //tear-down
    }
}
