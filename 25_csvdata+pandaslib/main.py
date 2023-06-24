# with open("25_csvdata+pandaslib\weather_data.csv") as data_file:
#     data_list = data_file.readlines()
#     for i in range(len(data_list)):
#         data_list[i] = data_list[i].strip()
#     print(data_list)

# import csv

# with open(r"25_csvdata+pandaslib\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)
    
import pandas

data = pandas.read_csv(r"25_csvdata+pandaslib\weather_data.csv")
# print(data["temp"])

# a whole table in pandas is a DATA FRAME, a column is a SERIES

data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)