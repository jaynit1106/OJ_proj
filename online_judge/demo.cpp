#include <bits/stdc++.h>



using namespace std;



#define ull unsigned long long



#define ll long long



#define ft first



#define sd second



#define rep(a,n) for(ll int i=a;i<n;i++)



#define pb push_back



#define all(t) t.begin(),t.end()



#define nline "\n"



#define vi vector<ll int>



#define vs vector<string>



#define pi pair<ll int,ll int>



void pv(vector<ll int>v){for(auto itr :v)cout<<itr<<" ";}



void p2d(vector<vector<ll int>>v){for(auto itr :v){for(auto itr1:itr)cout<<itr1<<" ";cout<<nline;}}



void printpair(vector<pair<ll int,ll int>>v){for(auto itr : v)cout<<itr.ft<<" "<<itr.sd<<nline;}



void printmap(map<ll int,ll int>m){for(auto itr :m)cout<<itr.ft<<" "<<itr.sd<<nline;}



void printstringvector(vector<string>v){for(auto itr :v)cout<<itr<<" ";cout<<nline;}



ll int modmul(ll int a,ll int b,ll int mod){return((a%mod)*(b%mod))%mod;}



ll int mod=1000000007;



ll int solve(){



ll int n;



cin>>n;



vector<ll int> v;



rep(0,n){



ll int x;



cin>>x;



v.pb(x);



}



sort(all(v));



pv(v);



return 0;



}



int main(){



ios_base::sync_with_stdio(0);



cin.tie(0);



cout.tie(0);



ll int t;



// cin>>t;



t=1;



// cout<<t;



while(t--){



solve();



}



return 0;



}