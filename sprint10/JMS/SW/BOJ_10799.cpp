#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string str;
	vector<int> v;
	int sum = 0;

	cin >> str;

	for (int i = 0; i < str.length();i++) {
		if (str[i] == '(') {
			if (str[i + 1] == ')') {
				for (int i = 0; i < v.size(); i++)
					v[i]++;
				i++;
			}
			else
				v.push_back(0);
		}
		else {
			sum += v[v.size() - 1] + 1;
			v.pop_back();
		}
	}

	cout << sum;
}
