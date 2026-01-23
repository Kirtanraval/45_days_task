cars = ["Toyota", "Honda", "Ford", "BMW"]
print(cars[1])
cars.append("Audi")
print("these are cars brands:", cars)

colors = ("Red", "Blue", "Green", "Yellow")
print(colors[2])

more_colors = list(colors)
more_colors.append("Purple")
print("these are colors:", more_colors)

my_info = {
    "name:" "RK",
    "age:" "22"
    "city:" "Vadodara"
}
for key, value in my_info.items():
    print(key, value)

