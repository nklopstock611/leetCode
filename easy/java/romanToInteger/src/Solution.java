import java.lang.reflect.Array;
import java.util.HashMap;

public class Solution {

    HashMap<Character, Integer> romans = new HashMap<Character, Integer>();

    public Solution() {
        romans.put('I', 1);
        romans.put('V', 5);
        romans.put('X', 10);
        romans.put('L', 50);
        romans.put('C', 100);
        romans.put('D', 500);
        romans.put('M', 1000);
    }

    public Integer romanToInteger(String r) {
        Integer integer = 0;
        Integer letter_value = 0;
        char[] letters = r.toCharArray();
        for (int i = 0; i < letters.length; i++) {
            if (romans.get(letters[i + 1]) > romans.get(letters[i])) {
                letter_value = romans.get(letters[i + 1]) - romans.get(letters[i]);
                i++;
            }
            else {
                letter_value = romans.get(letters[i]);
            }
            integer = integer + letter_value;
        }
        if (romans.get(letters[letters.length - 1]) < romans.get(letters[letters.length - 2])) {
            integer = integer + romans.get(letters[letters.length - 1]);
        }

        return integer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.romanToInteger("LVIII"));
    }

}
