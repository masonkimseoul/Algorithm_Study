#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	char inputboard[50][50];
	int cnta;
	int cntb;
	int minpoint = 64;
	int tpoint;
	for (int i = 0; i < N; i++) {
		scanf("%s", inputboard[i]);
	}
	for (int col = 0; col < N-7; col++) {
		for (int row = 0; row < M-7; row++) {
			//비교 시작
			cnta = 0;
			cntb = 0;
			for (int col2 = col; col2 < col + 8; col2++) {
				for (int row2 = row; row2 < row + 8; row2++) {
					//처음 시작블록을 검은색으로 할 때 검은색 짝수가 검은색 홀수가 흰색
						//짝수일 때
						if ((col2 + row2) % 2 == 0) {
							if (inputboard[col2][row2] == 'W') {
								cnta++;
							}
						}
						else {
							if (inputboard[col2][row2] == 'B') {
								cnta++;
							}
						}
					//처음시작 블록을 흰색으로 할 때 짝수가 흰색 홀수가 검은색
						if ((col2 + row2) % 2 == 0) {
							if (inputboard[col2][row2] == 'B') {
								cntb++;
							}
						}
						else {
							if (inputboard[col2][row2] == 'W') {
								cntb++;
							}
						}
					}
			}
			if (cnta <= cntb)
				tpoint = cnta;
			else
				tpoint = cntb;

			if (minpoint > tpoint)
				minpoint = tpoint;
		}
	}
	printf("%d", minpoint);




}