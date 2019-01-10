import com.google.common.collect.Lists;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.times;

class ObserverPatternTest {

  @BeforeEach
  void setUp() {
  }

  @AfterEach
  void tearDown() {
  }

  @Test
  void testObserverPattern() {
    Publisher publisher = new Publisher();
    Subscriber a = new Subscriber("A");
    Subscriber b = new Subscriber("B");
    Subscribe mock = Mockito.mock(Subscribe.class);

    publisher.addSub(a);
    publisher.addSub(b);
    publisher.addSub(mock);

    publisher.publish(2);
    publisher.publish(2);

    Mockito.verify(mock, times(2)).update(2);
  }
}

interface Subscribe {
  void update(int number);
}

class Subscriber implements Subscribe {
  private String name;

  public Subscriber(String name) {
    this.name = name;
  }

  @Override
  public void update(int number) {
    System.out.println(toString() + " rx: " + number);
  }

  @Override
  public String toString() {
    return "Subscriber{" +
            "name='" + name + '\'' +
            '}';
  }
}

class Publisher {
  private List<Subscribe> list = Lists.newArrayList();

  public void addSub(Subscribe subscribe) {
    list.add(subscribe);
  }

  public boolean removeSub(Subscribe subscribe) {
    return list.remove(subscribe);
  }

  public void publish(int number) {
    for (Subscribe each : list)
      each.update(number);
  }
}