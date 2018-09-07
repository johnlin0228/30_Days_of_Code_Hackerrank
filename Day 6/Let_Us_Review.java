import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < N; i++) {
            String str = sc.nextLine();
            char[] charArray = str.toCharArray();
            String evenStr = "";
            String oddStr = "";
            for (int j = 0; j < charArray.length; j++) {
                if (j % 2 == 0) {
                    evenStr += charArray[j];
                } else {
                    oddStr += charArray[j];
                }
            }
            System.out.println(evenStr + " " + oddStr);
        }
        sc.close();
    }
}