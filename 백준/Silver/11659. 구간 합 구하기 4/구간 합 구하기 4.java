

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    /*
        합 배열 공식 
        S[i] = S[i-1] + A[i] 
        배열 A
        합 배열 S
        https://www.notion.so/8f2100d3885d4253bfa1cf6cc9213a6e 노션
        https://www.youtube.com/watch?v=JSfXW7UJ04Y 강의
     */
    /**
     * @param args
     * @throws IOException
     */
    public static void main(String[] args) throws IOException {
        // 숫자가 많을 때 Scanner보다 많음
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        // 길게 받아주기 용의
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int suNo = Integer.parseInt(stringTokenizer.nextToken());       // 숫자 개수
        int quizNo = Integer.parseInt(stringTokenizer.nextToken());     // 질의 개수
        long[] S = new long[suNo +1]; // 배열은 0번째 index부터 시작하는데 편의성을 위해 1부터 시작하려구

        // 합 배열 숫자 개수만큼 반복하기
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 1; i <= suNo; i++) {
            S[i]  = S[i-1] + Integer.parseInt(stringTokenizer.nextToken());  
        }

        // 질의 개수만큼 반복하기
        for (int q = 0; q < quizNo; q++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int i = Integer.parseInt(stringTokenizer.nextToken());
            int j = Integer.parseInt(stringTokenizer.nextToken());
            System.out.println(S[j] - S[i-1]);
        }




    }

}
