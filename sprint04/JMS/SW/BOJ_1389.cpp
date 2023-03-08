#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <cstring>
#include <queue>

using namespace std;

set<int> vertice;
map<int, vector<int>> adjacenyList;
map<int, int> kebin;
int N, M;
bool visited[101];

typedef struct Info {
	int vertice, dis;
}Info;

void Input() {
	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		int vertice1, vertice2;

		cin >> vertice1 >> vertice2;
		vertice.insert(vertice1);
		vertice.insert(vertice2);

		adjacenyList[vertice1].push_back(vertice2);
		adjacenyList[vertice2].push_back(vertice1);
	}
}

void BFS(Info originvertice) {
	queue<Info> q;

	q.push(originvertice);
	visited[originvertice.vertice] = true;

	while (!q.empty()) {
		Info vertice = q.front();
		q.pop();

		for (auto p : adjacenyList[vertice.vertice]) {
			if (!visited[p]) {
				kebin[originvertice.vertice] += vertice.dis + 1;
				q.push({ p, vertice.dis + 1 });
				visited[p] = true;
			}
		}
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	Input();

	for (auto p : vertice) {
		memset(visited, false, sizeof(visited));
		BFS({ p,0 });
	}

	int mincnt = 500001, minindex = 101;

	for (auto p : kebin) {
		if (p.second < mincnt) {
			mincnt = p.second;
			minindex = p.first;
		}
	}

	cout << minindex;
}
