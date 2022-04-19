package Q10_generate_parentheses;

import java.util.*;

public class Solution1B {
    public static List<String> generateParentheses(int n) {
        List<String> list = new ArrayList<String>();
        generateAll(list, new char[2*n], 0);
        return list;
    }

    public static void generateAll(List<String> list, char[] chars, int index) {
        if (index == chars.length) {
            String s = new String(chars);
            if (isValid(s)) {
                list.add(new String(chars));
            }
            return;
        }

        chars[index] = '(';
        generateAll(list, chars, index+1);
        chars[index] = ')';
        generateAll(list, chars, index + 1);
    }

    public static boolean isValid(String str) {
        int open = 0;
        for (int k = 0; k < str.length(); k++) {
            if (str.charAt(k) == '(') {
                open++;
            } else {
                open--;
            }
            if (open < 0) {
                return false;
            }
        }
        if (open != 0) {
            return false;
        }
        return true;
    }
}
