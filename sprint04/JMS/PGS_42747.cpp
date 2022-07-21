#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int i(0);
    
    sort(citations.begin(), citations.end());

    for (i = 0; i < citations.size(); i++) {
        if (citations[i] >= citations.size() - i)
            return (citations.size() - i);
    }
}
