#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, K;
int arr[101][101] = { 0 };
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };
bool visited[101][101];
vector<int> area;

typedef struct Coordinate {
	int i, j;
}Coordinate;

void Input() {
	cin >> N >> M >> K;

	for (int i = 0; i < K; i++) {
		int x1, x2, y1, y2;

		cin >> x1 >> y1 >> x2 >> y2;

		for (int i = y1; i < y2; i++) {
			for (int j = x1; j < x2; j++)
				arr[i][j] = 1;
		}
	}
}

void BFS(Coordinate coordinate) {
	queue<Coordinate> q;
	int cnt = 1;

	q.push(coordinate);
	visited[coordinate.i][coordinate.j] = true;

	while (!q.empty()) {
		Coordinate currentCoordinate = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			Coordinate nextCoordinate = { currentCoordinate.i + diri[i], currentCoordinate.j + dirj[i] };

			if (nextCoordinate.i < 0 || nextCoordinate.j < 0 || nextCoordinate.i >= N || nextCoordinate.j >= M || visited[nextCoordinate.i][nextCoordinate.j] ||
				arr[nextCoordinate.i][nextCoordinate.j])
				continue;

			q.push(nextCoordinate);
			visited[nextCoordinate.i][nextCoordinate.j] = true;
			cnt++;
		}
	}

	area.push_back(cnt);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int cnt = 0;

	Input();

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (!arr[i][j] && !visited[i][j]) {
				cnt++;
				BFS({ i,j });
			}
		}
	}

	sort(area.begin(), area.end());
	cout << cnt << '\n';
	for (auto p : area)
		cout << p << " ";
}
