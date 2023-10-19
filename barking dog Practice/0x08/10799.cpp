//
// Created by 소승수 on 10/18/23.
//
#include <bits/stdc++.h>

using namespace std;

int main(){
    cin.tie(nullptr);
    cout.tie(nullptr);
    ios::sync_with_stdio(false);

    stack<char> st;
    int ans = 0;
    string input;
    cin >> input;
    for(int i = 0; i < input.length(); i++){
        if(input[i] == '(')
            st.push(input[i]);
        else{
            if(input[i-1] == '('){
                st.pop();
                ans += st.size();
            }else{
                st.pop();
                ans++;
            }
        }
    }
    cout << ans;
}