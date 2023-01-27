#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

double x, y, c;

double IsCorrect(double mid) {
	double h1 = sqrt(pow(x, 2) - pow(mid, 2));
	double h2 = sqrt(pow(y, 2) - pow(mid, 2));

	return h1 * h2 / (h1 + h2);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	cin >> x >> y >> c;

	double left = 0, right = min(x, y), mid;
	
	while (right - left > 0.000001) {
		mid = (left + right) / 2.0;

		if (IsCorrect(mid) >= c) left = mid;
		else right = mid;
	}

	cout << fixed;
	cout.precision(3);
	cout << left;
}
