#include<bits/stdc++.h>
using namespace std;

int Bsearch(int l , int r , long x, long a[]){
    while(l <= r){
        int mid = (r+l)/2;
        if (a[mid] == x){
            return mid;
        }
        else if (a[mid] < x) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}

void solve(int n, long k, long a[]){
    if (k == 0){
        for(int i = 0; i < n; i++){
            if (a[i] == 0){
            	cout<<"YES";
                return;
            }
        }
        cout<<"NO";
        return;
    }
        
    for(int i = 1; i < n; i++) {
        a[i] += a[i-1];
	}

    for(int i = 0; i < n; i++){
        if (a[i] - k == 0){
            cout<<"YES";
            return;
        }
        if ( a[i] - k > 0){
            int indez = Bsearch(0 , n - 1, a[i] - k, a);
        	if (indez != -1){
                cout<<"YES";
                return;
            }
        }
    }
    cout<<"NO";

}

int main() {    
    int t;
    cin>>t;
    while (t--) {
        int n;
        cin>>n;
        long k;
        cin>>k;
        long a[n];
        for (int i = 0; i < n; i++) {
            cin>>a[i];
        }
        solve(n, k, a); 
        cout<<endl;
    }
    return 0;
}

/*
3
6 33
1 4 20 3 10 5
7 7
1 4 0 0 3 10 5
2 0
1 4
*/