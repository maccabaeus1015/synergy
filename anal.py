import numpy as np
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA

data = np.loadtxt('data')

# まず時間の情報を抜く
new_data = np.delete(data, 0, axis=1)
print(new_data)

# for i in range(239):
#     a[i] = data[0,:]
# listではなく、npaddrayとして扱う

shape = (240, 33)
array = np.zeros(shape)

# a(t)に分類していく
for i in range(239):
    array[i, :] = new_data[i, :]
    
# clasify a(t) to  

    
nmf = NMF(n_components=2) # instance
nmf.fit(x)
