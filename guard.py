def valid(email, password):
    if not isinstance(email, str):
        return "invalid email, not a string"
    if "@" not in email:
        return "invalid email, no @"
    if not isinstance(password, str):
        return "invalid password, not a string"
    if len(password) < 8:
        return "invalid password, not 8 characters long"
    if password.isdigit() < 1:
        return "invalid password, no number"
    if password.isupper() < 1:
        return "invalid password, no uppercase letters"
    print(valid.__dict__)
    return "accepted"
print(valid("ejjsef@", "daddsf22sf"))