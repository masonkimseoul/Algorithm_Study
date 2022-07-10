#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<string, int> map;

int solution(vector<vector<string>> clothes) {
    int answer = 1;

    for(auto p : clothes)
        map[p[1]]++;

    for(auto p : map)
        answer *= (p.second + 1);
    
    return answer - 1;
}
