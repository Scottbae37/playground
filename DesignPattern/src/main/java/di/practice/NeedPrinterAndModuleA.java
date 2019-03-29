package di.practice;

import javax.inject.Inject;

public class NeedPrinterAndModuleA {
  @Inject
  ModuleA moduleA;
  Printer printer;

  @Inject
  public NeedPrinterAndModuleA(Printer printer) {
    this.printer = printer;
  }

  void useModuleA() {
    printer.out(moduleA.toString());
  }
}
