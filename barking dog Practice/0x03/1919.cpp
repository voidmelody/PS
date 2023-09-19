//
// Created by 소승수 on 2023/09/19.
//
#include <bits/stdc++.h>
using namespace std;

int arr1[26];
int arr2[26];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int count = 0;
    string a, b;
    cin >> a >> b;

    for(char c : a){
        arr1[c-'a']++;
    }
    for(char c : b){
        arr2[c-'a']++;
    }

    for(int i = 0; i < 26; i++){
        int minimum = min(arr1[i], arr2[i]);
        int maximum = max(arr1[i], arr2[i]);
        count += (maximum - minimum);
    }

    cout << count;
}

