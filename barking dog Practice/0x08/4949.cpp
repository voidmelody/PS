//
// Created by 소승수 on 10/18/23.
//
#include <bits/stdc++.h>

using namespace std;

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(0);

    while(true){
        string input;
        getline(cin, input);
        stack<char> st;
        bool flag = true;
        int index = 0;

        if(input.length() == 1 && input[0] == '.')
            break;

        while(input[index] != '.'){
            char c = input[index];
            if(c == '(' || c == '[')
                st.push(c);
            else if(c == ')'){
                if(!st.empty() && st.top() == '(') st.pop();
                else flag = false;
            }else if(c == ']'){
                if(!st.empty() && st.top() == '[') st.pop();
                else flag = false;
            }
            index++;
        }
        if(st.empty() && flag)
            cout <<"yes\n";
        else
            cout <<"no\n";
    }
}