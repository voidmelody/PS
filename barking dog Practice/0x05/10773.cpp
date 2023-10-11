//
// Created by 소승수 on 10/11/23.
//

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;
    int k, num;
    int sum = 0;
    cin >> k;
    while(k--){
        cin >> num;
        if(!num) s.pop();
        else s.push(num);
    }

    while(!s.empty()){
        sum += s.top();
        s.pop();
    }

    cout << sum;
}
