#coding=utf-8
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("final_an.csv")

dataset.tail()

x=np.array(dataset)

# feature normalization (feature scaling)
X_scaler = StandardScaler()
x = X_scaler.fit_transform(x)

# PCA
pca = PCA(n_components=0.98)# 保证降维后的数据保持90%的信息
pca.fit(x)
pca.transform(x)

newX=pca.fit_transform(x)   #降维后的数据
print(pca.explained_variance_ratio_)  #输出贡献率
print(newX) #输出降维后的数据

np.savetxt('new.csv', newX, delimiter = ',')
