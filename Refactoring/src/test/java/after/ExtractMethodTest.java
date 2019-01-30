package after;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class ExtractMethodTest {

  @BeforeEach
  void setUp() {
  }

  @AfterEach
  void tearDown() {
  }


  /**
   * Expected result
   * <p>
   * **************************
   * ***** Customer Owes ******
   * **************************
   * name:John
   * amount: 1600.0
   */
  @Test
  void testExtractMethod() {
    Customer customer = new Customer("John");
    Order order = new Order(1000);
    customer.addOrder(order);
    customer.printOrders(500);
  }
}