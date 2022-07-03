#include <iostream>
#include <algorithm>

using namespace std;

int N;

typedef struct {
	int h;
	bool visited, isflooding;
}Arr;

typedef struct {
	int i, j;
}Index;

Arr arr[100][100];
int diri[4] = { -1,1,0,0 }, dirj[4] = { 0,0,-1,1 };
int hmax = 0;

void InitArr(int heightflood) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][j].h > heightflood)
				arr[i][j].isflooding = false;
			else
				arr[i][j].isflooding = true;
			arr[i][j].visited = false;
		}
	}
}

void Input() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j].h;
			hmax = max(hmax, arr[i][j].h);
		}
	}
}

void DFS(Index index) {
	arr[index.i][index.j].visited = true;

	for (int i = 0; i < 4; i++) {
		Index temp = { index.i + diri[i], index.j + dirj[i] };

		if (temp.i < 0 || temp.j < 0 || temp.i >= N || temp.j >= N || arr[temp.i][temp.j].visited || arr[temp.i][temp.j].isflooding)
			continue;

		DFS(temp);
	}
}

int main() {
	int cntmax = 0;
	cin >> N;
	Input();

	for (int i = 0; i < hmax; i++) {
		int cnt = 0;

		InitArr(i);
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (!arr[j][k].isflooding && !arr[j][k].visited) {
					Index index = { j,k };

					cnt++;
					DFS(index);
				}
			}
		}

		cntmax = max(cntmax, cnt);
	}

	cout << cntmax;
}
