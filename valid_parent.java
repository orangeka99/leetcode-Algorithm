import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class valid_parent {
    public boolean isValid(String s) {
        HashMap<String, Integer> symbol_dict = new HashMap<String ,Integer>();
        symbol_dict.put("(", 2);
        symbol_dict.put(")", 1);
        symbol_dict.put("{", 4);
        symbol_dict.put("}", 3);
        symbol_dict.put("[", 6);
        symbol_dict.put("]", 5);

        if (s.length() == 2){
            if (symbol_dict.get(String.valueOf(s.charAt(0))) != symbol_dict.get(String.valueOf(s.charAt(s.length() - 1))) + 1) {
                return false;
            }else{
                return true;
            }
        }
        if (s.length() % 2 != 0){
            return false;
        }
        if (s.charAt(0) == ']' || s.charAt(0) == '}' || s.charAt(0) == ')' ){
            return false;
        }
        if (s.charAt(s.length() - 1) == '{' || s.charAt(s.length() - 1) == '[' || s.charAt(s.length() - 1) == '('){
            return false;
        }
        List<Integer> prev_str = new ArrayList<>();
        
        for (int i1 = 0; i1 < s.length(); i1++){
            if (i1 == 0){
                prev_str.add(symbol_dict.get(String.valueOf(s.charAt(i1))));
            }else{
                if (prev_str.isEmpty()){
                    prev_str.add(symbol_dict.get(String.valueOf(s.charAt(i1))));
                    continue;
                }
                if (prev_str.get(prev_str.size() - 1) != symbol_dict.get(String.valueOf(s.charAt(i1))) + 1){
                    prev_str.add(symbol_dict.get(String.valueOf(s.charAt(i1))));
                    if (prev_str.size() > s.length() / 2){
                        return false;
                    }
                }else{
                    if (prev_str.size() != 0){
                        prev_str.remove(prev_str.size() - 1);
                    }
                }
            }
        }

        if (prev_str.isEmpty()){
            return true;
        }else{
            return false;
        }
        
    }

    public static void main(String[] args) {
    }
}
