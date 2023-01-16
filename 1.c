#include<stdio.h>
void main()
{
        int t,n,i,j,cnt=0,cnt1=0,b;
        scanf("%d",&t);
        while(t!=0)
        {
			cnt1=0;
            t = t - 1;
            scanf("%d",&n);
            int a[n];
            for(i = 0 ; i < n ;i++)
            {
                scanf("%d",&a[i]);
            }
            for (i = 0; i < n; ++i)
            {
                for (j = i + 1; j < n; ++j)
                {
                    if (a[i] > a[j])
                    {
                        b = a[i];
                        a[i] = a[j];
                        a[j] = b;
                    }
                }
            }
            for(i = 0; i < n ; i++)
            {  
                cnt = 0;
                for(j = i; j < n; j++) 
                {    
                    if(a[i]==a[j])
                    {
            
                            cnt++;
                            if(cnt==3)
                            {
                                printf("%d\n",a[i]);
                                cnt1 = 1 ;
                                break;
                            }
                    }  
                }
                if(cnt1==1)
                {
                    break;
                }
            }
            if(cnt1 == 0 )
            {
                printf("-1\n");
            }
            
        }
}