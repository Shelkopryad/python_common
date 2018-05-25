import pandas as pd
import numpy as np

## series example
s = pd.Series(np.arange(1,15,2))
print(s)
indx = s.index
print(indx)
print(s[s > 5])

x = s[s > 5] * 6
print(x)
