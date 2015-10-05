#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;++k)
	{
		string s;
		cin>>s;
		string s1=s;
		bool ans=false;
		for(int i=0;i<s.size()-1;++i)
			if(s[i]<s[i+1])
				ans=true;
		if(!ans)
			cout<<"no answer"<<endl;
		else
		{
			next_permutation(s1.begin(),s1.end());
			cout<<s1<<endl;
		}
	}
}