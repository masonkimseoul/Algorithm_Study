#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int arr[100000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int answer = 1000000000, maxlength = 0, sumlength = 0;

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		maxlength = max(maxlength, arr[i]);
		sumlength += arr[i];
	}

	int left = maxlength, right = sumlength, mid, m = 0;
	while (left <= right) {
		mid = (left + right) / 2;
		m = 1;
		int tempSumLength = 0;

		for (int i = 0; i < N; i++) {
			if (m > M)
				break;
			if (tempSumLength + arr[i] > mid) {
				m++;
				tempSumLength = 0;
			}
			tempSumLength += arr[i];
		}

		if (m <= M) right = mid - 1;
		else left = mid + 1;
	}

	cout << left;
}
