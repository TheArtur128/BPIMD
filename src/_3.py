fruit = input('>> ')  # apple, orange, banana

if fruit not in ("apple", "orange", "banana"):
    input(
        "Fruit can only be an apple, orange or banana"
        "\nEnter something to exit"
        "\n"
    )
    exit()

color = input('>> ')  # red, green, yellow

if color not in ("red", "green", "yellow"):
    input(
        "Available colors: red, green, yellow"
        "\nEnter something to exit"
        "\n"
    )
    exit()

if fruit in ("orange", "banana") and color != "yellow":
    input(
        f"{fruit.capitalize()} can only be yellow"
        "\nEnter something to exit"
        "\n>> "
    )
    exit()

input(
    f"|> A {color} {fruit}"
    "\nEnter something to exit"
    "\n"
)
exit()
