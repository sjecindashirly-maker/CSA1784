# Decision Tree Implementation

def decision_tree(weather, humidity):
    if weather == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    elif weather == "Overcast":
        return "Yes"
    elif weather == "Rain":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    else:
        return "Invalid Input"

weather = input("Enter Weather (Sunny/Overcast/Rain): ")
humidity = input("Enter Humidity (High/Normal): ")

result = decision_tree(weather, humidity)

print("Play Tennis:", result)
