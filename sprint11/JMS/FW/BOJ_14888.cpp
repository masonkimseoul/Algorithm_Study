#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int arr[11];
char oper[4] = { '+','-','*','/' };
int opercnt[4];
int tempopercnt[4] = { 0 };
vector<int> ans;
vector<char> v;

int SubCalculate(int a, int b, char c) {
	switch (c)
	{
	case '+':
		return a + b;
	case '-':
		return a - b;
	case '*':
		return a * b;
	case '/':
		return a / b;
	default:
		return 0;
	}
}

int Calculate(vector<char> v) {
	int sum = SubCalculate(arr[0], arr[1], v[0]);

	for (int i = 1; i < N - 1; i++) sum = SubCalculate(sum, arr[i + 1], v[i]);

	return sum;
}

void RSolution() {
	if (v.size() == N - 1) {
		ans.push_back(Calculate(v));
		return;
	}

	for (int i = 0; i < 4; i++) {
		if (tempopercnt[i] < opercnt[i]) {
			v.push_back(oper[i]);
			tempopercnt[i]++;
			RSolution();
			v.pop_back();
			tempopercnt[i]--;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) cin >> arr[i];
	for (int i = 0; i < 4; i++) cin >> opercnt[i];

	RSolution();
	sort(ans.begin(), ans.end());

	cout << ans[ans.size() - 1] << '\n' << ans[0];
}
