import pandas as pd
import numpy as np


def loadData(data): # !! it makes first col to row name !!
  df = pd.read_csv(data)
  df = df.set_index('0')

  return df



def getTimeStep(df): # columns to list
  inputList = list(map(int, df.columns.tolist()))
  return inputList



def oneDayIs48(inputList): # detect days which is not 48 timeStep 
                           # and return {day:timeStep} dictionary
  oneDay = 24 * 2 # 24h x 30min
  day = 195
  dayList = []
  tempDic = {}
  for i in range(len(inputList)):
    dayList.append(inputList[i]//100)
  while True:
    if dayList.count(day) != oneDay:
      tempDic[day] = dayList.count(day)
    day += 1
    if day == 731:
      break

  return tempDic


def countOmit(df): # sum(count NAN)
  return sum(df.isnull().sum())



def observe(df,customer,day): # return a day of customer
  dayList = []
  usage = []
  inputList = getTimeStep(df)
  TorF = False
  for i in range(len(inputList)):
    temp = inputList[i]//100
    if temp==day:
      TorF = True
      dayList.append(inputList[i])
      usage.append(df.loc[customer][i])
    elif TorF == True: break

  df = pd.DataFrame(np.array(usage)).transpose()
  df.columns = dayList
  df.index = [customer]
  return df


def findNAN(df):
  inputList = getTimeStep(df)
  NANcolumn = []
    
  for i in range(len(inputList)):
    if df[str(inputList[i])].isnull().values.any()==True:
      NANcolumn.append(inputList[i])

  return NANcolumn


def testFunc(number): # toyCode for testing
  if number<0:
    raise ValueError
  return ("even" if number%2==0 else "odd")