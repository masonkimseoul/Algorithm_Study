#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	int arr[300], sum[300][2] = { 0 };

	cin >> N;
	for (int i = 0;i < N;i++)
		cin >> arr[i];

	sum[0][0] = arr[0];
	sum[1][0] = arr[1];
	sum[1][1] = arr[0] + arr[1];

	for (int i = 2;i < N;i++) {
		sum[i][0] = max(sum[i - 2][0], sum[i - 2][1]) + arr[i];
		sum[i][1] = sum[i - 1][0] + arr[i];
	}

	cout << max(sum[N - 1][0], sum[N - 1][1]);
}
