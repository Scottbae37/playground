package di.practice;

import dagger.Module;

import javax.inject.Inject;

@Module
@MySingleton
public class Printer {
  public void out(String s) {
    System.out.println(s);
  }


  private final Startable startable;

  @Inject
  public Printer(@ColdStarterQualifier Startable startable) {
    this.startable = startable;
  }

  public void useStarter() {
    startable.starttttt();
  }
}
