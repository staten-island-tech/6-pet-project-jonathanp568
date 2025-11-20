def valid(email, password):
    if not isinstance(email, str) or not isinstance(password, str):
        return "invalid email/password, not a string"
    if "@" not in email:
        return "invalid email, no @"
    if len(password) < 8:
        return "invalid password, not 8 characters long"
    if not any(ch.isdigit() for ch in password):
        return "invalid password, no number"
    if not any(ch.isupper() for ch in password):
        return "invalid password, no uppercase letters"
    print(email, password)
    return "accepted"
print(valid("ejjsef@", "jsdgiueoAii1"))