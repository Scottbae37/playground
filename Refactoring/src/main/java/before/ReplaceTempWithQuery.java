package before;

public class ReplaceTempWithQuery {
  private int quantity;
  private int itemPrice;

  public ReplaceTempWithQuery(int quantity, int itemPrice) {
    this.quantity = quantity;
    this.itemPrice = itemPrice;
  }

  double getPrice() {
    int basePrice = quantity * itemPrice;
    double discountFactor;
    if (basePrice > 1000) discountFactor = 0.95;
    else discountFactor = 0.98;
    return basePrice * discountFactor;
  }
}

