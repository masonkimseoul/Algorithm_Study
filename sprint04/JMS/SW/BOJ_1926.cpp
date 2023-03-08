#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef struct Coordinate {
	int i, j;
}Coordinate;

vector<int> area;
int n, m;
int arr[500][500];
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };
bool visited[500][500];

void Input() {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> arr[i][j];
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

			if (nextCoordinate.i < 0 || nextCoordinate.j < 0 || nextCoordinate.i >= n || nextCoordinate.j >= m || visited[nextCoordinate.i][nextCoordinate.j] ||
				!arr[nextCoordinate.i][nextCoordinate.j])
				continue;

			cnt++;
			q.push(nextCoordinate);
			visited[nextCoordinate.i][nextCoordinate.j] = true;
		}
	}

	area.push_back(cnt);
}

int main() {
	int cnt = 0;

	Input();
	area.push_back(0);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!visited[i][j] && arr[i][j]){
				cnt++;
				BFS({ i,j });
			}
		}
	}

	sort(area.begin(), area.end());
	
	cout << cnt << '\n';
	cout << area[area.size() - 1];
}
