#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

map<string, string> idMap;

vector<string> solution(vector<string> record) {
    vector<string> answer, tempanswer;
    
    for(auto p : record){
        stringstream ss(p);
        ss.str(p);
        string info[3];
        int i=0, infoindex=0;
        
        while(ss >> info[infoindex++]);
        
        if(info[0].compare("Enter") == 0){
            idMap[info[1]] = info[2];
            tempanswer.push_back("E" + info[1]);
        }
        else if(info[0].compare("Leave") == 0)
            tempanswer.push_back("L" + info[1]);
        else if(info[0].compare("Change") == 0)
            idMap[info[1]] = info[2];
    }
    
    for(auto p : tempanswer){
        if(p[0] == 'E'){
            string nickname  = idMap[p.substr(1)];
            answer.push_back(nickname.append("님이 들어왔습니다."));
        }
        else if(p[0] == 'L'){
            string nickname  = idMap[p.substr(1)];
            answer.push_back(nickname.append("님이 나갔습니다."));
        }
    }
    
    return answer;
}
