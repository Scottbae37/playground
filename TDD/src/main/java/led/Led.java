package led;

public class Led {
  private boolean isOn;

  public Led() {
    this.isOn = true;
  }

  public boolean getIsOn() {
    return isOn;
  }

  public void setIsOn(boolean on) {
    isOn = on;
  }
}
