package Q10_generate_parentheses;
import java.util.*;

public class Tester {
    public static void main(String[] args) {
        List<String> list = Solution1.generateParentheses(2);
        System.out.println(Arrays.toString(list.toArray()));
    }
}
