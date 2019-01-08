package solution;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class NameInverterTest {
  @Test
  @DisplayName("invert null should return exception")
  void tc01() {
    assertThrows(NullPointerException.class, () -> NameInverter.invert(null));
  }

  @Test
  @DisplayName("invert empty string should return empty string")
  void tc02() {
    assertThat(NameInverter.invert(""), is(""));
    assertThat(NameInverter.invert("   "), is(""));
  }

  @Test
  @DisplayName("invert_first_name_should_return_first_name")
  void tc03() {
    assertThat(NameInverter.invert("John"), is("John"));
    assertThat(NameInverter.invert("  John   "), is("John"));
  }

  @Test
  void invert_first_last_name_should_return_last_first() {
    assertThat(NameInverter.invert("John Smith"), is("Smith, John"));
  }

  @DisplayName("should invert \"HonorificsMr. FirstName LastName\" to \"LastName, FirstName\"")
  @Test
  void invert_honorifics_first_last_should_return_last_comma_first() {
    assertThat(NameInverter.invert("Mr. John Smith"), is("Smith, John"));
    assertThat(NameInverter.invert("Mrs. John Smith"), is("Smith, John"));
  }

  @DisplayName("should invert \"John Smith Sr.\" to \"Smith, John Sr.\"")
  @Test
  public void invert_postnominals() {
    assertThat(NameInverter.invert("John Smith Sr."), is("Smith, John Sr."));
    assertThat(NameInverter.invert("John Smith Sr. PhD."), is("Smith, John Sr. PhD."));
  }

  @DisplayName("Acceptance test \"Mr. John Smith Sr. PhD.\" to \"Smith, John Sr. PhD.\"")
  @Test
  void acceptance_test() {
    assertThat(NameInverter.invert("Mr. John Smith Sr. PhD."), is("Smith, John Sr. PhD."));
  }
}
