#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int opercnt[4], tempcnt[4] = { 0 };
int arr[100];
vector<int> v, ans;

int SubCalculate(int a, int b, int c) {
	switch (c)
	{
	case 0:
		return a + b;
	case 1:
		return a - b;
	case 2:
		return a * b;
	case 3:
		return a / b;
	default:
		return 0;
	}
}

void Calculate() {
	int sum = SubCalculate(arr[0], arr[1], v[0]);

	for (int i = 1; i < N - 1; i++) sum = SubCalculate(sum, arr[i + 1], v[i]);

	ans.push_back(sum);
}

void RSolution() {
	if (v.size() == N - 1) {
		Calculate();
		return;
	}

	for (int i = 0; i < 4; i++) {
		if (tempcnt[i] < opercnt[i]) {
			tempcnt[i]++;
			v.push_back(i);
			RSolution();
			tempcnt[i]--;
			v.pop_back();
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
