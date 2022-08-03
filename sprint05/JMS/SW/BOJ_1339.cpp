#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int alpha[26] = { 0 };
vector<string> v;
int n;

bool Compare(int A, int B) {
	if (A > B)
		return true;
	else
		return false;
}

void Input() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		string str;

		cin >> str;
		v.push_back(str);
	}
}

void Solution() {
	for (auto p : v) {
		int pownum = 0;

		for (int j = p.length() - 1; j >= 0; j--)
			alpha[p[j] - 'A'] += pow(10, pownum++);
	}

	sort(alpha, alpha + 26, Compare);

	int sum = 0, num = 9;
	for (auto p : alpha)
		sum += p * num--;

	cout << sum;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	Input();
	Solution();
}
