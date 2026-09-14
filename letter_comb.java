import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class letter_comb {
    
    public static void main(String[] args){
        String digits = "23";
        HashMap<String, String> phone_dict = new HashMap<String, String>();
        phone_dict.put("2" , "abc");
        phone_dict.put("3" , "def");
        phone_dict.put("4" , "ghi");
        phone_dict.put("5" , "jkl");
        phone_dict.put("6" , "mno");
        phone_dict.put("7" , "pqrs");
        phone_dict.put("8" , "tuv");
        phone_dict.put("9" , "wxyz");
        List<String> result = new ArrayList<>();
        if (digits.length() == 1){
            String phone_str = phone_dict.get(String.valueOf(digits.charAt(0)));
            for (int i = 0; i < phone_str.length();i++){
                result.add(String.valueOf(phone_str.charAt(i)));
            }
            
            // return result;
            System.out.println(result);
            return;
        }

        String first_str = phone_dict.get(String.valueOf(digits.charAt(0)));
        String main_str = digits.substring(1, digits.length());
        
        for (int i1 = 0 ; i1 < main_str.length(); i1++){
            String dic_str = phone_dict.get(String.valueOf(main_str.charAt(i1)));
            if (i1 == 0){
                for (int i2 = 0 ; i2 < first_str.length(); i2++){
                    for(int i3 = 0; i3 < dic_str.length(); i3++){
                        result.add("" + first_str.charAt(i2) + dic_str.charAt(i3));
                    }

                }
            }else{
                List<String> tmp_arr = new ArrayList<>();
                for (int i2 = 0; i2 < result.size(); i2++){
                    for (int i3 = 0; i3 < dic_str.length(); i3++){
                        tmp_arr.add("" + result.get(i2) + dic_str.charAt(i3));
                    }
                }
                result = tmp_arr;
            }
        }

        // return result;
        System.out.println(result);
    }
}