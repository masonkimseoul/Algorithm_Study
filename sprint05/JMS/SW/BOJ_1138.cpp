#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int arr[10];
vector<int> v;

void Input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		v.push_back(i);
	}
}

void Solution() {
	do {
		vector<int> permutationV(v);

		int f = 0;

		for (int i = 0; i < permutationV.size(); i++) {
			int cnt = 0;

			for (int j = 0; j < i; j++) {
				if (permutationV[i] < permutationV[j])
					cnt++;
			}

			if (cnt != arr[permutationV[i]]) {
				f = 0;
				break;
			}
			f = 1;
		}

		if (f) {
			for (auto q : permutationV)
				cout << q + 1 << " ";
			break;
		}
	} while (next_permutation(v.begin(), v.end()));
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	Input();
	Solution();
}
