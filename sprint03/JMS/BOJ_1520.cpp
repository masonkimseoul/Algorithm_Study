#include <iostream>
#include <cstring>

using namespace std;

typedef struct coordinate {
	int i, j;
}coordinate;

int N, M;
int arr[500][500];
int cnt[500][500];
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };

int DFS(coordinate index) {
	if (index.i == N - 1 && index.j == M - 1)
		return 1;
	if (cnt[index.i][index.j] != -1)
		return cnt[index.i][index.j];

	cnt[index.i][index.j] = 0;

	for (int i = 0; i < 4; i++) {
		coordinate nextcoordinate = { index.i + diri[i], index.j + dirj[i] };

		if (nextcoordinate.i < 0 || nextcoordinate.j < 0 || nextcoordinate.i >= N || nextcoordinate.j >= M || 
			arr[nextcoordinate.i][nextcoordinate.j] >= arr[index.i][index.j])
			continue;

		cnt[index.i][index.j] += DFS(nextcoordinate);
	}

	return cnt[index.i][index.j];
}

void Input() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			cin >> arr[i][j];
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	memset(cnt, -1, sizeof(cnt));
	Input();
	cout << DFS({ 0,0 });
}
