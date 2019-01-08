package solution;

import com.google.common.collect.Lists;

import java.util.ArrayList;
import java.util.List;

public class NameInverter {

  public static String invert(String name) {
    List<String> nameParts = breakingIntoPartsIgnoringWhitespace(name);

    if (nameParts.size() < 2)
      return nameParts.get(0);

    return invert(withoutHonorifics(nameParts));
  }

  private static ArrayList<String> breakingIntoPartsIgnoringWhitespace(String name) {
    return Lists.newArrayList(name.trim().split(RegularExpressions.ANY_SPACES));
  }

  private static List<String> withoutHonorifics(List<String> nameParts) {
    String s = nameParts.get(0);

    if (Honorifics.isHonorific(s))
      nameParts.remove(0);

    return nameParts;
  }

  private static String invert(List<String> nameParts) {
    String first = nameParts.get(0);
    String last = nameParts.get(1);
    String postnominals = "";
    postnominals = findAndMergePostnominals(nameParts);

    return String.format("%s, %s %s", last, first, postnominals).trim();
  }

  private static String findAndMergePostnominals(List<String> nameParts) {
    String postnominals = "";

    for (String each : nameParts.subList(2, nameParts.size()))
      postnominals += each + " ";

    return postnominals;
  }
}

class RegularExpressions {
  public static final String ANY_SPACES = "\\s+";
}

class Honorifics {
  private static final List<String> KNOWN_HONORIFICS = Lists.newArrayList("Mr.", "Mrs.");

  public static boolean isHonorific(String s) {
    return KNOWN_HONORIFICS.contains(s);
  }
}
