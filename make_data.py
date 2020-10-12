# %%
import pandas as pd
import numpy as np
indf = pd.read_csv('../res_table.csv',index_col=[0])
indf.head()
indf.index.name = 'Gene_acc'
indf.rename({'desc':'Desc'},axis=1,inplace=True)
indf=indf[['Gene_id','srank','Intensity','FDR','Desc']]
indf=indf[indf['Intensity']>0]
indf['Intensity']=np.log10(indf['Intensity'])
indf.describe()
# %%
indf.to_csv('res_table.csv')

# %%
import os
cwd = os.getcwd()
cwd
# %%
import pandas as pd
import numpy as np
indf = pd.read_csv('../res_table.csv',index_col=[0])
indf.head()

# %%
maxquant = pd.read_csv('../raw/combined/txt/proteinGroups.txt',sep='\t')
maxquant['Fasta headers']
desc_col = []
Protein_IDs = []

# %%
for gene_id in indf['Gene_id']:
    desc = ''
    for headers in maxquant['Fasta headers']:
        if gene_id in str(headers):
            desc+=headers
    desc = desc.replace(',',' ')
    desc_col.append(desc)
indf['desc2'] =  desc_col

for gene_id in indf['Gene_id']:
    desc = ''
    for headers in maxquant['Protein IDs']:
        if gene_id in str(headers):
            desc+=headers
    desc = desc.replace(',',' ')
    Protein_IDs.append(desc)
indf['ids2'] =  Protein_IDs       

# %%
indf.head()
# %%
indf.index.name = 'Gene_acc'
indf.rename({'desc':'Desc'},axis=1,inplace=True)
indf=indf[['Gene_id','srank','Intensity','FDR','Desc','desc2','ids2']]
indf=indf[indf['Intensity']>0]
indf['Intensity']=np.log10(indf['Intensity'])
indf.describe()
# %%
indf.to_csv('res_table2.csv')
# %%
