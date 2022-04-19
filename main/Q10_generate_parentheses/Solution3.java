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

    public static List<String> generateParentheses(int n) {
        Map<Integer,List<String>> solutions = new HashMap<Integer,List<String>>();
        solutions.put(0, Arrays.asList(""));

        for(int k = 1; k <= n; k++){
            List<String> list = new ArrayList<String>();
            for(int i = 0; i < k; i++){
                for(String left : solutions.get(i)){
                    for(String inside : solutions.get(k-i-1)){
                        list.add(left + "(" + inside + ")");
                    }
                }
            }

            solutions.put(k, list);
        }

        return solutions.get(n);
    }
}
