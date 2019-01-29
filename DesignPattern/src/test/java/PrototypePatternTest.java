import com.google.common.collect.Lists;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;
import static org.junit.jupiter.api.Assertions.assertFalse;

class PrototypePatternTest {

  @BeforeEach
  void setUp() {

  }

  @Test
  void testShallowCopy() throws CloneNotSupportedException {
    Prototype prototypeA = new Prototype();
    Prototype prototypeB = (Prototype) prototypeA.clone();

    prototypeA.addComponent("GasolineEngine");

    prototypeB.addComponent("Engine");
    prototypeB.setWithWheel(true);

    assertThat(prototypeA.isWithWheel(), is(false));
    assertThat(prototypeB.isWithWheel(), is(true));
    assertThat(prototypeA.getComponents(), is(prototypeB.getComponents()));

    System.out.println("========== Shallow copy ===========");
    printComponents(prototypeA, prototypeB);
  }

  @Test
  void testDeepCopy() throws CloneNotSupportedException {
    Prototype prototypeA = new ProtoTypeWithDeep();
    Prototype prototypeB = (Prototype) prototypeA.clone();

    prototypeA.addComponent("GasolineEngine");

    prototypeB.addComponent("Engine");
    prototypeB.setWithWheel(true);

    assertThat(prototypeA.isWithWheel(), is(false));
    assertThat(prototypeB.isWithWheel(), is(true));

    assertFalse(Arrays.equals(prototypeA.getComponents(), prototypeB.getComponents()));

    System.out.println("========== Deep copy ===========");
    printComponents(prototypeA, prototypeB);
  }

  private void printComponents(Prototype protoTypeA, Prototype protoTypeB) {
    for (String each : protoTypeA.getComponents())
      System.out.println("A: " + each);

    for (String each : protoTypeB.getComponents())
      System.out.println("B: " + each);
  }
}

class ProtoTypeWithDeep extends Prototype {
  @Override
  protected Prototype clone() throws CloneNotSupportedException {
    Prototype prototype = (Prototype) super.clone();

    prototype.list = Lists.newArrayList();
    prototype.list.addAll(list);

    return prototype;
  }
}

class Prototype implements Cloneable {
  private boolean withWheel;

  protected List<String> list;

  public Prototype() {
    list = Lists.newArrayList();
  }

  public void setWithWheel(boolean withWheel) {
    this.withWheel = withWheel;
  }

  public boolean isWithWheel() {
    return withWheel;
  }

  @Override
  protected Prototype clone() throws CloneNotSupportedException {
    return (Prototype) super.clone();
  }

  public void addComponent(String component) {
    list.add(component);
  }

  public String[] getComponents() {
    return (String[]) list.toArray(new String[list.size()]);
  }
}
