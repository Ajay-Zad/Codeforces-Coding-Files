import numpy as n
import pandas as p
d = {'Name':['A','B','C'],
     'Exam':['Sem1','Sem2','Sem3'],
     'Subject':['Maths','Science','English'],
     'result':['pass','pass','pass']}
f = p.DataFrame(d,columns=['Name','Exam','Subject','result'])
print(f)
print()
a = p.crosstab([f.Subject,f.Exam],f.result,margins=True)
print(a)

import matplotlib.pyplot as p
import pylab as pl
x = [5,3,7,9,1,11,12,5,19,12,3,4]
y = [10,22,15,56,71,33,44,29,2,6,66,50]
p.scatter(x,y)
p.show()