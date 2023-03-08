#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, cnt = 0, maxstart = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;

	vector<pair<int, int>> v;
	for (int i = 0; i < N; i++) {
		int start, end;
		cin >> start >> end;
		v.push_back(make_pair(end, start));
	}
	sort(v.begin(), v.end());

	int time = v[0].first;
	cnt++;
	for (int i = 1; i < N; i++) {
		if (v[i].second >= time) {
			time = v[i].first;
			cnt++;
		}
	}

	cout << cnt;
}
