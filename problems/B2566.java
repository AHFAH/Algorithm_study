package BOJ;

import java.util.Scanner;

public class B2566 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[9][9];
        int max = 0;
        int num;
        int row = 1;
        int column = 1;

        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                num = sc.nextInt();
                if (num > max) {
                    max = num;
                    row = i+1;
                    column = j+1;
                }
                arr[i][j] = num;
            }
        }
        sc.close();

        System.out.println(max);
        System.out.println(row + " " + column);
    }
}
