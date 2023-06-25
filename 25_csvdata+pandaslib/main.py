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

# data = pandas.read_csv(r"25_csvdata+pandaslib\weather_data.csv")
# print(data["temp"])

# a whole table in pandas is a DATA FRAME, a column is a SERIES

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(data_list)

# using pandas func
# print(data["temp"].mean())
# print(data["temp"].max())

# calling a series/column
# print(data["condition"])
# print(data.condition)

# printing a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# priting a selected column from a selected row
# print((data[data.temp == data.temp.max()]).condition)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Arunya", "Anilansh", "Nitin"],
#     "scores": [95, 92, 80]
# }
# data = pandas.DataFrame(data_dict)

# # put data into a csv file
# data.to_csv("25_csvdata+pandaslib/new_data.csv")

data = pandas.read_csv(r"25_csvdata+pandaslib\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "fur color": ["grey", "red", "black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("25_csvdata+pandaslib/Squirrel_Count.csv")