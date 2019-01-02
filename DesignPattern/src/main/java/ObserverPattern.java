import com.google.common.collect.Lists;

import java.util.List;

interface Subscriable {
  void update(int num);
}

class Subscriber implements Subscriable {
  private final String name;

  public Subscriber(String name) {
    this.name = name;
  }

  @Override
  public void update(int num) {
    System.out.println("\t" + name + " gets " + num);
  }
}

class Publisher {
  private List<Subscriable> subscriberList = Lists.newCopyOnWriteArrayList();

  public void addSubscriber(Subscriber sub) {
    subscriberList.add(sub);
  }

  public boolean delSubscriber(Subscriber sub) {
    return subscriberList.remove(sub);
  }

  public void publishNumber(int num) {
    for (Subscriable each : subscriberList) {
      each.update(num);
    }
  }
}

public class ObserverPattern {
  public static void main(String[] args) {
    Publisher publisher = new Publisher();
    Subscriber a = new Subscriber("A");
    Subscriber b = new Subscriber("B");

    System.out.println("1) A, B subscribers added");
    publisher.addSubscriber(a);
    publisher.addSubscriber(b);
    System.out.println("2) Publisher published 4, 5");
    publisher.publishNumber(4);
    publisher.publishNumber(5);

    Subscriber c = new Subscriber("C");
    System.out.println("3) B is removed and C is added");
    publisher.delSubscriber(b);
    publisher.addSubscriber(c);
    System.out.println("4) Publisher published 1, 3");
    publisher.publishNumber(1);
    publisher.publishNumber(3);
  }
}
