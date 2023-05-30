import java.util.Scanner;

class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int n1 = sc.nextInt();
        int n2 = sc.nextInt();

        int[][] arrayA = new int[n1][n2];
        int[][] arrayB = new int[n1][n2];

        // arrayA 입력
        for (int i = 0; i < arrayA.length; i++) {
            for (int j = 0; j < arrayA[i].length; j++) {
                arrayA[i][j] = sc.nextInt();
            }
        }

        // arrayB 입력
        for (int i = 0; i < arrayB.length; i++) {
            for (int j = 0; j < arrayB[i].length; j++) {
                arrayB[i][j] = sc.nextInt();
            }
        }

        // arrayA + arrayB
        for (int i = 0; i < arrayB.length; i++) {
            for (int j = 0; j < arrayB[i].length; j++) {
                int num = arrayA[i][j] + arrayB[i][j];
                System.out.printf("%d ", num);
            }
            System.out.println();
        }

    }
}
