#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

vector<int> connected[100];
bool visited[100];

bool Compare(vector<int> &v1, vector<int> &v2){
    if(v1[2] > v2[2])
        return false;
    return true;
}

bool DFS(int index, int b){
    visited[index] = true;
    
    if(index == b)
        return true;
    
    for(auto p : connected[index]){
        if(!visited[p])
            if(DFS(p, b))
                return true;
    }
    
    return false;
        
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    sort(costs.begin(), costs.end(), Compare);
    
    for(auto p : costs){
        memset(visited, false, sizeof(visited));
        if(!DFS(p[0], p[1])){
            answer += p[2];
            
            connected[p[0]].push_back(p[1]);
            connected[p[1]].push_back(p[0]);
        }
    }
    
    return answer;
}
