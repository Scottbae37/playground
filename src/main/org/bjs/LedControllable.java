package org.bjs;

public interface LedControllable {
  static final int LIGHT_ID_UNKNOWN = -1;
  static final int LIGHT_STATE_UNKNOWN = -1;

  public void turnOn(int index);

  public void turnOff(int index);
}
