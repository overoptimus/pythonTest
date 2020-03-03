from pyspark import SparkContext
from matplotlib.pyplot import hist
import matplotlib
import sys

sc = SparkContext(master='local[2]', appName='second spark app')
data = sc.textFile(r'..\dataSet\BX-CSV-Dump\BX-Users.csv')
head = data.first()
# print(head)
data_filter = data.filter(lambda line: line != head).map(lambda record: record.split(';')).filter(lambda record: len(record)==3)
data_age = data_filter.map(lambda record: record[2])
ages = data_age.filter(lambda record: record!='NULL').map(lambda record: int(eval(record))).collect()
print(ages, sep=' ', end='\n', file=sys.stdout, flush=False)
hist(ages, bins=40, density=True, color='lightblue')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 10)
# isinstance(222, int)
