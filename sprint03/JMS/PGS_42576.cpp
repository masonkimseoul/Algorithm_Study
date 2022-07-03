#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for(int i=0;i<completion.size();i++){
        if(completion[i].compare(participant[i]) != 0){
            answer = participant[i];
            return answer;
        }
    }
    
    answer = participant[participant.size()-1];
    return answer;
}
