package after;

public class ReplaceTempWithQuery {
  private int quantity;
  private int itemPrice;

  public ReplaceTempWithQuery(int quantity, int itemPrice) {
    this.quantity = quantity;
    this.itemPrice = itemPrice;
  }

  double getPrice() {
    return basePrice() * discountFactor();
  }

  private int basePrice() {
    return quantity * itemPrice;
  }

  private double discountFactor() {
    if (basePrice() > 1000)
      return 0.95;
    else
      return 0.98;
  }
}

