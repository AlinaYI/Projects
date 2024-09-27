#decoupling
feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    #our feet_inches is string
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


res = convert(feet_inches)

if res < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide.")