from pyspark import SparkContext, SparkConf


sc = SparkContext(master='local[2]', appName='First Spark App')
data = sc.textFile(r'data\UserPurchaseHistory.csv').map(lambda line: line.split(','))
# .map(lambda record: (record[0], record[1], record[2]))
print(data.collect())
numPurchase = data.count()
uniqueUsers = data.map(lambda record: record[0]).distinct().count()
totalRevenue = data.map(lambda record: float(record[2])).sum()
products = data.map(lambda record: (record[1], 1.0)).reduceByKey(lambda a, b: a + b).collect()
mostPopular = sorted(products, key=lambda x: x[1], reverse=True)[0][0]

print('totalPurchase is: %d' %(numPurchase))
print('userNum is: %d' %(uniqueUsers))
print('totalRevenue is: %d' %(totalRevenue))
print('mostPopular product is: %s' %(mostPopular))
