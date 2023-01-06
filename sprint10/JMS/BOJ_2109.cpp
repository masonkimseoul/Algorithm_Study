#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool Compare(pair<int,int> a, pair<int,int> b) {
	return a.first >= b.first;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	vector<pair<int, int>> v;
	bool visited[10001] = {false};

	cin >> N;

	for (int i = 0; i < N; i++) {
		int pay, day;
		cin >> pay >> day;
		v.push_back(make_pair(pay, day));
	}

	sort(v.begin(), v.end(), Compare);

	int sum = 0;
	for (int i = 0; i < N; i++) {
		for (int j = v[i].second; j >= 1; j--) {
			if (!visited[j]) {
				sum += v[i].first;
				visited[j] = true;
				break;
			}
		}
	}

	cout << sum;
}
