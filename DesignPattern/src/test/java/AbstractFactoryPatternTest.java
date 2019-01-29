import org.hamcrest.Matcher;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;

class AbstractFactoryPatternTest {

  @BeforeEach
  void setUp() {
  }

  @AfterEach
  void tearDown() {
  }

  @Test
  void testFactoryPattern() {
    MouseKeyboardFactory factory;
    MouseKeyboardFactory.Mouse mouse;
    MouseKeyboardFactory.Keyboard keyboard;

    factory = EnumFactory.MAC;
    mouse = factory.makeMouse();
    keyboard = factory.makeKeyboard();

    mouse.click();
    mouse.contextClick();
    keyboard.copy();
    keyboard.paste();

    factory = EnumFactory.WIN;
    mouse = factory.makeMouse();
    keyboard = factory.makeKeyboard();

    mouse.click();
    mouse.contextClick();
    keyboard.copy();
    keyboard.paste();

    assertThat(EnumFactory.MAC, is(EnumFactory.MAC));
    assertThat(EnumFactory.WIN, is(EnumFactory.WIN));
    assertThat(EnumFactory.MAC.makeMouse(), Matchers.not(EnumFactory.MAC.makeMouse()));
  }
}

interface MouseKeyboardFactory {
  Mouse makeMouse();

  Keyboard makeKeyboard();

  interface Mouse {
    void click();

    void contextClick();
  }

  interface Keyboard {
    void copy();

    void paste();
  }
}

enum EnumFactory implements MouseKeyboardFactory {
  MAC {
    @Override
    public Mouse makeMouse() {
      return new MagicMouse();
    }

    @Override
    public Keyboard makeKeyboard() {
      return new MagicKeyboard();
    }
  },
  WIN {
    @Override
    public Mouse makeMouse() {
      return new NormalMouse();
    }

    @Override
    public Keyboard makeKeyboard() {
      return new NormalKeyboard();
    }
  }
}

class NormalKeyboard implements MouseKeyboardFactory.Keyboard {
  @Override
  public void copy() {
    System.out.println("[Normal Keyboard] Ctrl + c");
  }

  @Override
  public void paste() {
    System.out.println("[Normal Keyboard] Ctrl + v");
  }
}

class NormalMouse implements MouseKeyboardFactory.Mouse {
  @Override
  public void click() {
    System.out.println("[Normal Mouse] Left click");
  }

  @Override
  public void contextClick() {
    System.out.println("[Normal Mouse] Right click");
  }
}

class MagicMouse implements MouseKeyboardFactory.Mouse {
  @Override
  public void click() {
    System.out.println("[Magic Mouse] Touch with one finger");
  }

  @Override
  public void contextClick() {
    System.out.println("[Magic Mouse] Touch with two fingers");
  }
}

class MagicKeyboard implements MouseKeyboardFactory.Keyboard {
  @Override
  public void copy() {
    System.out.println("[Magic Keyboard] Command + c");
  }

  @Override
  public void paste() {
    System.out.println("[Magic Keyboard] Command + v");
  }
}












