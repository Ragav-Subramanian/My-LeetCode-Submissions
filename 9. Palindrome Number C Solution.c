bool isPalindrome(long long int x){ 
    if(x<0) 
       { 
        return false; }
    else 
        { 
       long long int a=x,r=0; 
        while(a>0) 
            { 
            r=(r*10)+a%10; 
            a/=10; 
            } 
        if( r==x) 
            { 
            return true; 
            } 
        else 
            { 
            return false; 
        }
}
}

