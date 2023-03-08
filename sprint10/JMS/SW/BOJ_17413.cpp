#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<char> v;
stack<char> s;

void ClearStack() {
	while (!s.empty()) {
		v.push_back(s.top());
		s.pop();
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string str;
	getline(cin, str);

	int f = 0;

	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '<') {
			f = 1;
			ClearStack();
			v.push_back(str[i]);
		}
		else if (str[i] == '>') {
			f = 0;
			v.push_back(str[i]);
		}
		else {
			if (f)
				v.push_back(str[i]);
			else {
				if (str[i] == ' ') {
					ClearStack();
					v.push_back(str[i]);
				}
				else
					s.push(str[i]);
			}
		}
	}
	ClearStack();

	for (auto p : v)
		cout << p;
}
