"""
运行正常
"""

from sklearn.metrics import PrecisionRecallDisplay
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from GPTlesson2 import cosine_similarity, get_embedding

EMBEDDING_MODEL = "text-embedding-ada-002"

datafile_path = "data/fine_food_reviews_with_embeddings_1k.csv"

df = pd.read_csv(datafile_path)
df["embedding"] = df.embedding.apply(eval).apply(np.array)
df = df[df.Score != 3]
df["sentiment"] = df.Score.replace({1: "negative", 2: "negative", 4: "positive", 5: "positive"})


def evaluate_embeddings_approach(labels=['negative', 'positive'], model='EMBEDDING_MODEL'):
    label_embeddings = [get_embedding(label, model=EMBEDDING_MODEL) for label in labels]

    def label_score(review_embedding, label_embeddings):
        return cosine_similarity(review_embedding, label_embeddings[1]) - cosine_similarity(review_embedding,
                                                                                            label_embeddings[
                                                                                                0])  # 计算每个评论的概率分数

    probas = df["embedding"].apply(lambda x: label_score(x, label_embeddings))
    # 根据概率分数确定预测标签
    preds = probas.apply(lambda x: 'positive' if x > 0 else 'negative')
    # 生成并打印分类报告
    report = classification_report(df.sentiment, preds)
    print(report)
    # 绘制精准-召回曲线
    display = PrecisionRecallDisplay.from_predictions(df.sentiment, probas, pos_label='positive')
    _ = display.ax_.set_title("2-class Precision-Recall curve")


# 调用函数进行评估
evaluate_embeddings_approach(
    labels=['An Amazon review with a negative sentiment.', 'An Amazon review with a positive sentiment.'])
