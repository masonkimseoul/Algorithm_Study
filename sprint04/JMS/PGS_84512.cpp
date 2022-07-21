#include <string>
#include <vector>

using namespace std;

string alpha[5] = {"A", "E", "I", "O", "U"};

bool IsEqual(string word, string temp){
    if(temp.compare(word) == 0)
        return true;
    else
        return false;
}

int solution(string word) {
    int answer = 1;
    
    for(int i=0;i<5;i++, answer++){
        string temp = alpha[i];
        if(IsEqual(word, temp))
            return answer;
        
        for(int j=0;j<5;j++){
            answer++;
            string temp1 = temp+alpha[j];
            if(IsEqual(word, temp1))
                return answer;
            
            for(int k=0;k<5;k++){
                answer++;
                string temp2 = temp1 + alpha[k];
                if(IsEqual(word, temp2))
                    return answer;
                
                for(int l=0;l<5;l++){
                    answer++;
                    string temp3= temp2 + alpha[l];
                    if(IsEqual(word, temp3))
                        return answer;
                    
                    for(int q=0;q<5;q++){
                        answer++;
                        string temp4 = temp3+alpha[q];
                        if(IsEqual(word, temp4))
                            return answer;
                    }
                }
            }
        }
    }
}
