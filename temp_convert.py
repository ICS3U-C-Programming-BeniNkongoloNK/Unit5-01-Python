def fahrenheit():
    print("Hello, let me convert the temperature to fahrenheit for you")
    temp_cel_str = input("What is the temperature in celcius: \n")
    try:
        temp_cel_float = float(temp_cel_str)
        answer = (temp_cel_float * 9 / 5) + 32
        print("{}".format(temp_cel_float) + " in fahrenheit is {}".format(answer))
    except Exception:
        print("That is not a number, try again")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
