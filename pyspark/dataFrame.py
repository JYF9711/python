from pyspark.sql import Row
from pyspark import SparkContext
from pyspark.sql import SparkSession
import pandas as pd

spark=SparkSession.builder.appName("rddDataFrame").master("local[*]").getOrCreate()
#读取数据
book=spark.read.text('file:///opt/text/python/pyspark/book.txt')
#转化Rdd
book_rdd=book.rdd.map(lambda x:x[0].split(",")).map(lambda x:Row(id=x[0],name=x[1],rating=x[2],price=x[3],publish=x[4],rul=x[5]))
#创建dataFrame
book_df=spark.createDataFrame(book_rdd)
book_df.select(book_df['id'],book_df['name'],book_df['rating']-1).show()
#pandas
book_pds=book_df.groupBy('publish').count()
book_pds=book_pds.toPandas()
ax=book_pds.head(n=10).plot(x='publish',y=['count'],kind='bar',title='book count of publish')
print(ax)
