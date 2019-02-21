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
   * Equal null
   * Equal obejct
   * ---- 5CHF * 2 = 10CHF
   * ---- 공용 equals
   * 공용 times
   * ---- Franc과 Dollar 비교하기
   * ---- 통화? (this.getClass().equals(money.getClass()))
   * testFrancMultiplication 지워야 하나?
   */

  @Test
  void testMultiplication() {
    Money five = Money.dollar(5);
    assertEquals(Money.dollar(10), five.times(2));
    assertEquals(Money.dollar(15), five.times(3));
  }

  @Test
  void testEquality() {
    assertTrue(Money.dollar(5).equals(Money.dollar(5)));
    assertFalse(Money.dollar(5).equals(Money.dollar(6)));
    assertTrue(Money.franc(5).equals(Money.franc(5)));
    assertFalse(Money.franc(5).equals(Money.franc(6)));
    assertFalse(Money.franc(5).equals(Money.dollar(5)));
  }

  @Test
  void testFrancMultiplication() {
    Money five = Money.franc(5);
    assertEquals(Money.franc(10), five.times(2));
    assertEquals(Money.franc(15), five.times(3));
  }

  @Test
  void testCurrency() {
    assertEquals("USD", Money.dollar(1).currency());
    assertEquals("CHF", Money.franc(1).currency());
  }
}

abstract class Money {
  int amount;
  private String currency;

  public Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;
  }

  static Money dollar(int amount) {
    return new Dollar(amount, "USD");
  }

  public static Money franc(int amount) {
    return new Franc(amount, "CHF");
  }

  @Override
  public boolean equals(Object obj) {
    Money money = (Money) obj;
    return amount == money.amount && this.getClass().equals(money.getClass());
  }

  abstract Money times(int multiplier);

  String currency() {
    return currency;
  }
}

class Dollar extends Money {
  Dollar(int amount, String currency) {
    super(amount, currency);
  }

  Money times(int multiplier) {
    return Money.dollar(amount * multiplier);
  }
}

class Franc extends Money {
  Franc(int amount, String currency) {
    super(amount, currency);
  }

  Money times(int multiplier) {
    return Money.franc(amount * multiplier);
  }
}
