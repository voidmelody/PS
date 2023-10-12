//
// Created by 소승수 on 10/12/23.
//

#include <bits/stdc++.h>
using namespace std;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    deque<int> dq;
    int count = 0;
    int e;
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        dq.push_back(i);
    }

    while(m--){
        cin >> e;
        int left, right;

        for(int i = 0; i < dq.size(); i++){
            if(dq[i] == e){
                left = i;
                right = dq.size() - i;
                break;
            }
        }

        if(left <= right){
            while(dq.front() != e){
                dq.push_back(dq.front());
                dq.pop_front();
                count++;
            }
            dq.pop_front();
        }else{
            while(dq.back() != e){
                dq.push_front(dq.back());
                dq.pop_back();
                count++;
            }
            dq.pop_back();
            count++; // 타깃도 맨 앞으로 옮겨줘야 하므로.
        }
    }
    cout << count;
}