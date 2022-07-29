#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int maxday = 0;
    
    for(int i=0;i<progresses.size();i++){
        int amount = 100 - progresses[i];
        int day = amount / speeds[i];
        
        if(amount % speeds[i] > 0)
            day++;
        
        if(day > maxday){
            maxday = day;
            answer.push_back(1);
        }
        else
            answer[answer.size()-1]++;
    }
    
    return answer;
}
