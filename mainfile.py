from trees import *
from treePlotter import *
# 测试
myDat,labels=createDataSet()
shannon=calcShannonEnt(myDat)
# print("shannon is " +str(shannon))
a=chooseBestFeatureToSplit(myDat)
# print(labels)
# print("The best Feature is "+str(a))

# 测试树
myTree=createTree(myDat,labels)
print(myTree)
# myTree=retrieveTree(0)
# print(myTree)
# testlabel=classify(myTree,labels,[1,0])
# print(testlabel)
#绘制树
# myTree=retrieveTree(0)
# createPlot(myTree)

#隐形眼镜测试
# fr=open('lenses.txt')
# lenses=[inst.strip().split('\t') for inst in fr.readlines()]
# lensesLabels=['age','prescript','astigmatic','tearRate']
# lensesTree=createTree(lenses,lensesLabels)
# createPlot(lensesTree)
