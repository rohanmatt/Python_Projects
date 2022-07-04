import pandas

data = pandas.read_csv("cp.csv")
grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_sq_count)
print(red_sq_count)
print(black_sq_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sq_count, red_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")