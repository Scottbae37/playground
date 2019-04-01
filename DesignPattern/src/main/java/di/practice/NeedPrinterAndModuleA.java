package di.practice;

import javax.inject.Inject;

@MySingleton
public class NeedPrinterAndModuleA {
//  @Inject
  ModuleA moduleA;
  private final Printer printer;
  private final Startable startable;


  //  @MySingleton --> Error msg: @Scope annotations are not allowed on @Inject constructors. Annotate the class instead.
  @Inject
  public NeedPrinterAndModuleA(ModuleA moduleA, Printer printer, Startable startable) {
    this.moduleA = moduleA;
    this.printer = printer;
    this.startable = startable;
  }

  void useModuleA() {
    printer.out(moduleA.toString());
  }

  @Inject
  void useStarter(){
    startable.starttttt();
  }
}
