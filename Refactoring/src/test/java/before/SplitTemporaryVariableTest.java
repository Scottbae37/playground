package before;

import org.junit.jupiter.api.Test;

import static before.SplitTemporaryVariable.*;
import static org.junit.jupiter.api.Assertions.*;

class SplitTemporaryVariableTest {
  @Test
  void testSplitTemporaryVariable() {
    double expected = 2.5;
    Distance dist = new Distance();

    double actual = dist.getDistanceTravelled(2);

    assertEquals(expected, actual);
  }
}