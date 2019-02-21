package practice;

import com.google.common.collect.ImmutableList;
import com.google.common.collect.Lists;
import jdk.nashorn.internal.ir.annotations.Immutable;
import org.junit.Test;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;
import static org.junit.jupiter.api.Assertions.*;

public class PrimeFactorsTest {

  @BeforeEach
  void setUp() {
    System.out.println("SETUP");
  }

  @AfterEach
  void tearDown() {
    System.out.println("tearDown");
  }

}