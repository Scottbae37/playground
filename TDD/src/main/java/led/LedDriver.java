package led;

import java.util.ArrayList;
import java.util.Iterator;

class LedDriver implements LedControllable {
  private ArrayList<Led> leds;

  static LedDriver getLedDriverInst() {
    LedDriver inst = new LedDriver();
    inst.leds = new ArrayList<Led>();
    return inst;
  }

  private LedDriver() {
  }

  void create(ArrayList<Led> led) {
    Iterator<Led> iter = led.iterator();
    while (iter.hasNext()) {
      iter.next().setIsOn(false);
    }

    iter = led.iterator();
    while (iter.hasNext()) {
      leds.add(iter.next());
    }

  }

  @Override
  public void turnOn(int index) {
    leds.get(index).setIsOn(true);
  }

  @Override
  public void turnOff(int index) {
    leds.get(index).setIsOn(false);
  }

  void turnOnAll() {
    Iterator<Led> iter = leds.iterator();
    while (iter.hasNext())
      iter.next().setIsOn(true);
  }

  void turnOffAll() {
    Iterator<Led> iter = leds.iterator();
    while (iter.hasNext())
      iter.next().setIsOn(false);
  }

  boolean getIsOn(int index) {
    return leds.get(index).getIsOn();
  }

  void turnOn(int[] ledNums) {
    for (int idx : ledNums)
      leds.get(idx).setIsOn(true);
  }

  void turnOff(int[] ledNums) {
    for (int idx : ledNums)
      leds.get(idx).setIsOn(false);
  }
}
