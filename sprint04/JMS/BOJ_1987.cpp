#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

char c[21][21];
int R, C, maxcnt = 0;
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };
map<char, int> visited;

typedef struct Coordinate {
	int i, j, dis;
}Coordinate;

void Input() {
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		getchar();
		for (int j = 0; j < C; j++)
			cin >> c[i][j];
	}
}

void DFS(Coordinate index) {
	maxcnt = max(maxcnt, index.dis);
	visited[c[index.i][index.j]] = 1;

	for (int i = 0; i < 4; i++) {
		Coordinate nextCoordinate = { index.i + diri[i], index.j + dirj[i], index.dis + 1 };

		if (nextCoordinate.i < 0 || nextCoordinate.j < 0 || nextCoordinate.i >= R  || nextCoordinate.j >= C || visited[c[nextCoordinate.i][nextCoordinate.j]] == 1)
			continue;

		DFS(nextCoordinate);
	}

	visited[c[index.i][index.j]] = 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	Input();
	DFS({ 0,0,1 });
	cout << maxcnt;
}
