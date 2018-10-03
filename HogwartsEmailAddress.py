#include <bits/stdc++.h>
#include<string.h>
using namespace std;

string isValid(string email) {
    int len=email.length();
    int flag=0,i=0;
    if(len>5)
    for(i=0;i<5;i++){
        if((int)email.at(i)>95){
            continue;
        }
        else{
            flag=1;
            break;
        }
    }
    if(len!=18 || flag==1){
        return "No";
    }
    else{
        if(email.substr(5)=="@hogwarts.com"){
            return "Yes";
        }
        else{
            return "No";
        }
    }
    return 0;
}

int main() {
    string s;
    cin >> s;
    string result = isValid(s);
    cout << result << endl;
    return 0;
}
