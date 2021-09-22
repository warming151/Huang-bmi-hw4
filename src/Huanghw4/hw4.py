import numpy as np
import pandas as pd
import scanpy as sc

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import scipy as sp

import h5py



from matplotlib import rcParams
from matplotlib import cm

sc.settings.verbosity = 3             # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_header()
sc.settings.set_figure_params(dpi=80, facecolor='white')


def unsupervised_umap():
    adata = sc.read_10x_mtx(
        './filtered_gene_bc_matrices/hg19/',  # the directory with the `.mtx` file
        var_names='gene_symbols',                # use gene symbols for the variable names (variables-axis index)
        cache=True)      

    adata.var_names_make_unique()

    #sc.pl.highest_expr_genes(adata, n_top=20, )

    sc.pp.filter_cells(adata, min_genes=100)
    sc.pp.filter_genes(adata, min_cells=3)

    adata.var['mt'] = adata.var_names.str.startswith('MT-')  # annotate the group of mitochondrial genes as 'mt'
    sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)


    #sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
    #             jitter=0.4, multi_panel=True)
    #sc.pl.scatter(adata, x='total_counts', y='pct_counts_mt')
    #sc.pl.scatter(adata, x='total_counts', y='n_genes_by_counts')

    adata = adata[adata.obs.n_genes_by_counts < 2500, :]
    adata = adata[adata.obs.pct_counts_mt < 5, :]

    sc.pp.normalize_total(adata, target_sum=1e4)


    sc.pp.log1p(adata)

    sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)

    #sc.pl.highly_variable_genes(adata)

    sc.pp.regress_out(adata, ['total_counts', 'pct_counts_mt'])

    sc.pp.scale(adata, max_value=10)


    # In[18]:


    sc.tl.pca(adata, svd_solver='arpack')


    #sc.pl.pca_variance_ratio(adata, log=True)



    sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)


    sc.tl.umap(adata)

    # sc.tl.leiden(adata)

    sc.pl.umap(adata,  save='Huang.pdf')
    print("umap plot has saved")






