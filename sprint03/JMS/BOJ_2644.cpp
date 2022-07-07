#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int n, m, find1, find2, result;
int hier[101] = { 0 };
vector<int> fam[101];

void Input() {
	cin >> n;
	cin >> find1 >> find2;
	cin >> m;

	for (int i = 0; i < m; i++) {
		int temp1, temp2;

		cin >> temp1 >> temp2;
		fam[temp1].push_back(temp2);
		fam[temp2].push_back(temp1);
	}
}

int BFS(int a, int b) {
	queue<int> q;

	q.push(a);
	hier[a] = 0;

	while (!q.empty()) {
		int index = q.front();
		q.pop();

		if (index == b)
			return hier[index];

		for (auto p : fam[index]) {
			if (!hier[p]) {
				hier[p] = hier[index] + 1;
				q.push(p);
			}
		}
	}

	return -1;
}

int main() {
	Input();

	cout << BFS(find1, find2);
}
