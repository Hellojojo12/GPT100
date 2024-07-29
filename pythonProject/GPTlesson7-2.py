"""
废了，接口调用的方式不一样了
"""

from openai.embeddings_utils import get_embeddings
import openai, os, tiktoken, backoff
import pandas as pd  # 加上 pandas 的导入
from secure import *


openai.api_key = OPENAI_API_KEY
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
batch_size = 2000
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191

# 修改文件路径为新的路径
df = pd.read_csv('data/20_newsgroup.csv')

print("Number of rows before null filtering:", len(df))
df = df[df['text'].isnull() == False]
encoding = tiktoken.get_encoding(embedding_encoding)

df["n_tokens"] = df.text.apply(lambda x: len(encoding.encode(x)))
print("Number of rows before token number filtering:", len(df))
df = df[df.n_tokens <= max_tokens]
print("Number of rows data used:", len(df))
