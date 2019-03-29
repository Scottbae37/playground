package di.coffee;

import dagger.Lazy;
import javax.inject.Inject;

class CoffeeMaker {
  private final Lazy<Heater> heater; // Create a possibly costly heater only when we use it.
  private final Pump pump;
  private final MugCup mugCup;

  @Inject CoffeeMaker(Lazy<Heater> heater, Pump pump, MugCup mugCup) {
    this.heater = heater;
    this.pump = pump;
    this.mugCup = mugCup;
  }

  public void brew() {
    heater.get().on();
    pump.pump();
    System.out.println(" [_]P coffee! [_]P ");
    heater.get().off();
  }

  public Pump getPump() {
    return pump;
  }
}