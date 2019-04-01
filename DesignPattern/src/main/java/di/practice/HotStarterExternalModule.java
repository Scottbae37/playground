package di.practice;

import dagger.Module;
import dagger.Provides;

@Module
public class HotStarterExternalModule {
  private final Startable startable;

  public HotStarterExternalModule(Startable startable) {
    this.startable = startable;
  }

  @Provides
  @MySingleton
  public Startable provideStarter() {
    return startable;
  }
}
