package di.practice;

import dagger.Component;

@MySingleton
@Component(modules = {MyModule.class, HotStarterExternalModule.class, ColdStarterModule.class})
public interface ComponentDag {
  Printer printer();

  NeedPrinterAndModuleA needPrinterAndModuleA();
}
