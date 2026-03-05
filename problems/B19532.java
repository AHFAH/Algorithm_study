package BOJ;

import java.util.Scanner;

public class B19532 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int e = sc.nextInt();
        int f = sc.nextInt();

        // 완전탐색
/*        for (int i = -999; i < 1000; i++) {
            for (int j = -999; j < 1000; j++) {
                if(a*i+b*j==c && d*i+e*j==f) {
                    System.out.println(i+" "+j);
                    System.exit(0);
                }
            }
        }*/

        //가감법
        int x = (c*e - b*f) / (a*e - b*d);
        int y = (c*d - a*f) / (b*d - a*e);

        System.out.println(x + " " + y);
    }
}
