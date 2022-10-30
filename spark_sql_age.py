# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:31:24 2022

@author: anirudhya n
"""

from pyspark.sql import SparkSession 

spark = SparkSession.builder.appName("avg_no_of_frnds_by_age").master("local[3]").getOrCreate()

people = spark.read.option("header","True").option("inferSchema","true")\
    .csv("file:///Spark_Course/fakefriends-header.csv" )
print("The input dataframe")
people.show()

print("input schema")
people.printSchema()

age_by_frnds = people.groupBy("age").avg("friends")
print("the friends by age is")
age_by_frnds.show()

'''print("writing output to a file")

age_by_frnds.write.csv()

'''
    
    