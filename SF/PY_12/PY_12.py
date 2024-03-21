import pandas as pd
import numpy as np
import os

# def concat_user_files(path):
#     dfs = []
#     files = os.listdir(path)
#     sorted_files = sorted(files)
#     for file in sorted_files:
#         full_file_path = path + '/' + file
#         file_df = pd.read_csv(full_file_path, sep=',')
#         dfs.append(file_df)
#     con_df = pd.concat(dfs, ignore_index=True)
#     con_df = con_df.drop_duplicates(ignore_index=True)
#     return con_df


# print(concat_user_files(path = 'C:/Users/aoreshkin.IT-ONE/VSProject/SF_DS_PYTHON/SF/PY_10/data'))


# items_df = pd.DataFrame({
#     'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
#     'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
#     'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
# })

# purchase_df = pd.DataFrame({
#     'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
#     'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
#     'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
# })


# merged = items_df.merge(
#     purchase_df,
#     on='item_id',
#     how='inner'
# )

# income = sum(merged['stock_count']*merged['price'])
# income2 = (merged['stock_count']*merged['price']).sum()


