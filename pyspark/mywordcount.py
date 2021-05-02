from pyspark import SparkContext
sc = SparkContext( 'local', 'mywordcount')
textFile = sc.textFile("file:///opt/text/python/pyspark/data.txt")
wordCount = textFile.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a, b : a + b)
wordCount.collect()
wordCount.foreach(print)

