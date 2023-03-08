#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	long long K, N, right = 0, mid, left = 1, cnt = 0, result = 0;
	long long arr[10001];

	cin >> K >> N;
	for (int i = 0; i < K; i++) {
		cin >> arr[i];
		right = max(right, arr[i]);
	}

	mid = (left + right) / 2;
	while (left <= right) {
		mid = (left + right) / 2;
		cnt = 0;

		for (int i = 0; i < K; i++)
			cnt += arr[i] / mid;

		if (cnt >= N) {
			left = mid + 1;
			result = result > mid ? result : mid;
		}
		else
			right = mid - 1;
	}

	cout << result;
}
