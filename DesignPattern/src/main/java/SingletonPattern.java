import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class SingletonPattern {
  private static SingletonPattern ourInstance = new SingletonPattern();

  public static SingletonPattern getInstance() {
    return ourInstance;
  }

  private SingletonPattern() {
  }

  public static void main(String[] args) {
    ExecutorService executorService = Executors.newFixedThreadPool(4);
    for (int i = 0; i < 100; i++) {
      executorService.execute(() -> {
        while (true) DynamicSingleton.getInstance();
      });
    }
  }
}

class DynamicSingleton {
  private static volatile DynamicSingleton instance = null;

  private DynamicSingleton() {
  }

  public static DynamicSingleton getInstance() {

    // Double Checked Locking
    if (instance == null) {
      synchronized (DynamicSingleton.class) {
        if (instance == null) {
          System.out.println("New Dynamic Singlenton");
          instance = new DynamicSingleton();
        }
      }
    }
    return instance;
  }
}


