package di.practice;
import di.practice.DaggerComponentDag;


public class Dagger2Test {
  public static void main(String args[]) {
    ComponentDag component = DaggerComponentDag.builder().build();
    ComponentDag com2 = DaggerComponentDag.create();
    com2.needPrinterAndModuleA().useModuleA();
    component.printer().out("Out");
    component.needPrinterAndModuleA().useModuleA();
    /**
     * Output:
     *  di.ModuleA@5e481248
     *  Out
     *  di.ModuleA@66d3c617
     */
  }
}
