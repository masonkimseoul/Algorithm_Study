#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> answer;
int visited[10001] = {0};

bool DFS(string dest, vector<vector<string>> tickets){
    answer.push_back(dest);
    
    for(int i=0;i<tickets.size();i++){
        if(!visited[i] && !tickets[i][0].compare(dest)){
            visited[i]  = 1;
            if(DFS(tickets[i][1], tickets))
                return true;
            else
                visited[i] = 0;
        }
    }
    
    if(answer.size() - 1 == tickets.size())
        return true;
    else{
        answer.pop_back();
        return false;
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    
    DFS("ICN", tickets);
    
    return answer;
}
