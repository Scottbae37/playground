package di.practice;

import dagger.Module;
import dagger.Provides;

@Module
public class ColdStarterModule {
  @Provides
  @MySingleton
  @ColdStarterQualifier
  public Startable provideStarter() {
    return new ColdStarter();
  }
}
