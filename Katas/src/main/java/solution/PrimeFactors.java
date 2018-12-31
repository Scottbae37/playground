package solution;

import com.google.common.collect.Lists;

import java.util.List;

public class PrimeFactors {
  public static List<Integer> of(int num) {
    List<Integer> factors = Lists.newArrayList();

    for (int divisor = 2; num > 1; divisor++) {
      for (; num % divisor == 0; num /= divisor) {
        factors.add(divisor);
      }
    }
    return factors;
  }

}
