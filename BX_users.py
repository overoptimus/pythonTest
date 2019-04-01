from pyspark import SparkConf, SparkContext, SparkFiles

PATH = r'F:\dataSet\BX-CSV-Dump'

sc = SparkContext(master='local[2]', appName='BX_users Spark App')
data = sc.textFile(PATH + '\BX_Users.csv')
