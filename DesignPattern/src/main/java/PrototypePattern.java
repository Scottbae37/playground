import java.util.ArrayList;
import java.util.List;

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