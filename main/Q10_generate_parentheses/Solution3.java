package Q10_generate_parentheses;

import java.util.*;

public class Solution3 {
    public static List<String> generateParentheses(int n) {
        List<String> list = new ArrayList<String>();

        if(n == 0){
            list.add("");
        }

        for(int k = 0; k < n; k++){
            for(String left : generateParentheses(k)){
                for(String inside : generateParentheses(n-k-1)){
                    list.add(left + "(" + inside + ")");
                }
            }
        }

        return list;
    }
}
