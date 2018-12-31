package solution;

public class FizzBuzz {

    private static final String FIZZ_STR = "Fizz";
    private static final String BUZZ_STR = "Buzz";

    public String of(int num) {
        if (num <= 0)
            return "0";

        return _of(num);
    }

    private String _of(int num) {
        String retStr = "";
        if (num % 3 == 0)
            retStr += FIZZ_STR;
        if (num % 5 == 0)
            retStr += BUZZ_STR;
        return retStr.isEmpty() ? String.valueOf(num) : retStr;
    }
}
