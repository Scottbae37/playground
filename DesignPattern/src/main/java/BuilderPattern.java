public class BuilderPattern {
  public static void main(String[] args) {
    TeleScope objA = TeleScope.newBuilder()
        .setCode(1).setEtc("Etc1").setInch(10.11).setMadeInCode(111)
        .setName("A").setType(11).setSize(11).setSerialNum(111)
        .build();
    TeleScope objB = TeleScope.newBuilder()
        .setCode(2).setEtc("Etc2").setInch(22.22).setMadeInCode(222)
        .setName("B").setType(22).setSize(2).setSerialNum(2222)
        .build();

    System.out.println("Object A " + objA.toString());
    System.out.println("Object B " + objB.toString());
  }
}

class TeleScope {
  private final String name;
  private final int type;
  private final int madeInCode;
  private final int code;
  private final int serialNum;
  private final float size;
  private final double inch;
  private final String etc;

  private TeleScope(Builder builder) {
    this.name = builder.name;
    this.type = builder.type;
    this.madeInCode = builder.madeInCode;
    this.code = builder.code;
    this.serialNum = builder.serialNum;
    this.size = builder.size;
    this.inch = builder.inch;
    this.etc = builder.etc;
  }

  @Override
  public String toString() {
    return "TeleScope{" +
        "name='" + name + '\'' +
        ", type=" + type +
        ", madeInCode=" + madeInCode +
        ", code=" + code +
        ", serialNum=" + serialNum +
        ", size=" + size +
        ", inch=" + inch +
        ", etc='" + etc + '\'' +
        '}';
  }

  static Builder newBuilder() {
    return new Builder();
  }

  static class Builder {
    private String name = "";
    private int type;
    private int madeInCode;
    private int code;
    private int serialNum;
    private float size;
    private double inch;
    private String etc = "";

    TeleScope build() {
      return new TeleScope(this);
    }

    Builder setName(String name) {
      this.name = name;
      return this;
    }

    Builder setType(int type) {
      this.type = type;
      return this;
    }

    Builder setMadeInCode(int madeInCode) {
      this.madeInCode = madeInCode;
      return this;
    }

    Builder setCode(int code) {
      this.code = code;
      return this;
    }

    Builder setSerialNum(int serialNum) {
      this.serialNum = serialNum;
      return this;
    }

    Builder setSize(float size) {
      this.size = size;
      return this;
    }

    Builder setInch(double inch) {
      this.inch = inch;
      return this;
    }

    Builder setEtc(String etc) {
      this.etc = etc;
      return this;
    }
  }
}
