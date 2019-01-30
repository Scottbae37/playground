package before;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;

class ReplaceTempWithQueryTest {

  @BeforeEach
  void setUp() {
  }

  @Test
  void getPrice() {
    ReplaceTempWithQuery cut = new ReplaceTempWithQuery(5, 500);

    assertThat(cut.getPrice(), is(2375.0));
  }
}