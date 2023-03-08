#include <iostream>
#include <map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	map<int, int> m;

	int N, M;
	
	cin >> N;

	for (int i = 0;i < N;i++) {
		int num;
		cin >> num;
		m[num]++;
	}

	cin >> M;
	for (int i = 0;i < M;i++) {
		int num;
		cin >> num;
		cout << m[num] << " ";
	}
}

