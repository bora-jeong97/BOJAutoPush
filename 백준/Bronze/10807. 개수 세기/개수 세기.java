

import java.util.Scanner;

class Main {

    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int array[] = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();    
        }

        int targetN = sc.nextInt();
        

        for (int i = 0; i < array.length; i++) {
            if(targetN == array[i]){
                sum++;
            }
        }

        System.out.println(sum);

    }
}