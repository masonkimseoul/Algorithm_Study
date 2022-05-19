#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

set<string> resultset;
set<string>::iterator iter;
vector<char> arr;
char result[15];
int L, S;

void InputArr() {
	for (int i = 0; i < S; i++) {
		char temp;

		cin >> temp;
		arr.push_back(temp);
	}

	sort(arr.begin(), arr.end());
}

void PrintResult() {
	for (iter = resultset.begin(); iter != resultset.end(); iter++) {
		cout << *iter << endl; // 최소 한 개의 모음 + 최소 2개의 자음
	}
}

void RecurFind(int index, int subcnt) {
	for (int i = index; i < S; i++) {
		result[subcnt] = arr[i];

		if (subcnt == L - 1) {
			resultset.insert(result);
			subcnt--;
		}

		RecurFind(i + 1, subcnt + 1);
	}
}

void FindPassword() {
	for (int i = 0; i <= S - L; i++) {
		result[0] = arr[i];

		RecurFind(i + 1, 1);
	}
}

int main() {
	cin >> L >> S;
	InputArr();
	FindPassword();
	PrintResult();
}
