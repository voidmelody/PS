//
// Created by 소승수 on 2023/09/13.
//
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

   int arr[5];
   int sum = 0;
   for(int i = 0; i < 5; i++){
       cin >> arr[i];
       sum += arr[i];
   }

   sort(arr, arr+5);

   int average = sum / 5;
   int middle = arr[2];
   cout << average << '\n' << middle;
}

