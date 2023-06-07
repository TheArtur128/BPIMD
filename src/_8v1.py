usernames = list()

name = input("Enter first username: ")
usernames.append(name)
print(f">> {name}")

name = input("Enter second username: ")
usernames.append(name)
print(f">> {name}")

name = input("Enter third username: ")
usernames.append(name)
print(f">> {name}")

print(f"All users: {', '.join(usernames)}")