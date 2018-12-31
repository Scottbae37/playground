package solution;

import com.google.common.collect.ImmutableList;
import org.junit.Test;

import static junit.framework.TestCase.assertEquals;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class PrimeFactorsTest {
  @Test
  public void of_1_is_none() {
    assertThat(PrimeFactors.of(1), is(ImmutableList.of()));
  }

  @Test
  public void of_2_is_2() {
    assertThat(PrimeFactors.of(2), is(ImmutableList.of(2)));
  }

  @Test
  public void of_3_is_3() {
    assertThat(PrimeFactors.of(3), is(ImmutableList.of(3)));
  }

  @Test
  public void of_4_is_4() {
    assertThat(PrimeFactors.of(4), is(ImmutableList.of(2, 2)));
  }

  @Test
  public void of_6_is_2_3() {
    assertThat(PrimeFactors.of(6), is(ImmutableList.of(2, 3)));
  }

  @Test
  public void of_8_is_2_2_2() {
    assertThat(PrimeFactors.of(8), is(ImmutableList.of(2, 2, 2)));
  }

  @Test
  public void of_9_is_3_3() {
    assertThat(PrimeFactors.of(9), is(ImmutableList.of(3, 3)));
  }

  @Test
  public void acceptanceTest() {
    assertThat(PrimeFactors.of(2 * 3 * 5 * 7 * 7 * 3 * 2 * 3 * 7 * 11), is(ImmutableList.of(2, 2, 3, 3, 3, 5, 7, 7, 7, 11)));
  }
}
