# from re import M
# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("brown2","blue2")
# timmy.forward(100)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.align="l"
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["fire","water","wind"])
table.align="l"
print(table)