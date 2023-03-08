#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int arr[500][500];
int maxsum = 0;
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };
bool visited[500][500] = { false };

typedef struct Cd {
	int y, x;
}Cd;

void DFS(Cd cd, int depth, int sum) {
	sum += arr[cd.y][cd.x];

	if (depth == 4) {
		maxsum = max(maxsum, sum);
		return;
	}

	for (int i = 0; i < 4; i++) {
		Cd currentCD = { cd.y + diri[i], cd.x + dirj[i] };

		if (currentCD.x >= 0 && currentCD.y >= 0 && currentCD.x < M && currentCD.y < N && !visited[currentCD.y][currentCD.x]) {
			visited[currentCD.y][currentCD.x] = true;
			DFS(currentCD, depth + 1, sum);
			visited[currentCD.y][currentCD.x] = false;
		}
	}
}

void LastTetromino(Cd cd) {
	if (cd.x > 0 && cd.x < M - 1 && cd.y < N - 1) {
		int sum = arr[cd.y][cd.x];
		sum += arr[cd.y][cd.x - 1] + arr[cd.y][cd.x + 1] + arr[cd.y + 1][cd.x];
		maxsum = max(maxsum, sum);
	}
	if (cd.x > 0 && cd.y < N - 1 && cd.y > 0) {
		int sum = arr[cd.y][cd.x];
		sum += arr[cd.y][cd.x - 1] + arr[cd.y - 1][cd.x] + arr[cd.y + 1][cd.x];
		maxsum = max(maxsum, sum);
	}
	if (cd.y > 0 && cd.x < M - 1 && cd.x > 0) {
		int sum = arr[cd.y][cd.x];
		sum += arr[cd.y][cd.x - 1] + arr[cd.y - 1][cd.x] + arr[cd.y][cd.x+1];
		maxsum = max(maxsum, sum);
	}
	if (cd.x < M - 1 && cd.y < N - 1 && cd.y > 0) {
		int sum = arr[cd.y][cd.x];
		sum += arr[cd.y][cd.x + 1] + arr[cd.y - 1][cd.x] + arr[cd.y + 1][cd.x];
		maxsum = max(maxsum, sum);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) cin >> arr[i][j];

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			LastTetromino({ i,j });
			visited[i][j] = true;
			DFS({ i,j }, 1, 0);
			visited[i][j] = false;
		}

	cout << maxsum;
}
