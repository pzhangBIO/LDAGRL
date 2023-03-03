from numpy import *
import numpy as np
import random
import math
import os
import time
import pandas as pd
import csv
import math
import random
import copy

# 定义函数
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])      # 转换数据类型
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

AllNode = []
ReadMyCsv(AllNode, 'AllNode.csv')

FinalLncFeatureNum = []
ReadMyCsv(FinalLncFeatureNum, 'FinalLncFeatureNum.csv')

FinalDiseaseFeatureNum = []
ReadMyCsv(FinalDiseaseFeatureNum, 'FinalDiseaseFeatureNum.csv')

# 生成AllNodebridge
counterP = 0
while counterP < 5:
    LineEmbeddingName = 'vec_all' + str(counterP) + '.txt'
    LineEmbedding = np.loadtxt(LineEmbeddingName, dtype=str, skiprows=1)

    # bridge
    AllNodeBridgeNum = []
    counter = 0
    while counter < len(AllNode):
        pair = []
        counter1 = 0
        while counter1 < len(LineEmbedding[0]) - 1:        # 如果节点孤立，则Feature全为0
            pair.append(0)
            counter1 = counter1 + 1
        AllNodeBridgeNum.append(pair)
        counter = counter + 1

    # bridge
    counter = 0
    while counter < len(LineEmbedding):
        num = int(LineEmbedding[counter][0])
        AllNodeBridgeNum[num] = list(LineEmbedding[counter][1:])
        counter = counter + 1

    print(np.array(AllNodeBridgeNum).shape)
    AllNodeBridgeNumName = 'AllNodeMannerNum' + str(counterP) + '.csv'
    StorFile(AllNodeMannerNum, AllNodeMannerNumName)


    num1 = 0
    # 将lnc和disease的feature加入Bridge中，[Bridge,lnc/disease]
    counter = 0
    while counter < len(FinalLncFeatureNum):
        AllNodeBridgeNum[int(FinalLncFeatureNum[counter][0])].extend(FinalLncFeatureNum[counter][1:])
        num1 = num1 + 1
        counter = counter + 1
    print(num1)

    num2 = 0
    counter = 0
    while counter < len(FinalDiseaseFeatureNum):
        AllNodeBridgeNum[int(FinalDiseaseFeatureNum[counter][0])].extend(FinalDiseaseFeatureNum[counter][1:])
        num2 = num2 + 1
        counter = counter + 1
    print(num2)

    print(np.array(AllNodeBridgeNum).shape)
    AllNodeFeatureNumName = 'AllNodeAttributeBridgeNum' + str(counterP) + '.csv'
    StorFile(AllNodeBridgeNum, AllNodeFeatureNumName)

    counterP = counterP + 1


