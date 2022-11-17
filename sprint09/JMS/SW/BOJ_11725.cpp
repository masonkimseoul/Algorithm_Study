#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	map<int, vector<int>> m;

	int n;
	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int num1, num2;
		cin >> num1 >> num2;
		m[num1].push_back(num2);
		m[num2].push_back(num1);
	}

	bool visited[100001] = {false};
	int arr[100001];
	queue<int> q;

	q.push(1);
	visited[1] = true;

	while (!q.empty())
	{
		int current = q.front();
		q.pop();

		for (auto p : m[current]) {
			if (!visited[p]) {
				q.push(p);
				visited[p] = true;
				arr[p] = current;
			}
		}
	}

	for (int i = 2; i <= n; i++)
		cout << arr[i] << '\n';
}
