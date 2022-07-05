# numbers = [1,2,3,4,5]
# new_list = [n + 1 for n in numbers ]
# print(new_list)

# range_lsit =[ num * 2 for num in range(0,5)]
# print(range_lsit)

# names = ["Rohan ", "alex" , "rijin",  "bomb"]
# new_names = [n for n in names if len(n) <= 4]
# print(new_names)

# new_names = [n.upper() for n in names if len(n) <= 5]
# print(new_names)
# import random
# name_score = {n:random.randint(1,100) for n in names}
# print(name_score)
# names_passed = {n:scores for (n, scores) in name_score.items() if scores >= 60 }
# print(names_passed)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {n: weather * 9/5 + 32 for (n,weather) in weather_c.items()}

print(weather_f)
