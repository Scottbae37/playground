public class FactoryMethod {
  /**
   * 객체를 생성하는 인터페이스를 정의하지만,
   * 인스턴스를 만들 클래스의 결정은 서브클래스가 한다.
   * Factory Method 패턴에서는 클래스의 인스턴스를 만드는 시점을
   * 서브클래스로 미룬다.
   * <p>
   * AbstractFactory는 다르게 상속을 사용하여, 하위 클래스가 Factory Method 를 override 하여 객체 생성
   * https://stackoverflow.com/questions/5739611/differences-between-abstract-factory-pattern-and-factory-method
   *
   * the Factory Method pattern uses inheritance and relies on a subclass to handle the desired object instantiation.
   *
   * with the Abstract Factory pattern, a class delegates the responsibility of object instantiation to another object via composition
   */

  /**
   * Intent
   * - Defines an interface for creating objects, but let subclasses to decide which class to instantiate
   * - Refers to the newly created object through a common interface
   *
   * Applicability & Examples
   *  - The need for implementing the Factory Method is very frequent. The cases are the ones below:
   *   > when a class can't anticipate the type of the objects it is supposed to create
   *   > when a class wants its subclasses to be the ones to specific the type of a newly created object
   *
   */
  public static void main(String[] agrs) {
    DriverFactory f = new SlmDriverFactory();
    Driver driver = f.create(true, 70.5f);

    DriverFactory factory = new SlmDriverFactory();
    driver = factory.create(true, 99.9f);
  }

  //FIXME: BAD
  Driver createTaxiDriver() {
    return new TaxiDriver();
  }

  //FIXME: BAD
  Driver createBusDriver() {
    return new BusDriver();
  }
}

abstract class DriverFactory {
  final Driver create(boolean needWork, float percents) {
    // driver의 생성 후 할 일을 공통으로 관리한다.
    Driver driver = createDriver();
    driver.setCondition(percents);
    if (needWork)
      driver.drive();

    return driver;
  }

  // 구체적인 생성은 하위 클래스가 수행하도록 추상 메소드를 선언한다.
  abstract protected Driver createDriver(); /// Factory Method
}

interface Driver {
  void setCondition(float percent);

  void drive();
}

// 구체적인 객체의 생성을 구현한다.
class SlmDriverFactory extends DriverFactory {
  @Override
  protected Driver createDriver() {
    return new TaxiDriver();
  }

}

class TaxiDriver implements Driver {
  @Override
  public void setCondition(float percent) {
    System.out.println("TaxiDriver's condition " + percent + "%");
  }

  @Override
  public void drive() {
    System.out.println("TaxiDriver is driving");
  }
}

class BusDriverFactory extends DriverFactory {
  @Override
  protected Driver createDriver() {
    return new BusDriver();
  }

}

class BusDriver implements Driver {
  @Override
  public void setCondition(float percent) {
    System.out.println("BusDriver's condition " + percent + "%");
  }

  @Override
  public void drive() {
    System.out.println("BusDriver is driving");
  }
}


interface Super {
}

class Subject implements Super {
  Integer a;

  public static Subject create() { // Factory Method 일반형
    return new Subject();
  }

  public void init() {
  }

  private Subject() {
  }

  public static Subject create1() { // 생성 후 초기화
    Subject ret = new Subject();
    ret.init();
    return ret;
  }

  public static synchronized Subject create2() { // 생성 후 동기화
    Subject ret = new Subject();
    return ret;
  }

  public static Super create3() { // 생성후 타입 변환
    return new Subject();
  }

  private static Subject instance = null;

  public static Subject create4() { // 생성 관리 (ex : Singleton)
    if (instance == null) {
      instance = new Subject();
    }

    return instance;
  }
}