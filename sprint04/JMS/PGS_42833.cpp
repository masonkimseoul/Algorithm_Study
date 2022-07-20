#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "", temp = "";
    int i=0,j=k;
    
    while(i < k && j > 0){
        int max = -1, maxindex= -1;
        
        for(int q=i;q<j+i+1;q++){
            if(max < number[q]){
                max = number[q];
                maxindex = q;
            }
        }
        
        temp = number.substr(0, i);
        temp += number.substr(maxindex);
        j = j - maxindex + i;
        i++;
        number = temp;
    }
    
    if(j>0)
        number = number.substr(0, number.length() - j);
    
    return number;
}
