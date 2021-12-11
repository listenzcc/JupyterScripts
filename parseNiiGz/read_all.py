
'''
FileName: read_all.py
Author: Chuncheng
Version: V0.0
Purpose: Read all nii.gz files
'''

# %%
import os
import numpy as np
import pandas as pd
import nibabel as nib

# %%


def read_niigz(filename):
    print(f'Read {filename}')
    img = nib.load(filename)

    # The img has the shape of (1974, 1, 83), and there are totally 163842 numbers
    # The counting is as the same as the lh-fsaverage template's 163842 vertex
    # Beware that the img is of the type of nibabel.nifti1.Nifti1Image
    print('-----------------------------------------------------------')
    print(type(img), img.shape, np.prod(img.shape))

    # -- %%
    # The data in array format
    data = img.get_fdata()
    print('-----------------------------------------------------------')
    print(data.shape, np.max(data), np.min(data))

    # -- %%
    # The header, there are so many keys ...
    hdr = img.header
    print('-----------------------------------------------------------')
    print('\n'.join(['| {:20s} | {} '.format(e, hdr[e]) for e in hdr]))
    print('-----------------------------------------------------------')

    return data


# %%
for name in [e for e in os.listdir() if e.endswith('nii.gz')]:
    data = read_niigz(name)
    df = pd.DataFrame(data.squeeze())
    df.to_csv(f'{name}.csv')


# %%
