#include <iostream>
#include <vector>
#include <map>
#include <cstring>
#include <queue>

using namespace std;

int k, v, e;
map<int, vector<int>> graph;
int color[20001];
bool visited[20001];

bool BFS(int index) {
	queue<int> q;

	q.push(index);
	visited[index] = true;
	color[index] = 1;

	while (!q.empty()) {
		int currentIndex = q.front();
		q.pop();

		for (auto p : graph[currentIndex]) {
			if (color[p] == color[currentIndex])
				return true;

			if (visited[p])
				continue;

			q.push(p);
			visited[p] = true;
			if (color[currentIndex] == 1)
				color[p] = 2;
			else
				color[p] = 1;
		}
	}

	return false;
}

int main() {
	cin >> k;
	for (int i = 0; i < k; i++) {

		cin >> v >> e;

		for (int j = 0; j < e; j++) {
			int vertex1, vertex2;

			cin >> vertex1 >> vertex2;

			graph[vertex1].push_back(vertex2);
			graph[vertex2].push_back(vertex1);
		}

		int f = 0;

		for (auto p : graph) {
			if (!visited[p.first]) {
				if (BFS(p.first)) {
					f = 1;
					break;
				}
			}
		}

		if (f)
			cout << "NO";
		else
			cout << "YES";
		cout << endl;

		memset(visited, false, sizeof(visited));
		memset(color, 0, sizeof(color));
		graph.clear();
	}
}
