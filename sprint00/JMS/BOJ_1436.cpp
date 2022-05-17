#include <iostream>

using namespace std;

int Find666(int N) {
	int i = 666, cnt = 0, temp, sixcount = 0;

	while(1) {
		temp = i;
		sixcount = 0;
		while (temp >= 6) {
			if (temp % 10 == 6)
				sixcount++;
			else
				sixcount = 0;

			if (sixcount == 3) {
				cnt++;
				break;
			}
			temp /= 10;
		}

		if (cnt == N)
			return i;
		i++;
	}
}

int main() {
	int N;

	cin >> N;
	cout << Find666(N);
}
