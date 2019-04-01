package di.practice;

import dagger.Module;
import dagger.Provides;

import javax.inject.Inject;
import javax.inject.Singleton;

@Module/*(includes = {ColdStarterModule.class})*/
@MySingleton
public class Printer {
  public void out(String s) {
    System.out.println(s);
  }


  private final Startable startable;

  @Inject
  public Printer(@ColdStarterQulifier Startable startable) {
    this.startable = startable;
  }

  public void useStarter() {
    startable.starttttt();
  }
}
