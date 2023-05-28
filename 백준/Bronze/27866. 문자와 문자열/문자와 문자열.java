import java.util.Scanner;

class Main {

    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);

        String S = sc.next();
        int n = sc.nextInt();

        char c = S.charAt(n-1);
        System.out.println(c);

    }
}