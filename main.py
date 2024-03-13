
def main():
    def tryAdd():
        num1 = 10
        num2 = 23
        try:
            print(num1 + num2)
        except:
            print("You encountered an error.")

    # tryToAdd()
    
    def errTryAdd():
        apple_price = 0.49
        banana_price = "0.79"
        # print(apple_price + banana_price)
        try:
            print(apple_price + banana_price)
        except TypeError:
            print("You can't add integers/floats to a string using arithmetic.")

    # errTryAdd()

    def usingTryFinally():
        people = ["Jake", "Kelly", "Reggie", "Chayenne"]
        try:
            print(f"Before: {people}")
            people.append("Kyleigh")
            print(f"After: {people}")
        except:
            print("You encountered an error.")
        finally:
            print("Everything went according to plan.")

    # usingTryFinally()
    
    def multiTry():
        file_name = "index.html"
        try:
            demo_file = open(file_name, 'w')
            try:
                demo_file.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>First step to Web Dev with Python!</h1>
</body>
</html>
""")
            except:
                print("Something went wrong when writing to the file")
            finally:
                demo_file.close()
                print(f"Go check your {file_name}")
        except:
            print("Something went wrong when opening the file")
    
    multiTry()


if __name__ == "__main__":
    main()