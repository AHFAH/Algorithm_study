package BOJ;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class B3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Set<Integer> set = new HashSet<Integer>();

        for(int i=0; i<10; i++){
            set.add(sc.nextInt()%42);
        }
        System.out.println(set.toArray().length);
    }
}
