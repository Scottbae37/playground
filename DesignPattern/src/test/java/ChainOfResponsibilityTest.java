import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ChainOfResponsibilityTest {
  /**
   * ### Chain of Responsibility (책임의 연쇄, 책임의 사슬)
   * <p>
   * #### 특징
   * 요청을 처리할 수 있는 기회를 하나 이상의 객체에게 부여함으로써 요청하는 객체와 처리하는 객체 사이의 결합도를 없애려는 것이다. 요청을 해결할 객체를 만날 때까지 객체 고리를 따라서 요청을 전달한다.
   * 요청의 처리 과정을 추상화하여 요청을 단순화한다.
   * 요청의 처리 과정을 다양한 구조로 변경할 수 있도록 한다.
   * <p>
   * <p>
   * #### 장점
   * Sender 와 Receiver 을 de-coupling 할 수 있음.
   * Sender 입장에서는 어떤 Receiver 가 처리하든지 상관 없이
   * <p>
   * <p>
   * #### 예)
   * 현실에서의 병원(작은 병원 -> 종합병원, 대학병원)
   * Client Object가 보내는 요청을 처리할 Handler를 chaining 하고, 본인이 해결하지 못하는 request에 대해서 본인이 처리하고 못하는 부분은 다음 Handler에게 넘김, Java에서 Exception Handling과 비슷함
   * ```
   * Req        Req         Req         Req
   * \       /   \       /   \       /   \
   * Handler     Handler     Handler     Handler
   * ```
   * <p>
   * #### 발생 가능한 문제점:
   * 2번째 Filter가 본인이 처리 하지 못하는 요청임에도 불구하고, 다음 Filter에게 전달하는 것을 누락했을 때 문제가 될 수 있음.
   * ```
   * Req       Req                   Req(X)
   * \      /   \      /   \      /   \
   * Filter     Filter     Filter     Filter
   * ```
   * <p>
   * #### 해결 방법:
   * 아래 알고리즘 적용 (강제화 하기 위해서 Template Pattern을 적용 가능 )
   * 1. Check if rule matches
   * 2. If it matches, do something specific
   * 3. If it doesn't match, call the next filter in the list
   */


  @Test
  void test() {
    Filter f = new HighFilter(new NullObjFilter(), 200, 300);
    f = new MidFilter(f, 100, 200);
    f = new NormalFilter(f, 0, 100);
    /// Normal -> Mid -> High
    String result = "";

    int value = 99;
    result = f.filter(value);
    assertEquals("NormalFilter.filter", result);
    System.out.println(value + "-" + result);

    value = 100;
    result = f.filter(value);
    assertEquals("MidFilter.filter", result);
    System.out.println(value + "-" + result);

    value = 200;
    result = f.filter(value);
    assertEquals("HighFilter.filter", result);
    System.out.println(value + "-" + result);

    value = 300;
    result = f.filter(value);
    assertEquals("No", result);
    System.out.println(value + "-" + result);
  }
}

interface Filter {
  boolean canHandle(int value);

  String filter(int value);
}

class NormalFilter implements Filter {
  private Filter rule;
  private int lowerClosed, upperOpen;

  public NormalFilter(Filter rule, int lowerClosed, int upperOpen) {
    this.rule = rule;
    this.lowerClosed = lowerClosed;
    this.upperOpen = upperOpen;
  }

  @Override
  public boolean canHandle(int value) {
    return lowerClosed <= value && value < upperOpen;
  }

  @Override
  public String filter(int val) {
    if (canHandle(val))
      return "NormalFilter.filter";
    return rule.filter(val);
  }
}

class MidFilter implements Filter {
  private Filter rule;
  private int lowerClosed, upperOpen;

  public MidFilter(Filter rule, int lowerClosed, int upperOpen) {
    this.rule = rule;
    this.lowerClosed = lowerClosed;
    this.upperOpen = upperOpen;
  }

  @Override
  public boolean canHandle(int value) {
    return lowerClosed <= value && value < upperOpen;
  }

  @Override
  public String filter(int value) {
    if (canHandle(value))
      return "MidFilter.filter";
    return rule.filter(value);
  }
}

class HighFilter implements Filter {
  private Filter rule;
  private int lowerClosed, upperOpen;

  public HighFilter(Filter rule, int lowerClosed, int upperOpen) {
    this.rule = rule;
    this.lowerClosed = lowerClosed;
    this.upperOpen = upperOpen;
  }

  @Override
  public boolean canHandle(int value) {
    return lowerClosed <= value && value < upperOpen;
  }

  @Override
  public String filter(int value) {
    if (canHandle(value))
      return "HighFilter.filter";

    return rule.filter(value);
  }
}

class NullObjFilter implements Filter {
  @Override
  public boolean canHandle(int value) {
    return false;
  }

  @Override
  public String filter(int value) {
    return "No";
  }
}