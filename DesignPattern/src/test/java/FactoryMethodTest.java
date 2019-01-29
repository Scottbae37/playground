import org.junit.jupiter.api.Test;

/**
 * the Factory Method pattern uses inheritance and relies on a subclass to handle the desired object instantiation.
 *
 *  with the Abstract Factory pattern, a class delegates the responsibility of object instantiation to another object via composition
 */

class FactoryMethodTest {
  @Test
  void test() {
  }
}

class ClsForFactoryMethod {
  public void doSomething() {
    Foo f = makeFoo();
    f.whatever();
  }

  protected Foo makeFoo() {
    return new RegularFoo();
  }

  private class RegularFoo implements Foo {
    @Override
    public void whatever() { }
  }
}

class ClsForFactoryMethodB extends ClsForFactoryMethod {
  protected Foo makeFoo() {
    //subclass is overriding the factory method
    //to return something different
    return new SpecialFoo();
  }

  private class SpecialFoo implements Foo {

    @Override
    public void whatever() {

    }
  }
}

class ClsAbstractFactory {
  private Factory factory;

  public ClsAbstractFactory(Factory factory) {
    this.factory = factory;
  }

  public void doSomething() {
    //The concrete class of "f" depends on the concrete class
    //of the factory passed into the constructor. If you provide a
    //different factory, you get a different Foo object.
    Foo f = factory.makeFoo();
    f.whatever();
  }

}

interface Foo {
  void whatever();
}

interface Factory {

  Foo makeFoo();

  Bar makeBar();

  Aycufcn makeAmbiguousYetCommonlyUsedFakeClassName();

  class Bar {

  }

  class Aycufcn {

  }
}

class ConcreteFactory implements Factory {

  @Override
  public Foo makeFoo() {
    return null;
  }

  @Override
  public Bar makeBar() {
    return null;
  }

  @Override
  public Aycufcn makeAmbiguousYetCommonlyUsedFakeClassName() {
    return null;
  }
}

//need to make concrete factories that implement the "Factory" interface here