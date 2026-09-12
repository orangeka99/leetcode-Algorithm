import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

class threeSumClosest {
    public int threeSum(int[] nums, int target) {
        List<Integer> main_arr = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(main_arr);
        int main_len = main_arr.size();
        if (target < main_arr.get(0)){ 
            if (main_arr.get(0) + main_arr.get(1) + main_arr.get(2) > target){
                return main_arr.get(0) + main_arr.get(1) + main_arr.get(2);
            }
        }
        if (target > main_arr.get(main_len - 1)){
            if (main_arr.get(main_len - 1) + main_arr.get(main_len - 2) + main_arr.get(main_len - 3) < target){
                return main_arr.get(main_len - 1) + main_arr.get(main_len - 2) + main_arr.get(main_len - 3);
            }

        }
        List<Integer> prev_arr = new ArrayList<>();
        List<Integer> val_list = new ArrayList<>();
        val_list.add(target - 1);
        val_list.add(target + 1);
        val_list.add(target);

        int current_val = 0;
        int val_len = 0;
        for (int i1 = 0; i1 < main_len; i1++){
            for (int i2 = i1 + 1; i2 < main_len; i2++){
                for (int i3 = 0; i3 < val_list.size(); i3++){
                    if (!prev_arr.isEmpty()){
                        if (prev_arr.get(0) == target){
                            break;
                        }
                    }
                    current_val = main_arr.get(i1) + main_arr.get(i2) - val_list.get(i3);
                    current_val = current_val * -1;
                    int index = main_arr.indexOf(current_val);
                    if (index < 0){
                        continue;
                    }
                    if (index == i1 || index == i2){
                        continue;
                    }
                    int total = main_arr.get(i1) + main_arr.get(i2) + current_val;
                    if (val_list.get(i3) < total){
                        val_len = Math.abs(val_list.get(i3) - total);
                    }else if (val_list.get(i3) > total){
                        val_len = Math.abs(total - val_list.get(i3));
                    }else{
                        val_len = 0;
                    }
                    if (prev_arr.isEmpty()){
                        prev_arr.add(total);
                        prev_arr.add(val_len);
                    }else{
                        if (total == target){
                            prev_arr.set(0, total);
                            prev_arr.set(1, val_len);
                        }else{
                            if (prev_arr.get(1) >= val_len){
                                prev_arr.set(0, total);
                                prev_arr.set(1, val_len);
                            }
                        }
                    }
                }
            }
        }
        if (prev_arr.size() != 0){
            return prev_arr.get(0);
        }else{
            current_val = 0;
            val_len = 0;
            for (int i1 = 0;i1 < main_len; i1++){
                for (int i2 = i1 + 1; i2 < main_len; i2++){
                    for (int i3 = i2 + 1; i3 < main_len; i3++){
                        current_val = main_arr.get(i1) + main_arr.get(i2) + main_arr.get(i3);
                        if (current_val < target){
                            val_len = Math.abs(current_val - target);
                        }else{
                            val_len = Math.abs(target - current_val);
                        }
                        if (i1 == 0 && i2 == 1 && i3 == 2){
                            prev_arr.add(current_val);
                            prev_arr.add(val_len);
                        }else{
                            if (val_len < prev_arr.get(1)){
                                prev_arr.set(0, current_val);
                                prev_arr.set(1, val_len);
                            }
                        }
                    }
                    
                }
            }
            return prev_arr.get(0);
        }

    }
}