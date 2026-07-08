import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();

        sol(k, n, 1, 0, "");
    }

    static void sol(int k, int n, int idx, int depth, String arr) {
        if (depth == n) {
            System.out.println(arr);
            return;
        }

        for (int i = idx; i <= k; i++) {
            sol(k, n, idx, depth+1, arr + i + " ");
        }
    }
}