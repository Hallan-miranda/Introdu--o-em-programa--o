c = float(input("What is the temperature ? "))
f = float(((9*c)/5) + 32)
scale = input("Fahrenheit or Celsius (F/C)? ")
temperature = 0
speed = 5

if scale.lower() == "c":
    temperature = f
elif scale.lower() == "f":
    temperature = c

while speed <= 60:
    windchil = 35.74 + (0.6215 * temperature) - (35.75 * (speed ** 0.16)) + (0.4275 * temperature * (speed ** 0.16))
    print(f"At temperature {temperature}°F, and wind speed {speed} mph, the windchill is: {round(windchil, 2)}F")
    speed = speed + 5