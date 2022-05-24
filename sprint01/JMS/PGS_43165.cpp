#include <string>
#include <vector>

using namespace std;

int cnt = 0;

void RecurSearch(vector<int> numbers, int target, int index, int sum) {
    if (index > numbers.size() - 1)
        return;

    if (index == numbers.size() - 1 && (sum + numbers[index] == target || sum - numbers[index] == target))
        cnt++;

    RecurSearch(numbers, target, index + 1, sum + numbers[index]);
    RecurSearch(numbers, target, index + 1, sum - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    RecurSearch(numbers, target, 0, 0);
    answer = cnt;

    return answer;
}
