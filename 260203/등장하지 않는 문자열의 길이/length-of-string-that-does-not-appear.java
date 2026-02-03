import java.util.Scanner;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();

        int low = 1;
        int high = n;
        int ans = 0;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (hasDuplicate(str, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }

        }
        
        System.out.println(ans + 1);
        
    }

    static boolean hasDuplicate(String str, int len) {
        HashSet<String> set = new HashSet<>();

        for (int i = 0; i <= str.length() - len; i++) {
            String sub = str.substring(i, i+len);

            if (!set.add(sub)) {
                return true;
            }
         }
         return false;
    }
}