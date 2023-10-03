

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        // 한 줄씩 공백으로 끊어서 받아줌.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());   // 배열 크기
        int M = Integer.parseInt(st.nextToken());   // 질의 수
        int A[][] = new int[N+1][N+1];  // 2차원 수 배열
        int D[][] = new int[N+1][N+1];  // 구간 합  
        

        // 1. 2차원 수 배열 입력
         for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }       

        
        // 2. 구간 합 입력
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
               D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j];  
            }
        }


        // 3. 질의 입력 및 계산
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            // 질의 입력
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            
            // 구간 합 배열로 질의 답변
            int result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1];
            System.out.println(result);
        
        }
    }

}