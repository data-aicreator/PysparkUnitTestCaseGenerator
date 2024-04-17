
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Create a Spark session
spark = SparkSession.builder \
    .appName("Customer Transactions") \
    .getOrCreate()

# Read the CSV file containing customer transactions
# Adjust the file path to match your dataset location
file_path = "path/to/customer_transactions.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Calculate the total transaction amount for each customer
customer_totals = df.groupBy("customer_id").agg(sum("transaction_amount").alias("total_amount"))

# Display the total transaction amount for each customer
customer_totals.show()

# Stop the Spark session
spark.stop()
