def valid(email, password):
    if not isinstance(email, str):
        return "invalid email"
    if "@" not in email:
        return "invalid email"
    if not isinstance(password, str):
        return "invalid password"
    if len(password) < 8:
        return "invalid password"
    if len(password.isdigit) < 1:
        return "invalid password"
    if password.isupper < 1:
        return "invalid password"
    print("accepted")
    return valid.__dict__
print(valid("ejjsef@", "daddsfsfD2sf"))