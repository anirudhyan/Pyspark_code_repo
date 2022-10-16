from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///Spark_Course/ml-100k/u.data")
ratings = lines.map(lambda x: x.split()[2])  # creates a new rdd and this is transformation
result = ratings.countByValue()               # this is an action and it returns a normal python object {dictionary}
print(type(result))


sortedResults = collections.OrderedDict(sorted(result.items()))
print(type(sortedResults))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
