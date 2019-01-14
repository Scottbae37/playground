import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BuilderPatternTest {

  @BeforeEach
  void setUp() {
  }

  @AfterEach
  void tearDown() {
  }

  @Test
  void testBuilderPattern() {
    String aName = "A";
    int aType = 11;
    int aMadeInCode = 111;
    int aCode = 1;
    int aSerialNum = 111;
    float aSize = 11.0f;
    double aInch = 10.11;
    String aEtc = "Etc1";
    String expectedA = "TeleScope{name='" + aName + "', type=" + aType + ", madeInCode=" + aMadeInCode + ", code=" + aCode + ", serialNum=" + aSerialNum + ", size=" + aSize + ", inch=" + aInch + ", etc='" + aEtc + "'}";
    String expectedB = "TeleScope{name='B', type=22, madeInCode=222, code=2, serialNum=2222, size=2.0, inch=22.22, etc='Etc2'}";

    TeleScope objA = TeleScope.newBuilder()
        .setName(aName)
        .setType(aType)
        .setMadeInCode(aMadeInCode)
        .setCode(aCode)
        .setSerialNum(aSerialNum)
        .setSize(aSize)
        .setInch(aInch)
        .setEtc(aEtc)
        .build();
    assertEquals(expectedA, objA.toString());
  }
}