package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class B5597 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = new int[30];

        for(int i=0; i<28; i++){
            int ok = sc.nextInt();
            a[ok-1] = 1;
        }

        for(int i=0; i<30; i++){
            if(a[i]==0)
                System.out.println(i+1);
        }

        sc.close();
    }
}
