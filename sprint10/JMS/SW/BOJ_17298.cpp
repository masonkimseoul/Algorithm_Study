#include <iostream>
#include <vector>
#include <stack>
#include <map>

using namespace std;

int N;
vector<int> v;
stack<int> s;
map<int, int> m;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		v.push_back(num);
	}

	m[N - 1] = -1;
	s.push(v[N - 1]);
	for (int i = N - 2; i >= 0; i--) {
		if (v[i] < v[i + 1])
			m[i] = v[i + 1];
		else {
			if (v[i] >= m[i + 1]) {
				m[i] = -1;
				while (!s.empty()) {
					int num = s.top();
					if (num > v[i]) {
						m[i] = num;
						break;
					}
					s.pop();
				}
			}
			else
				m[i] = m[i + 1];
		}
		
		s.push(v[i]);
	}

	for (int i = 0; i < N; i++)
		cout << m[i] << ' ';
}
