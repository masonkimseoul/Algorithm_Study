#include <string>
#include <cstring>
#include <vector>

using namespace std;

int mincnt = 51, f = 0;

int CountCompare(string A, string B) {
    int temp = 0;

    for (int i = 0; i < A.length(); i++) {
        if (A[i] == B[i])
            temp++;
    }

    return temp;
}

void RecurFind(int index, vector<string> words, string target, int cnt, int visited[]) {
    visited[index] = 1;
    cnt++;

    if (words[index].compare(target) == 0) {
        f = 1;
        if (mincnt > cnt)
            mincnt = cnt;
    }
    else {
        for (int i = 0; i < words.size(); i++) {
            if (!visited[i] && CountCompare(words[i], words[index]) == words[i].length() - 1)
                RecurFind(i, words, target, cnt, visited);
        }
    }

    visited[index] = 0;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int visited[50];

    for (int i = 0; i < words.size(); i++) {
        if (CountCompare(words[i], begin) == begin.length() - 1) {
            memset(visited, 0, sizeof(visited));
            f = 0;

            RecurFind(i, words, target, 0, visited);

            if (f)
                answer = mincnt;
        }
    }

    return answer;
}
