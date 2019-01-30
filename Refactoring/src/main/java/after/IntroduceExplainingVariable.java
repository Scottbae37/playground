package after;

public class IntroduceExplainingVariable {
  static class Price {
    int quantity, itemPrice;

    public Price(int quantity, int itemPrice) {
      this.quantity = quantity;
      this.itemPrice = itemPrice;
    }

    /**
     * IntroduceExplainingVariable
     */
    double price() {
      // price is base price - quantity discount + shipping
      final int basePrice = quantity * itemPrice;
      final double quantityDiscount = Math.max(0, quantity - 500) * itemPrice * 0.05;
      final double shipping = Math.min(basePrice * 0.1, 100.0);
      return basePrice - quantityDiscount + shipping;
    }

    /**
     * ExtractMethod
     */
    double priceExtractMethod() {
      // price is base price - quantity discount + shipping
      return basePrice() - quantityDiscount() + shipping();
    }

    private double shipping() {
      return Math.min(basePrice() * 0.1, 100.0);
    }

    private double quantityDiscount() {
      return Math.max(0, quantity - 500) * itemPrice * 0.05;
    }

    private int basePrice() {
      return quantity * itemPrice;
    }
  }
}
