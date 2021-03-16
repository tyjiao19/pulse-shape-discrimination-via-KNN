import csv
import random

# read file
with open('new.csv', 'r')as file:
    reader = csv.DictReader(file)
    datas = [row for row in reader]

# K
K = 5

# regroup & shuffle
random.shuffle(datas)
n = len(datas) // 4

test_set = datas[1300:]
train_set = datas[0:1300]

# print(datas)
# print(test_set)


# KNN

# distance
def distance(d1, d2):
    res = 0

    for key in ( 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'):
        res += (float(d1[key]) + float(d2[key])) ** 2
    return res ** 0.5

def knn(data):
    # 1.distance
    res = [
        {"result": train['Rn'], "distance": distance(data, train)}
        for train in train_set
    ]
    #    print(res)

    # 2.ranking data
    res = sorted(res, key=lambda item: item['distance'])
    #    print(res)

    # 3.k of the nearest data
    res2 = res[0:K]
    #    print(res2)
    
    # 4.weighted mean
    result1 = {'1': 0, '0': 0}

    # 总距离
    dis = 0
    for r in res2:
        dis += r['distance']

    for r in res2:
        result1[r['result']] += 1 - r['distance'] / dis

    if result1['1'] > result1['0']:
        return '1'
    else:
        return '0'


# test
correct = 0
Ra = 0
Rn = 0
Ra2 = 0
Rn2 = 0

for test in test_set:
    result = test['Ra']
    result2 = knn(test)
    #    print(result,end=' ')
    #    print(result2)

    if result == '1':
        Ra += 1
    else:
        Rn += 1

    if result2 == '1':
        Ra2 += 1
    else:
        Rn2 += 1

    if result == result2:
        correct += 1

print("模型Rn:", Rn, "模型Ra:", Ra)
print("实际Rn:", Rn2, "实际Ra:", Ra2)

print("正确识别的信号数：", correct)
print("总信号数：", len(test_set))

print("准确率：{:.2f}%".format(100 * correct / len(test_set)))
