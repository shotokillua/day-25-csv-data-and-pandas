# with open("weather_data.csv") as data_file:
#     data = data_file.read()
#     data_list = data.split("\n")
#     print(data_list)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# average = data["temp"].mean()
# print(average)
# max = data["temp"].max()
# print(max)

#print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# temp_c = monday.temp
# print(temp_c)
# temp_f = (9/5) * temp_c + 32
# print(temp_f)

# # Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = squirrel_data["Primary Fur Color"]
red = 0
black = 0
gray = 0

for color in colors:
    if color == "Cinnamon":
        red += 1
    elif color == "Black":
        black += 1
    else:
        gray += 1

# print(red)
# print(black)
# print(gray)

squirrel_data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}
final_data_frame = pandas.DataFrame(squirrel_data_dict)
final_data_frame.to_csv("squirrel_count.csv")
