import java.io.*;
import java.util.*;

public class Main {
        static long MOD = 1000000007;
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());        
        

        int[] dp = new int[1001];

        dp[0] = 0; dp[1] = 2; dp[2] = 7;
        for (int i = 3; i <= 1000; i++) {
            dp[i] = (3 * dp[i-1] % MOD + dp[i-2] % MOD - dp[i-3] % MOD + MOD) % MOD;
        }

        System.out.println(dp[N]);
    }
}