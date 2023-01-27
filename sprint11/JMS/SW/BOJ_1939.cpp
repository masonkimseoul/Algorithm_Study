#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int N, M, x , y;
vector<pair<int, int>> vertice[10001];
int maxWeight = 0;
bool visited[10001] = { false };

#define MAX 1000000000

bool Compare(pair<int, int> a, pair<int, int> b) {
	if (a.second == b.second) return a.first <= b.first;
	else return	a.second <= b.second;
}

bool BFS(int mid) {
	queue<int> q;

	q.push(x);
	visited[x] = true;

	while (!q.empty()) {
		int current = q.front();

		q.pop();

		if (current == y) return true;

		for (auto p : vertice[current]) {
			if (!visited[p.first] && p.second >= mid) {
				q.push(p.first);
				visited[p.first] = true;
			}
		}
	}

	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int maxWeight = 0;

	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int a, b, c;
		
		cin >> a >> b >> c;

		maxWeight = max(maxWeight, c);

		vertice[a].push_back(make_pair(b, c));
		vertice[b].push_back(make_pair(a, c));
	}
	cin >> x >> y;

	int left = 1, right = maxWeight, mid;
	while (left <= right) {
		mid = (left + right) / 2;
		memset(visited, false, sizeof(visited));

		if (BFS(mid)) left = mid + 1;
		else right = mid - 1;
	}

	cout << right;
}
