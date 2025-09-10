# -*- coding: UTF-8 -*-
import gzip
import pickle

# 載入Model
with gzip.open('./api/model/xgboost-iris.pgz', 'rb') as f:
    xgboostModel = pickle.load(f)

# 從run取得input
def predict(input):
    pred=xgboostModel.predict(input)[0]
    print(pred)
    return pred