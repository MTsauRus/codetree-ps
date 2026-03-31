import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] dp = new int[1001];

        dp[0] = 0; dp[1] = 1; dp[2] = 2; dp[3] = 3;

        for (int i = 4; i < 1001; i++) {
            dp[i] = (dp[i-1] + dp[i-2])%10007;
        }

        System.out.print(dp[n]);

    }
}