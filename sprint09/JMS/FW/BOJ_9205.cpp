#include <iostream>
#include <cmath>
#include <map>
#include <cstring>
#include <queue>
#include <vector>

using namespace std;

typedef struct Coordinate {
	int i, j;
}Coordinate;

Coordinate home, store[102], festival;
map<int, vector<int>> m;
int n, f = 0;
bool visited[102];

bool isWalk(Coordinate A, Coordinate B) {
	if (abs(A.i - B.i) + abs(A.j - B.j) <= 1000)
		return true;
	else
		return false;
}

void DFS(Coordinate current, int index) {
	if (isWalk(current,festival) || f) {
		f = 1;
		return;
	}

	for (auto p : m[index]) {
		if (f)
			return;
		if (!visited[p]) {
			visited[p] = true;
			DFS(store[p], p);
			visited[p] = false;
		}
	}
}

void BFS() {
	queue<int> q;
	q.push(101);
	visited[101] = true;

	while (!q.empty()) {
		int current = q.front();
		q.pop();

		if (isWalk(store[current], festival)) {
			f = 1;
			return;
		}

		for (auto p : m[current]) {
			if (!visited[p]) {
				visited[p] = true;
				q.push(p);
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;

	for (int i = 0;i < t;i++) {
		cin >> n;
		int x, y;
		cin >> x >> y;
		home = { x,y };
		store[101] = home;
		for (int j = 0;j < n;j++) {
			cin >> x >> y;
			store[j] = { x,y };

			for (int k = 0;k < j;k++) {
				if (isWalk(store[j], store[k])) {
					m[j].push_back(k);
					m[k].push_back(j);
				}
			}

			if (isWalk(home, store[j]))
				m[101].push_back(j);
		}

		cin >> x >> y;
		festival = { x,y };

		BFS();

		if(f)
			cout << "happy";
		else
			cout << "sad";
		cout << '\n';

		memset(visited, false, sizeof(visited));
		m.clear();
		f = 0;
	}
}
