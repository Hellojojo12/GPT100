"""
运行成功，下载到了data
"""

import os
from sklearn.datasets import fetch_20newsgroups
import pandas as pd


def twenty_newsgroup_to_csv(filepath):
    newsgroups_train = fetch_20newsgroups(
        subset='train', remove=('headers', 'footers', 'quotes'))

    df = pd.DataFrame([newsgroups_train.data, newsgroups_train.target.tolist()]).T
    df.columns = ['text', 'target']

    targets = pd.DataFrame(newsgroups_train.target_names, columns=['title'])

    out = pd.merge(df, targets, left_on='target', right_index=True)
    # out.to_csv('20_newsgroup.csv', index=False)
    out.to_csv(filepath, index=False)


directory = 'data'
filename = '20_newsgroup.csv'
filepath = os.path.join(directory, filename)

os.makedirs(directory, exist_ok=True)

twenty_newsgroup_to_csv(filepath)

