usernames = list()

def enter_username(username_description: str) -> None:
    name = input(f"Enter {username_description} username: ")
    usernames.append(name)
    print(f">> {name}")

enter_username("first")
enter_username("second")
enter_username("third")

print(f"All users: {', '.join(usernames)}")
