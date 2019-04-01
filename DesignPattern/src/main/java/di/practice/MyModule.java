package di.practice;

import dagger.Module;
import dagger.Provides;

@Module(includes = {Printer.class})
public class MyModule {
  @Provides
  @MySingleton
  public NeedPrinterAndModuleA provideNeedPrinterAndModuleA(ModuleA moduleA, Printer printer, Startable startable) {
    return new NeedPrinterAndModuleA(moduleA, printer, startable);
  }
}
