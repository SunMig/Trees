from math import log
import operator

#计算香农熵
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)

    return  shannonEnt

def createDataSet():
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])#把抽取出该特征以后的所有特征组成一个列表
            retDataSet.append(reducedFeatVec) #创建抽取该特征以后的dataset
    return retDataSet
# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGain=0.0;bestFeature = -1
    for i in range(numFeatures):
        #将dataSet中的数据先按行依次放入example中，然后取得example中的example[i]元素放入featList中
        featList=[example[i] for example in dataSet]
        print(featList)
        uniqueVals=set(featList)# python的set是一个无序不重复元素集
        print(uniqueVals)
        newEntropy=0.0
        # 计算每一个属性值的熵,并求和
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i #返回最好的属性特征对应的地址
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
    # 利用opeator操作键值对排序的字典并返回出现次数最多的分类名称
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

# 创建树的函数
def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    # 这两个迭代终止条件是为了给下面的循环返回节点的数值
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)

    # 寻找最优的数据集划分方式
    bestFeat=chooseBestFeatureToSplit(dataSet)
    #拿到对应的标签
    bestFeatLabel=labels[bestFeat] #字符型
    myTree={bestFeatLabel:{}}
    del(labels[bestFeat]) #删除已经使用的标签
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)#列表转成集合，方便找到唯一值
    for value in uniqueVals:
        subLabels=labels[:] #复制一份，防止循环过程改变变量值
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
        print(myTree)
    return myTree