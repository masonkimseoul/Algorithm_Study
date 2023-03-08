#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	int arr[100][100];
	vector<int> v[100];

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
			if (arr[i][j])
				v[i].push_back(j);
		}
	}

	queue<int> q;
	bool visited[100] = { false };
	int result[100][100] = { 0 };

	for (int i = 0; i < n; i++) {
		q.push(i);
		visited[i] = true;
		while (!q.empty()) {
			int current = q.front();
			q.pop();

			for (auto p : v[current]) {
				result[i][p] = 1;
				if (!visited[p]) {
					visited[p] = true;
					q.push(p);
				}
			}
		}
		
		memset(visited, false, sizeof(visited));
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cout << result[i][j] << ' ';
		cout << '\n';
	}
}
