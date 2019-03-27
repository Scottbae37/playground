import org.junit.jupiter.api.Test;


import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class CompositeTest {
  /**
   * 8. Composite
   * 부분-전체에 계층을 나타내기 위해 복합 객체를 트리 구조로 만든다.
   * Composite 패턴은 클라이언트가 개별적 객체와 복합 객체 모두를 동일하게 다루도록 한다.
   * <p>
   * - 복합 객체와  단일 객체를 동일시 함으로써 소프트웨어 구조를 단순화 시킨다.
   * - 재귀적 호출을 통해 복잡한 구현을 단순화 한다.
   */

  @Test
  void compositePattern() {
    ClientSearch searchClient = new ClientSearch();
    File file = new File("./src");
    ComponentItem item = searchClient.search(file);

    System.out.println("files = " + item.getFiles());

    System.out.println("lines = " + item.getLines());
  }
}

class ClientSearch {
  public ComponentItem search(File file) {
    CompositeDirectoryItem item = new CompositeDirectoryItem();

    File[] files = file.listFiles();
    for (File each : files) {
      if (each.isDirectory()) {
        item.add(search(each)); // File의 타입이 디렉토리인 경우 search() 메소드를 재귀적으로 호출한다.
      } else {
        if (each.getAbsolutePath().endsWith(".java")) {
          System.out.println(each.getAbsolutePath());
          item.add(new LeafFileItem(each));
        }
      }

    }
    return item;
  }
}

// 복합 객체와 단말 객체가 같은 방식으로 다뤄지도록 인터페이스를 선언한다.
interface ComponentItem {
  int getFiles();

  int getLines();
}

// Composite 객체(복합객체)
class CompositeDirectoryItem implements ComponentItem {
  private List<ComponentItem> kids = new ArrayList<>();

  public void add(ComponentItem kid) {
    kids.add(kid);
  }

  @Override
  public int getFiles() { // 복합 객체는 모든 일을 자식 Item들에게 시켜서 계산한다.
    int ret = 0;
    for (ComponentItem each : kids)
      ret += each.getFiles();
    return ret;
  }

  @Override
  public int getLines() {
    int ret = 0;
    for (ComponentItem each : kids)
      ret += each.getLines();
    return ret;
  }
}

// Leaf 객체(단말 객체)
class LeafFileItem implements ComponentItem {
  private File file;

  public LeafFileItem(File file) {
    this.file = file;
  }

  @Override
  public int getFiles() {
    return 1;
  }

  @Override
  public int getLines() {
    int lineCnt = 0;
    try {
      Scanner scan = new Scanner(file);
      while (scan.hasNextLine()) {
        String line = scan.nextLine().trim();
        if (!line.equals(""))
          lineCnt++;
      }
      return lineCnt;
    } catch (FileNotFoundException e) {
      e.printStackTrace();
      return lineCnt;
    }
  }
}
