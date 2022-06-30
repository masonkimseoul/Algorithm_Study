#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> answer;
int visited[10001] = {0};

void DFS(int index, vector<vector<string>> tickets){
    answer.push_back(tickets[index][1]);
    
    for(int i=0;i<tickets.size();i++){
        if(!visited[i] && !tickets[i][0].compare(tickets[index][1])){
            visited[index] = 1;
            visited[i] = 1;
            DFS(i, tickets);
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    
    for(int i=0;i<tickets.size();i++){
        if(!tickets[i][0].compare("ICN")){
            answer.push_back("ICN");
            DFS(i, tickets);
            break;
        }
    }
    
    
    return answer;
}
