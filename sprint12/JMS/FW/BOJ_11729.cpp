#include <iostream>

using namespace std;

int N;

void Hanoi(int n, int start, int mid, int dest) {
	if (n == 1) {
		cout << start << ' ' << dest << '\n';
		return;
	}

	Hanoi(n - 1, start, dest, mid);
	cout << start << ' ' << dest << '\n';
	Hanoi(n - 1, mid, start, dest);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	
	cout << (1 << N) - 1 << '\n';
	Hanoi(N, 1, 2, 3);
}
