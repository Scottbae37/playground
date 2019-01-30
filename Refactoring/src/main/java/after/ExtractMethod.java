package after;

import java.util.*;

public class ExtractMethod {
}

class Customer {
  private final String name;
  private List<Order> orders;

  public Customer(String name) {
    this.name = name;
    orders = new ArrayList<>();
  }

  public void addOrder(Order order) {
    orders.add(order);
  }

  public List<Order> getOrders() {
    return orders;
  }

  public void printOrders(int previousAmount) {
    printBanner();
    double outstanding = calcOutstanding(previousAmount);
    printDetail(outstanding);
  }

  private void printBanner() {
    System.out.println("**************************");
    System.out.println("***** Customer Owes ******");
    System.out.println("**************************");
  }

  private double calcOutstanding(int previousAmount) {
    Iterator<Order> it = orders.iterator();
    double outstanding = previousAmount * 1.2;
    while (it.hasNext()) {
      Order each = it.next();
      outstanding += each.getAmount();
    }
    return outstanding;
  }

  private void printDetail(double outstanding) {
    System.out.println("name:" + name);
    System.out.println("amount: " + outstanding);
  }
}

class Order {
  private int amount;

  Order(int amount) {
    this.amount = amount;
  }

  int getAmount() {
    return amount;
  }
}
