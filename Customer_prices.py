# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:46:17 2022

@author: anirudhya n
"""

from pyspark import SparkConf , SparkContext
conf = SparkConf().setMaster("local").setAppName("Customer total amount")

sc = SparkContext(conf=conf)
input = sc.textFile("file:///Spark_Course/customer-orders.csv")

cust_item_map = input.map(lambda x :(int(x.split(",")[0]),float(x.split(",")[2])))

cust_price = cust_item_map.reduceByKey(lambda a,b : a+b)
cust_price_sorted = cust_price.sortByKey()

for i in cust_price_sorted.collect():
    cust_id = i[0]
    price = i[1]
    print("The customer id {} has purchased for {} dollars".format(cust_id,price))
    

 