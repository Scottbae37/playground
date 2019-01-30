package before;

public class IntroduceExplainingVariable {
  static class Price {
    int quantity, itemPrice;

    public Price(int quantity, int itemPrice) {
      this.quantity = quantity;
      this.itemPrice = itemPrice;
    }

    double price() {
      // price is base price - quantity discount + shipping
      return quantity * itemPrice -
              Math.max(0, quantity - 500) * itemPrice * 0.05 +
              Math.min(quantity * itemPrice * 0.1, 100.0);
    }
  }
}
