#include <iostream>
#include <deque>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string str;
	int num = 0;
	deque<int> nd;
	deque<char> cd;

	cin >> str;

	for (auto p : str) {
		if (p >= '0' && p <= '9')
			num = num * 10 + p - '0';
		else {
			nd.push_back(num);
			num = 0;
			cd.push_back(p);
		}
	}
	nd.push_back(num);

	for (int i = 0; i < cd.size();i++) {
		if (cd[i] == '+') {
			int temp = nd[0] + nd[1];
			nd.pop_front();
			nd.pop_front();
			nd.push_front(temp);
		}
		else {
			int j = 2, temp = nd[1];

			while (i + 1 < cd.size() && cd[i + 1] == '+') {
				temp += nd[j++];
				i++;
			}
			temp = -1 * temp + nd[0];

			nd.erase(nd.begin(), nd.begin() + j);
			nd.push_front(temp);
		}
	}

	cout << nd[0];
}
