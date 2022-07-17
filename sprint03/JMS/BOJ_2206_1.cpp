#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

typedef struct Index {
	int i, j;
}Index;

typedef struct Matrix {
	int wall, dis;
	bool visited, isRoute;
}Matrix;

int n, m, walldistancemax = 0;
int diri[4] = { -1,1,0,0 };
int dirj[4] = { 0,0,-1,1 };
Matrix mat[1000][1000];
bool isBreak;

void InitMat() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			mat[i][j].dis = n * m;
	}

	mat[0][0].visited = true;
	mat[0][0].dis = 1;
	mat[n - 1][m - 1].isRoute = true;
}

void SecInitMat() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			mat[i][j].visited = false;
	}
}

void BFS() {
	queue<Index> q;

	q.push({ 0,0 });

	while (!q.empty()) {
		Index index = q.front();
		q.pop();

		if (index.i == n - 1 && index.j == m - 1)
			return;

		for (int i = 0; i < 4; i++) {
			Index nextindex = { index.i + diri[i], index.j + dirj[i] };

			if (nextindex.i < 0 || nextindex.j < 0 || nextindex.i >= n || nextindex.j >= m ||
				mat[nextindex.i][nextindex.j].visited || mat[nextindex.i][nextindex.j].wall)
				continue;

			mat[nextindex.i][nextindex.j].visited = true;
			mat[nextindex.i][nextindex.j].dis = mat[index.i][index.j].dis + 1;
			q.push(nextindex);
		}

		if (q.empty() && !isBreak) {

			
			for (int i = 0; i < 4; i++) {
				Index nextindex = { index.i + diri[i], index.j + dirj[i] };

				if (nextindex.i < 0 || nextindex.j < 0 || nextindex.i >= n || nextindex.j >= m ||
					mat[nextindex.i][nextindex.j].visited)
					continue;

				isBreak = true;
				mat[nextindex.i][nextindex.j].wall = 0;
				mat[nextindex.i][nextindex.j].visited = true;
				mat[nextindex.i][nextindex.j].dis = mat[index.i][index.j].dis + 1;
				q.push(nextindex);
			}
		}
	}
}

void BFSRoute() {
	queue<Index> q;

	SecInitMat();
	q.push({ n - 1,m - 1 });
	mat[n - 1][m - 1].visited = true;

	while (!q.empty()) {
		Index index = q.front();
		q.pop();

		if (index.i == 0 && index.j == 0) {
			mat[0][0].isRoute = true;
			return;
		}

		for (int i = 0; i < 4; i++) {
			Index nextindex = { index.i + diri[i], index.j + dirj[i] };

			if (nextindex.i < 0 || nextindex.j < 0 || nextindex.i >= n || nextindex.j >= m ||
				mat[nextindex.i][nextindex.j].visited || mat[nextindex.i][nextindex.j].wall)
				continue;

			if (mat[nextindex.i][nextindex.j].dis + 1 == mat[index.i][index.j].dis) {
				mat[nextindex.i][nextindex.j].visited = true;
				mat[nextindex.i][nextindex.j].isRoute = true;
				q.push(nextindex);
			}
		}
	}
}

void FindBreakWallMin() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!mat[i][j].wall) {
				for (int k = 0; k < 4; k++) {
					Index index = { i + diri[k], j + dirj[k] };

					if (index.i < 0 || index.j < 0 || index.i >= n || index.j >= m || !mat[index.i][index.j].wall)
						continue;

					for (int l = 0; l < 4; l++) {
						Index nextindex = { index.i + diri[l], index.j + dirj[l] };

						if (nextindex.i < 0 || nextindex.j < 0 || nextindex.i >= n || nextindex.j >= m ||
							mat[nextindex.i][nextindex.j].wall)
							continue;
						if (nextindex.i == i && nextindex.j == j)
							continue;

						if (mat[i][j].dis + 2 < mat[nextindex.i][nextindex.j].dis && mat[nextindex.i][nextindex.j].isRoute)
							walldistancemax = max(walldistancemax, abs(mat[nextindex.i][nextindex.j].dis - mat[i][j].dis));
					}
				}
			}
		}
	}

	if (walldistancemax != 0)
		cout << mat[n - 1][m - 1].dis - walldistancemax + 2;
	else
		cout << mat[n - 1][m - 1].dis;
}

void Input() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		getchar();
		string str;
		cin >> str;
		for (int j = 0; j < m; j++)
			mat[i][j].wall = str[j] - '0';
	}
}

int main() {
	Input();
	InitMat();

	BFS();
	if (mat[n - 1][m - 1].dis != n * m) {
		if (!isBreak) {
			BFSRoute();
			FindBreakWallMin();
		}
		else
			cout << mat[n - 1][m - 1].dis;
	}
	else
		cout << -1;
}


/*
6 4
0000
0110
0000
1101
0111
0000

이 test 고쳐야함
*/
