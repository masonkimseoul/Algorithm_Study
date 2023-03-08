#include <iostream>

using namespace std;

int arr[20], N, S, cnt = 0;

void InputArr() {
	for (int i = 0; i < N; i++)
		cin >> arr[i];
}

void RecurFindSubSet(int index, int sum) {
	for (int i = index; i < N; i++) {
		if (sum + arr[i] == S)
			cnt++;

		RecurFindSubSet(i + 1, sum + arr[i]);
	}
}

void FindSubSet() {
	for (int i = 0; i < N; i++) {
		if (arr[i] == S)
			cnt++;
		RecurFindSubSet(i + 1, arr[i]);
	}
}

int main() {
	cin >> N >> S;
	InputArr();
	FindSubSet();
	cout << cnt;
}
