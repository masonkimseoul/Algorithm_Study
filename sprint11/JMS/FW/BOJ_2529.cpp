#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int k, f = 0;
vector<char> cv;
vector<vector<int>> ans;
bool visited[10] = { false };

bool IsCorrect(int a, int b, char c) {
	if (c == '<' && a < b)
		return true;
	else if (c == '>' && a > b)
		return true;
	return false;
}

void RSolution(vector<int> v) {
	if (v.size() == k + 1) {
		for (int i = 0; i < k; i++) {
			if (!IsCorrect(v[i], v[i + 1], cv[i]))
				return;
		}
		
		ans.push_back(v);
		return;
	}

	for (int i = 9; i >= 0; i--) {
		if (!visited[i]) {
			v.push_back(i);
			visited[i] = true;
			RSolution(v);
			v.pop_back();
			visited[i] = false;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> k;
	for (int i = 0; i < k; i++) {
		getchar();
		char c;
		cin >> c;
		cv.push_back(c);
	}

	vector<int> v;
	RSolution(v);
	sort(ans.begin(), ans.end());

	for (auto p : ans[ans.size() - 1])
		cout << p;
	cout << '\n';
	for (auto p : ans[0])
		cout << p;
}
