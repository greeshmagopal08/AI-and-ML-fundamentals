import pandas as pd
import numpy as np

data1=pd.read_excel("/Users/anandramesh/Downloads/dataA.xlsx")

data1.head()

data1.mean()

data1.corr()

data1.cov()

data2=pd.read_excel("/Users/anandramesh/Downloads/dataB.xlsx")

data2.head()

data2.mean()

data2.corr()

data2.cov()

#Question 3#

datacova=pd.read_excel("/Users/anandramesh/Downloads/covarianceA.xlsx")
datacova=np.array(datacova)

datacova=np.array([[3.757918233,0.177423199,0.344860372],
[0.177423199,3.03085632,0.126411838],
[0.344860372,0.126411838,3.333493692]])

datameana=np.array([0.499055727,1.013085008,0.718697756])

newmatrix= np.random.multivariate_normal(datameana,datacova,500)
newmatrix

newmatrix.mean(axis=0)

#With the same mean and covariance we cannot create the same dataset.#