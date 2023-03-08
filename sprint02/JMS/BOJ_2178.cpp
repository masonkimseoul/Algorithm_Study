#include <iostream>
#include <queue>
#include <string>

using namespace std;

int N, M;
int arr[100][100] = { 0 };
int desti[4] = { -1, 1,0,0 };
int destj[4] = { 0,0,-1,1 };
bool visited[100][100] = { false };

typedef struct axes {
	int i, j, dis;
}Axes;

void Input() {
	for (int i = 0; i < N; i++) {
		getchar();
		string temp;
		cin >> temp;

		for (int j = 0; j < M; j++)
			arr[i][j] = temp[j] - 48;
	}
}

void BFS() {
	queue<Axes> que;

	que.push({ 0,0,1 });
	visited[0][0] = true;

	while (!que.empty()) {
		Axes frontAxes = que.front();
		
		que.pop();

		if (frontAxes.i == N - 1 && frontAxes.j == M - 1) {
			cout << frontAxes.dis;
			return;
		}

		for (int i = 0; i < 4; i++) {
			Axes nextDest = { frontAxes.i + desti[i], frontAxes.j + destj[i], frontAxes.dis + 1 };

			if (nextDest.i < 0 || nextDest.j < 0 || nextDest.i >= N || nextDest.j >= M || !arr[nextDest.i][nextDest.j] || visited[nextDest.i][nextDest.j])
				continue;

			visited[nextDest.i][nextDest.j] = true;
			que.push(nextDest);
		}
	}
}

int main() {
	cin >> N >> M;
	Input();
	BFS();
}
