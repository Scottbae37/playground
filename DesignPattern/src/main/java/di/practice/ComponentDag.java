package di.practice;

import dagger.Component;

import javax.inject.Singleton;

@Singleton
@Component(modules = {Printer.class})
public interface ComponentDag {
  Printer printer();
  NeedPrinterAndModuleA needPrinterAndModuleA();
}
