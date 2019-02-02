package money;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MoneyTest {

  /**
   * TODO:
   * $5 + 10CHF = $10(환율이 2:1일 경우)
   * $5 * 2 = $10
   * amount를 private으로 만들기
   * Dollar 부작용(side effect)?
   * Money 반올림?
   */

  @Test
  void testMultiplication() {
    Dollar five = new Dollar(5);
    five.times(2);
    assertEquals(10, five.amount);
  }

  private class Dollar {
    public int amount = 5 * 2; //코드의 데이터와 테스트 데이터 사이의 중복

    public Dollar(int amount) {
    }

    public void times(int added) {

    }
  }
}
