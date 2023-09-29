import pandas as pd
import numpy as np

num=np.random.RandomState(100)
numseries=pd.Series(num.normal(10,4,20))


pfinal=np.percentile(numseries,q=[0,25,50,75,100])
print(pfinal)
