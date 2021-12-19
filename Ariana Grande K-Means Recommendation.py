#!/usr/bin/env python
# coding: utf-8

# In[76]:


pip install spotipy


# In[77]:


from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale


# In[78]:


df = pd.read_csv('/Users/ragave/Downloads/arianagrande_spotify.csv')
df.head()


# In[79]:


# creating a copy of the dataset
df_cluster = df.copy()
df_cluster = df_cluster.iloc[:300]


# In[80]:


# creating a dataframe without the categorical features
# do not include unnamed, name, album, artist, release_date, and length
X = df_cluster.iloc[:, [6,7,8,9,10,11,12,13,14,15,16]].values


# In[130]:


df.columns


# In[81]:


print(X.shape)
df_cluster.head()


# In[82]:


# finding out the proper number of clusters
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.savefig('Elbow_Method.png')
plt.show()


# In[85]:


# data preprocessing
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


# In[86]:


scaled = scaler.fit_transform(X)


# In[87]:


# instantiating model
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(scaled)


# In[88]:


from mpl_toolkits.mplot3d import Axes3D
# visualizing clusters
fig, ax = plt.subplots(figsize=(13,11))
ax = fig.add_subplot(111, projection='3d')
plt.scatter(scaled[y_kmeans == 0,0],scaled[y_kmeans == 0,1], s= 50, c= 'red',label= 'Cluster 1')
plt.scatter(scaled[y_kmeans == 1,0], scaled[y_kmeans == 1,1], s= 50, c= 'blue', label= 'Cluster 2')
plt.scatter(scaled[y_kmeans == 2,0], scaled[y_kmeans == 2,1], s= 50, c= 'green', label= 'Cluster 3')
plt.scatter(scaled[y_kmeans == 3,0], scaled[y_kmeans == 3,1], s= 50, c= 'cyan', label= 'Cluster 4')
plt.scatter(scaled[y_kmeans == 4,0], scaled[y_kmeans == 4,1], s= 50, c= 'magenta', label= 'Cluster 5')
# centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s= 300, c= 'yellow', label= 'Centroids')
plt.title('Clusters')
plt.legend()
plt.savefig('clusters.png')
plt.show()


# In[89]:


# predictions 
y_kmeans


# In[90]:


# converting preditcions into a df
kmeans = pd.DataFrame(data=y_kmeans, dtype=int)
kmeans.columns = ['k_cluster']

# predictions as a df
print(kmeans.shape)
kmeans.head()


# In[91]:


# concatenating the cluster column to the dataframe
df_cluster = pd.concat([df_cluster, kmeans], axis=1)

# checking the dataframe
print(df_cluster.shape)
df_cluster.head()


# In[92]:


# checking for null
(df_cluster.isnull().sum()/ df_cluster.shape[0]).sort_values(ascending=False)


# In[93]:


# popularity mean by cluster
df_cluster.groupby(['k_cluster']).popularity.mean().sort_values(ascending=False)


# In[94]:


# checking number of songs in each cluster
df_cluster['k_cluster'].value_counts()


# In[105]:


# checking the songs in the cluster
df_cluster.loc[df_cluster['k_cluster'] == 0]


# In[106]:


# checking the songs in the cluster
df_cluster.loc[df_cluster['k_cluster'] == 1]


# In[107]:


# checking the songs in the cluster
df_cluster.loc[df_cluster['k_cluster'] == 2]


# In[108]:


# checking the songs in the cluster
df_cluster.loc[df_cluster['k_cluster'] == 3][:10]


# In[109]:


# checking the songs in the cluster
df_cluster.loc[df_cluster['k_cluster'] == 4][:10]


# In[96]:


# statistical distribution of the data in each column, for each cluster
df_cluster.groupby("k_cluster").describe() 

