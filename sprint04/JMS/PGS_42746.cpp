#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>

using namespace std;

bool Compare(string &a, string &b){
    if(a+b > b+a)
        return true;
    return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    
    for(auto p : numbers)
        v.push_back(to_string(p));
    
    sort(v.begin(), v.end(), Compare);
    
    if(v[0] == "0")
        return "0";
    
    for(auto p : v)
        answer += p;
    
    return answer;
}
