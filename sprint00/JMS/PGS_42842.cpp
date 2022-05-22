#include <string>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    float sqrt_yellow = sqrt(yellow);

    if (yellow == pow(sqrt_yellow, 2)) {
        answer.push_back((int)sqrt_yellow + 2);
        answer.push_back((int)sqrt_yellow + 2);
    }
    else {
        for (int i = (int)sqrt_yellow; i >= 1; i--) {
            if (yellow % i == 0) {
                int width = yellow / i + 2, height = i + 2;

                if (width * height == brown + yellow) {
                    answer.push_back(width);
                    answer.push_back(height);
                    break;
                }
            }
        }
    }

    return answer;
}

int main() {
    int a, b;

    cin >> a >> b;
    vector<int> sol = solution(a, b);

    cout << sol.front() << " " << sol.back();
}
