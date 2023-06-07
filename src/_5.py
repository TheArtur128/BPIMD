fruit = input("Enter fruit: ").strip().lower()

if fruit not in ("apple", "orange", "banana"):
    input(
        "! Unsupported fruit name"
        "\nEnter something to exit\n"
    )
    exit()

color = input("Enter fruit color: ")

if color not in ("red", "green", "yellow"):
    input(
        "! Unsupported fruit color"
        "\nEnter something to exit\n"
    )
    exit()

if fruit in ("orange", "banana") and color != "yellow":
    input(
        f"! {fruit.capitalize()} can't be {color}"
        "\nEnter something to exit\n"
    )
    exit()

input(
    f"|> A {color} {fruit}"
    "\nEnter something to exit\n"
)
exit()
