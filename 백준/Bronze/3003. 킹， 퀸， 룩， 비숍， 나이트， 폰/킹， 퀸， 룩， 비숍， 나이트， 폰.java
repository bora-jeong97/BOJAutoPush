
import java.util.Scanner;

class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int array[] = {
            1, 1, 2, 2, 2, 8
        };
        int input[] = new int[6];
        for (int i = 0; i < input.length; i++) {
            input[i] = sc.nextInt();
            int num = array[i] - input[i];
            System.out.print(num+" ");
        }

    }
}