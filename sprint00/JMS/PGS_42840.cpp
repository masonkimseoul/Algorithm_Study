#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    int answerpat1[5] = { 1,2,3,4,5 }, answerpat2[8] = { 2,1,2,3,2,4,2,5 }, answerpat3[10] = { 3,3,1,1,2,2,4,4,5,5 },
        cntanswer[3] = { 0 };

    for (int i = 0; i < answers.size(); i++) {
        int correct = answers[i];

        if (correct == answerpat1[i % 5])
            cntanswer[0]++;
        if (correct == answerpat2[i % 8])
            cntanswer[1]++;
        if (correct == answerpat3[i % 10])
            cntanswer[2]++;
    }

    vector<int> answer;
    int answermax = max({ cntanswer[0],cntanswer[1],cntanswer[2] });
        
    for (int i = 0; i < 3; i++) {
        if (answermax == cntanswer[i])
            answer.push_back(i + 1);
    }

    return answer;
}

int main() {
    vector<int> answers, result;

    answers.push_back(1);
    answers.push_back(2);
    answers.push_back(3);
    answers.push_back(4);
    answers.push_back(5);

    result = solution(answers);

    for (int i = 0; i < result.size(); i++)
        cout << result[i] << " ";

}
