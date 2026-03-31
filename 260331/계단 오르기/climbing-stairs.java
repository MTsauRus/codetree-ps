import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] dp = new int[1001];

        dp[0] = 0; dp[1] = 0; dp[2] = 1; dp[3] = 1;
        for (int i = 4; i < 1001; i++) {
            dp[i] = (dp[i-2]+1 + dp[i-3]+1) % 10007;

        }
        int N = Integer.parseInt(br.readLine());
        System.out.println(dp[N]);
    }
}