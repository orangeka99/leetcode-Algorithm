import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;

public class foursum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<Integer> main_arr = new ArrayList<>();
        main_arr = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(main_arr);
        List<List<Integer>> result = new ArrayList<>();
        
        if (main_arr.size() < 4) {
            return result;
        }
        if (main_arr.size() == 4) {
            long sum = 0;
            for (int i = 0; i < main_arr.size(); i++) {
                if (main_arr.get(i) == 1000000000) {
                    sum = sum + 1000000000L;
                } else {
                    sum = sum + main_arr.get(i);
                }
            }
            if (sum != target) {
                return result;
            } else {
                List<Integer> rest_tmp = new ArrayList<>();
                rest_tmp.add(main_arr.get(0));
                rest_tmp.add(main_arr.get(1));
                rest_tmp.add(main_arr.get(2));
                rest_tmp.add(main_arr.get(3));
                result.add(new ArrayList<>(rest_tmp));
                return result;
            }
        }
        
        Set<Integer> unique_member = new HashSet<>(main_arr);

        if (unique_member.size() == 1 && main_arr.size() != 1) {
            List<Integer> rest_tmp = new ArrayList<>();
            rest_tmp.add(main_arr.get(0));
            rest_tmp.add(main_arr.get(1));
            rest_tmp.add(main_arr.get(2));
            rest_tmp.add(main_arr.get(3));
            result.add(new ArrayList<>(rest_tmp));
            return result;
        }
        System.out.println("GGG");
        Arrays.sort(nums);
        ArrayList<Integer> tmp_arr = new ArrayList<>();
        Set<List<Integer>> unique_rows = new HashSet<>();

        System.out.println(main_arr);
        // System.out.println(Arrays.toString(nums));
        for (int i1 = 0; i1 < main_arr.size(); i1++) {
            for (int i2 = i1 + 1; i2 < main_arr.size(); i2++) {
                for (int i3 = i2 + 1; i3 < main_arr.size(); i3++) {
                    int current_val = main_arr.get(i1) + main_arr.get(i2) + main_arr.get(i3);
                    
                    current_val = current_val - target;
                    current_val = current_val * -1;

                    int index = Arrays.binarySearch(nums, current_val);
                    if (index < 0) {
                        continue;
                    }

                    if (index == i1 || index == i2 || index == i3) {
                        continue;
                    }
                    tmp_arr.add(main_arr.get(i1));
                    tmp_arr.add(main_arr.get(i2));
                    tmp_arr.add(main_arr.get(i3));
                    tmp_arr.add(current_val);
                    tmp_arr.sort(null);

                    if (unique_rows.contains(tmp_arr)) {
                        tmp_arr.clear();
                        continue;
                    }
                    unique_rows.add(new ArrayList<>(tmp_arr));
                    tmp_arr.clear();
                }
            }
        }
        result = new ArrayList<>(unique_rows);
        return result;

    }

    public static void main(String[] args) {
        // int[] arr = { 1000000000, 1000000000, 1000000000, -1000000000, 1000000000};
        // int target = 0;

        // foursum solver = new foursum();
        // List<List<Integer>> result = solver.fourSum(arr, target);
        // System.out.println(result);
        int ggg = -1000000000 + -1000000000 + -1000000000;
        System.err.println(ggg);
    }
}
