package di.practice;

import dagger.Module;
import dagger.Provides;

import javax.inject.Singleton;

@Singleton
@Module
public class Printer {

  @Provides
  Printer providePrinter() {
    return new Printer();
  }

  public void out(String s) {
    System.out.println(s);
  }
}
