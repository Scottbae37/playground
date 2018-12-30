package led;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Iterator;

import static org.junit.Assert.*;

public class LedDriverTest {
    private LedDriver cut;
    private ArrayList<Led> spyLedList;
    static final int numOfLedToCreate = 16;

    @Before
    public void setUp() throws Exception {
        cut = LedDriver.getLedDriverInst();
        spyLedList = new ArrayList<Led>();
//        numOfLedToCreate = 16;
        addLed(spyLedList, numOfLedToCreate);
        cut.create(spyLedList);
    }

    private void addLed(ArrayList<Led> list, int num) {
        for (int i = 0; i < num; i++) {
            list.add(new Led());
        }
    }

    @After
    public void tearDown() throws Exception {
        cut = null;
        if(!spyLedList.removeAll(spyLedList)){
            System.out.println("Remove error");
            fail("Error at List remove");
        }
    }

    @Test
    public void testCreate_should_turn_off_all_leds_after_create() throws Exception {
        //setup
        //exercise
        cut.create(spyLedList);
        //verify
        Iterator<Led> iter = spyLedList.iterator();
        while (iter.hasNext()) {
            assertFalse(iter.next().getIsOn());
        }
        //test-down
    }

    @Test
    public void testTurnOn_should_turn_on_selected_led() throws Exception {
        //setup
        int ledNum = 0;
        boolean expected = true;

        //exercise
        cut.turnOn(ledNum);
        //verify
        assertEquals(expected, spyLedList.get(0).getIsOn());
        //tear-down
    }
    @Test
    public void testTurnOn_should_turn_on_selected_led_while_other_leds_keep_stay() throws Exception {
        //setup
        int ledNum = 0;
        int otherLeds[] = new int[]{1, 2, 3, 4};
        boolean expected = true;

        //exercise
        cut.turnOn(ledNum);
        boolean dd;
        for(int idx:otherLeds)
            cut.turnOff(idx);
        //verify
        assertEquals(expected, cut.getIsOn(ledNum));
        for(int idx:otherLeds)
            assertFalse(cut.getIsOn(idx));
        //tear-down
    }

    @Test
    public void testTurnOff_should_turn_off_selected_led() throws Exception {
        //setup
        boolean expected = false;
        int ledNum = 1;
        //exercise
        cut.turnOff(ledNum);
        //verify
        assertEquals(expected, cut.getIsOn(ledNum));
        //tear-down
    }

    @Test
    public void testTurnOnAll_should_turn_on_all_leds() throws Exception {
        //setup
        //exercise
        cut.turnOnAll();
        //verify
        for(int i = 0; i < numOfLedToCreate; i++)
            assertTrue(cut.getIsOn(i));
        //tear-down
    }

    @Test
    public void testTurnOffAll_should_turn_off_all_leds() throws Exception {
        //setup
        //exercise
        cut.turnOnAll();
        cut.turnOffAll();
        //verify
        for(int i = 0; i < numOfLedToCreate; i++)
            assertFalse(cut.getIsOn(i));
        //tear-down
    }

    @Test(expected = IndexOutOfBoundsException.class)
    public void testTurnOn_should_throw_exception_when_invalid_led_idx() throws Exception {
        //setup
        final int invalidIdx = -1;
        //exercise
        cut.turnOff(invalidIdx);
        //verify

        //tear-down
    }

    @Test
    public void testTurnOff_should_turn_off_selected_led_when_boundary_values() throws Exception {
        //setup
        final int boundaryIdxA = 0;
        final int boundaryIdxB = spyLedList.size() - 1;
        //exercise
        cut.turnOnAll();
        cut.turnOff(boundaryIdxA);
        cut.turnOff(boundaryIdxB);
        //verify
        assertFalse(cut.getIsOn(boundaryIdxA));
        assertFalse(cut.getIsOn(boundaryIdxB));
        //tear-down
    }

    @Test
    public void testTurnOn_should_turn_on_selected_led_array() throws Exception {
        //setup
        int ledNums[] = new int[]{1, 5, 6, 8, 2};
        boolean expected = true;
        //exercise
        cut.turnOn(ledNums);
        //verify
        for(int idx:ledNums)
            assertEquals(expected, cut.getIsOn(idx));
        //tear-down
    }
    @Test
    public void testTurnOff_should_turn_off_selected_led_array() throws Exception {
        //setup
        int ledNums[] = new int[]{1, 5, 6, 8, 2};
        boolean expected = false;
        //exercise
        cut.turnOnAll();
        cut.turnOff(ledNums);
        //verify
        for(int idx:ledNums)
            assertEquals(expected, cut.getIsOn(idx));
        //tear-down
    }

}
