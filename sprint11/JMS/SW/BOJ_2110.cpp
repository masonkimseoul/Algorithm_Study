#include <iostream>
#include <algorithm>

using namespace std;

int N, c;
int arr[200000];
bool isSurplus = false;

bool IsCorrect(int distance) {
	bool success = true;


	if (success) return true;
	else return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int maxDistnace = 0;

	cin >> N >> c;
	for (int i = 0; i < N; i++)	cin >> arr[i];
	sort(arr, arr + N);

	int left = 1, right = arr[N - 1] - arr[0], mid;
	while (left <= right) {
		mid = (left + right) / 2;
		int cnt = 1, prePosition = 0;

		for (int j = 1; j < N; j++) {
			if (cnt > c) break;
			if (arr[j] - arr[prePosition] > mid) {
				cnt++;
				prePosition = j;
			}
		}

		if (cnt < c) right = mid - 1;
		else left = mid + 1;
	}

	cout << left;
}
