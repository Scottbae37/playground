/**
 *
 * Intent
 *  - creates objects without exposing the instantiation logic to the client.
 *  - refers to the newly created object through a common interface
 *
 */
public class AbstractFactoryPattern {
  public static void main(String[] agrs) {
    AbstractFactoryPattern pattern = new AbstractFactoryPattern();
    Button button = null;
    Dialog dialog = null;

    Factory f = new MacFactory();
    pattern.makeAndDraw(button, dialog, f);

    f = new WinFactory();
    pattern.makeAndDraw(button, dialog, f);

    f = EnumStyleFactory.MAC;
    pattern.makeAndDraw(button, dialog, f);

    f = EnumStyleFactory.WIN;
    pattern.makeAndDraw(button, dialog, f);
  }

  private void makeAndDraw(Button btn, Dialog dlg, Factory factory) {
    btn = factory.newButton();
    dlg = factory.newDialog();
    btn.onDraw();
    dlg.onDraw();
  }
}

enum EnumStyleFactory implements Factory {
  MAC {
    @Override
    public Button newButton() {
      System.out.println("[Enum Mac] new Button!!");
      return new MacButton();
    }

    @Override
    public Dialog newDialog() {
      System.out.println("[Enum Mac] new Dialog!!");
      return new MacDialog();
    }
  },
  WIN {
    @Override
    public Button newButton() {
      System.out.println("[Enum WIN] new Button!!");
      return new WinButton();
    }

    @Override
    public Dialog newDialog() {
      System.out.println("[Enum WIN] new Dialog!!");
      return new WinDialog();
    }
  }
}

class MacFactory implements Factory {
  @Override
  public Button newButton() {
    System.out.println("[Mac style] new Button");
    return new MacButton();
  }

  @Override
  public Dialog newDialog() {
    System.out.println("[Mac style] new Dialog");
    return new MacDialog();
  }
}

class WinFactory implements Factory {
  @Override
  public Button newButton() {
    System.out.println("[Windows style] new Button");
    return new WinButton();
  }

  @Override
  public Dialog newDialog() {
    System.out.println("[Windows style] new Dialog");
    return new WinDialog();
  }
}

interface Factory {
  Button newButton();

  Dialog newDialog();
}

interface Button {
  void onDraw();
}

interface Dialog {
  void onDraw();
}

class MacButton implements Button {
  @Override
  public void onDraw() {
    System.out.println("[Mac style] Drawing button..");
  }
}

class MacDialog implements Dialog {
  @Override
  public void onDraw() {
    System.out.println("[Mac style] Drawing dialog..");
  }
}

class WinButton implements Button {
  @Override
  public void onDraw() {
    System.out.println("[Windows style] Drawing button..");
  }
}

class WinDialog implements Dialog {
  @Override
  public void onDraw() {
    System.out.println("[Windows style] Drawing dialog..");
  }
}