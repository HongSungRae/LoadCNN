import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from dataProcess import *

## eda로 정확히 뭘 할건지 생각을 해봅시다
# 1. 무작위 사용자 무작위로 7일 시퀀스하게 뽑아서 plot해보기
# 2. 결측치가 있는 곳의 열이름 관찰하기, plot 분명 어떤 규칙이 있을거라 생각
# 3. 7일씩 평균내서 계절성 살펴보기

class EDAplot():
    def __init__(self,df_csv):
        self.df = loadData(df_csv)
        print("=======>EDA plot<=======")

    def select(self,day_start,day_end): # select rd customer & rd-seq 7days
        np.random.seed(0)
        legth = len(self.df)
        index_cust = self.df.index
        rd_customer = index_cust[np.random.randint(low=0,high=len(index_cust))]
        while True:
            rd_day = np.random.randint(day_start,day_end+1) # test train val 모두에서 작동하게 만들려고 파라메타로 시작과 끝을 주었음
            if: # 시작일로부터 8일치가 안뽑히면 continue
                pass
            elif: # nan이 하나라도 있으면 continue
                pass
            else: break
        
        # rd_customer에 대해 rd_day포함 8일치의 데이터를 df로 뽑는다.
        return df_8days
    




a = EDAplot("df_timeSeries.csv")
print(a.select())
print('Done')