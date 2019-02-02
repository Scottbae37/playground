package money;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class MoneyTest {

  /**
   * TODO:
   * $5 + 10CHF = $10(환율이 2:1일 경우)
   * ---- $5 * 2 = $10
   * ---- amount를 private으로 만들기
   * ---- Dollar 부작용(side effect)?
   * Money 반올림?
   * ---- equals()
   * hashCode()
   */

  @Test
  void testMultiplication() {
    Dollar five = new Dollar(5);
    assertEquals(new Dollar(10), five.times(2));
    assertEquals(new Dollar(15), five.times(3));
  }

  @Test
  void testEquality() {
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(5).equals(new Dollar(6)));
  }

  private class Dollar {
    private int amount;

    public Dollar(int amount) {
      this.amount = amount;
    }

    public Dollar times(int added) {
      return new Dollar(amount * added);
    }

    @Override
    public boolean equals(Object obj) {
      Dollar dollar = (Dollar) obj;
      return this.amount == dollar.amount;
    }
  }
}
