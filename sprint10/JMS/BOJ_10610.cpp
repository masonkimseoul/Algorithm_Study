#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string str;
	vector<int> v;
	int sum = 0;

	cin >> str;

	for (int i = 0; i < str.length(); i++) {
		v.push_back(str[i] - '0');
		sum += v[i];
	}

	sort(v.begin(), v.end(), greater<int>());

	if (sum % 3 != 0 || v[v.size()-1] != 0)
		cout << -1;
	else {
		string temp;
		for (auto p : v)
			temp += p + '0';
		cout << temp;
	}
}
