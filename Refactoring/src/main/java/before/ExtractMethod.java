package before;

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

  // TODO:
  public void printOrders(int previousAmount) {
    Iterator<Order> it = orders.iterator();
    double outstanding = previousAmount * 1.2;

    // print banner
    System.out.println("**************************");
    System.out.println("***** Customer Owes ******");
    System.out.println("**************************");

    // calculate outstanding
    while (it.hasNext()) {
      Order each = it.next();
      outstanding += each.getAmount();
    }

    // print details
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
