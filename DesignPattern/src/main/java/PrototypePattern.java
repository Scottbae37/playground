import java.util.ArrayList;
import java.util.List;

/**
 *
 * Intent
 * > specifying the kind of objects to create using a prototypical instance
 * > creating new objects by copying this prototype
 *
 * Specific problems and implementation
 * > Using a prototype manager
 *  - 동적으로 생성 삭제 할 수 있는 객체들의 registry를 만들어 보관하고, 이를
 * protytype manger라 하고 객체들을 관리함
 *
 * 비슷하지만, 약간 다른 객체를 생성할 때, 새로 생성하는 것 보다는 Clone 하여,
 * 다른 부분만 바꿔서 확장하여 사용함. Clone 할 때, Deep-copy를 할 것인지
 * Shallow-copy를 할 것인지는 상황에 따라
 *
 * @see <a href "https://www.oodesign.com/prototype-pattern.html">https://www.oodesign.com/prototype-pattern.html</a>
 */
public class PrototypePattern {
  public static void main(String[] args) throws Exception {
    Table table = new Table(100, 200);
    table.add("Led Light");
    table.print();

    Table s2 = table.clone();
    s2.print();

    table.add("Drawer");
    System.out.println();

    table.print();
    s2.print();
  }
}

class Table implements Cloneable {
  private int width;
  private int height;
  private List<String> accList = new ArrayList<>();

  public void add(String name) {
    accList.add(name);
  }

  public Table(int width, int height) {
    this.setWidth(width);
    this.setHeight(height);
  }

  public void setWidth(int width) {
    this.width = width;
  }

  public void setHeight(int height) {
    this.height = height;
  }

  public void print() {
    System.out.println("width = " + width);
    System.out.println("height = " + height);
    for (String each : accList) System.out.println("acc = " + each);
  }

  @Override
  protected Table clone() throws CloneNotSupportedException {
    Table copy = (Table) super.clone();
    copy.accList = new ArrayList<>(); // clone method provides Shallow copy
    copy.accList.addAll(accList);        // For Deep copy, Need to copy elements as well

    return copy;
  }
}