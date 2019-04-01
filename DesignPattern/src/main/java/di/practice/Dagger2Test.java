package di.practice;

import di.practice.DaggerComponentDag;


public class Dagger2Test {
  public static void main(String args[]) {
    ComponentDag com1 = DaggerComponentDag.builder()
            .hotStarterExternalModule(new HotStarterExternalModule(new HotStarter()))
            .build();
    ComponentDag com2 = DaggerComponentDag.builder()
            .hotStarterExternalModule(new HotStarterExternalModule(new HotStarter()))
            .build();
    com1.printer().out("Out");
    com1.needPrinterAndModuleA().useModuleA();
    com1.needPrinterAndModuleA().useModuleA();
    com2.needPrinterAndModuleA().useModuleA();
    com2.needPrinterAndModuleA().useModuleA();


    Printer p1_1 = com1.printer();
    Printer p1_2 = com1.printer();
    System.out.println(p1_1 + " - p1_1");
    System.out.println(p1_2 + " - p1_2");
    assert p1_1.equals(p1_2);

    Printer p2_1 = com2.printer();
    Printer p2_2 = com2.printer();
    System.out.println(p2_1 + " - p2_1");
    System.out.println(p2_2 + " - p2_2");
    assert p2_1.equals(p2_2);

    System.out.println(com1.needPrinterAndModuleA());
    System.out.println(com1.needPrinterAndModuleA());
    System.out.println(com2.needPrinterAndModuleA());
    System.out.println(com2.needPrinterAndModuleA());

    p1_1.useStarter();
    com1.needPrinterAndModuleA().useStarter();
    /**
     * Output:
     *  Out
     *  di.practice.ModuleA@355da254
     *  di.practice.ModuleA@355da254
     *  di.practice.ModuleA@4dc63996
     *  di.practice.ModuleA@4dc63996
     *  di.practice.Printer@d716361 - p1_1
     *  di.practice.Printer@d716361 - p1_2
     *  di.practice.Printer@6ff3c5b5 - p2_1
     *  di.practice.Printer@6ff3c5b5 - p2_2
     *  di.practice.NeedPrinterAndModuleA@3764951d
     *  di.practice.NeedPrinterAndModuleA@3764951d
     *  di.practice.NeedPrinterAndModuleA@4b1210ee
     *  di.practice.NeedPrinterAndModuleA@4b1210ee
     */
  }
}
