#include <iostream>
#include <stack>
#include <map>
#include <vector>

using namespace std;

int N;
int arr[1000001], ans[1000001], cnt[1000001] = { 0 };
map<int, int> m;
stack<int> s;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		cnt[arr[i]]++;
	}

	for (int i = N - 1; i >= 0; i--) {
		while (!s.empty() && cnt[s.top()] <= cnt[arr[i]])
			s.pop();

		if (s.empty())
			ans[i] = -1;
		else
			ans[i] = s.top();

		s.push(arr[i]);
	}

	for (int i = 0; i < N; i++)
		cout << ans[i] << ' ';
}
