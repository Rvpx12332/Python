temperature = int(input("Enter the temperature in °C: "))

if temperature < 15:
    print("It is cold outside. Wear a jacket or pullover.")
elif temperature < 25:
    print("The weather is pleasant. Wear normal clothes.")
else:
    print("It is warm/hot. You can wear light and soft clothes.")
