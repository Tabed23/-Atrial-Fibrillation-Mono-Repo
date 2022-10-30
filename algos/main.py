import numpy as np
import pandas as pd
import gzip

# compress numpy array file and export
f = gzip.GzipFile("compressed_npy.gz", "w")
ecg_arr = np.load('ecgeq-500hzsrfava.npy')
np.save(file=f, arr=ecg_arr)
f.close()

# read in the compressed numpy file
f = gzip.GzipFile('compressed_npy.gz', "r")
X = np.load(f)

# get 6428 layers, 700 rows and 12 columns
X = X[:,:700,:]
print(X.shape)

m,n,r = X.shape


out_arr = np.column_stack((np.repeat(np.arange(m),n),X.reshape(m*n,-1)))
out_df = pd.DataFrame(out_arr)


# rename columns and drop duplicates
out_df.columns= ['index', 'I', 'II', 'III', 'aVF', 'aVR', 'aVL', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']
out_df['index'] = out_df['index'].astype('int32')
out_df = out_df.drop_duplicates()


df = pd.read_csv('training_13_features.csv')
label_df = df.copy()
label_df['unique_id'] = np.arange(label_df.shape[0])


# merge out_df and label_df 
merged_df = pd.merge(out_df, label_df, how='inner', left_on='index', right_on='unique_id')
merged_df = merged_df.drop(columns=['index', 'unique_id'])



# dropna and reset index
new_mdf = merged_df.dropna()
new_mdf = new_mdf.reset_index(drop=True)
print(new_mdf)