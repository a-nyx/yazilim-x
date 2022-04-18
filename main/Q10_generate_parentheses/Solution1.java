import java.util.*;

public class Solution1 {
    public List<String> generateParentheses(int n) {
        List<String> answers = new ArrayList<String>();

        generateAll(answers, n);
        deleteInvalid(answers);

        return answers;
    }

    public void generateAll(List<String> arr, int n) {
        int amount = (int) Math.pow(2, 2 * n);
        for (int i = 0; i < amount; i++) {
            arr.add(binaryToString(i, n));
        }
    }

    public void deleteInvalid(List<String> arr) {
        for (int i = 0; i < arr.size(); i++) {
            int open = 0;
            boolean shouldDelete = false;
            for (int k = 0; k < arr.get(i).length(); k++) {
                if (arr.get(i).charAt(k) == '(') {
                    open++;
                } else {
                    open--;
                }
                if (open < 0) {
                    shouldDelete = true;
                    break;
                }
            }
            if (open != 0) {
                shouldDelete = true;
            }
            if (shouldDelete) {
                arr.remove(i);
                i--;
            }
        }
    }

    public String binaryToString(int binary, int n) {
        String str = "";
        for (int i = 0; i < 2 * n; i++) {
            if (((binary >> i) & 1) == 1) {
                str += '(';
            } else {
                str += ')';
            }
        }
        return str;
    }

}
