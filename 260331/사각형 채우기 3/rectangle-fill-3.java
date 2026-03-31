import java.io.*;
import java.util.*;

public class Main {

        public static void main(String[] args) throws IOException {
        int MOD = 1000000007;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());        
        

        int[] dp = new int[1001];

        dp[0] = 1; dp[1] = 2; dp[2] = 7;
        for (int i = 3; i <= 1000; i++) {
            dp[i] = (3 * dp[i-1] + dp[i-2] - dp[i-3]) % MOD;
        }

        System.out.println(dp[N]);
    }
}