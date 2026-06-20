import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        
        int globalSum = 0;

        for (int i = 0; i < n-2; i++) {
            for (int j = 0; j < n-2; j++) {
                int tmpSum = 0;
                for (int x = 0; x <= 2; x++) {
                    for (int y = 0; y <= 2; y++) {
                        tmpSum += grid[i+x][j+y];
                    }
                }
                globalSum = Math.max(tmpSum, globalSum);
            }
        }    

        System.out.println(globalSum);
    }
}