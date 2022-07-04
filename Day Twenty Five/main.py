# import csv
# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)
    
from numpy import average
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

# data_dict=  data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list)/len(temp_list)
# print(int(average))
# print(data["temp"].mean())
# print(data["temp"].max())

print(data [data.day=="Monday"])
print(data[data.temp==data.temp.max()])