#include <iostream>
#include <algorithm>
using namespace std;

int FindChess(char arr[][50], int n, int m, int N, int M, int mode) {
	int cnt = 0, f;

	for (int i = n; i < n + 8; i++) {
		for (int j = m; j < m + 8; j++) {
			if (i == n && j == m) {
				if (mode) {
					if (arr[i][j] != 'W')
						cnt++;
					arr[i][j] = 'W';
				}
				else {
					if (arr[i][j] != 'B')
						cnt++;
					arr[i][j] = 'B';
				}
				continue;
			}

			f = 1;

			if (i != n)
				if (arr[i - 1][j] != arr[i][j]) f = 0;
			if (j != m)
				if (arr[i][j - 1] != arr[i][j]) f = 0;

			if (f) {
				cnt++;
				arr[i][j] = (arr[i][j] == 'B' ? 'W' : 'B');
			}
		}
	}

	return cnt;
}

void Input(char arr[][50], int N, int M) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			cin >> arr[i][j];
	}
}

void SwapArray(char arr[][50], char arr1[][50], int N, int M) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			arr1[i][j] = arr[i][j];
	} 
}

int main() {
	int N, M, mincnt = 100;
	char arr[50][50], temp[50][50];

	cin >> N >> M;
	Input(arr, N, M);

	for (int i = 0; i < N - 7; i++) {
		for (int j = 0; j < M - 7; j++) {
			SwapArray(arr, temp, N, M);
			mincnt = min(mincnt, FindChess(temp, i, j, N, M, 0));
			SwapArray(arr, temp, N, M);
			mincnt = min(mincnt, FindChess(temp, i, j, N, M, 1));
		}
	}

	cout << mincnt;
}
