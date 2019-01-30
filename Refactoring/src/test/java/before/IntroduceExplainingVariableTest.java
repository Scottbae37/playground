package before;

import org.junit.jupiter.api.Test;

import static before.IntroduceExplainingVariable.*;
import static org.junit.jupiter.api.Assertions.*;

class IntroduceExplainingVariableTest {
  @Test
  void testIntroduceExplainingVariable() {
    final double expected = 2100.0;
    Price car = new Price(2, 1000);

    double actual = car.price();

    assertEquals(expected, actual);
  }
}