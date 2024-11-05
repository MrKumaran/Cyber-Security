def hasInvalidCharacters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    for i in string:
        if i not in valid:
            return True
    return False


def isValid(mail):
    if mail.count("@") == 1:
        usr_name = mail.split("@")
        if len(usr_name[0]) == 0:
            return False
        else:
            if hasInvalidCharacters(usr_name[0]):
                return False
            elif usr_name[1].count(".") == 1:
                domain = usr_name[1].split(".")
                if len(domain[0]) == 0:
                    return False
                else:
                    if len(domain[1]) == 0:
                        return False
                    else:
                        if hasInvalidCharacters(domain[0]):
                            return False
                        elif hasInvalidCharacters(domain[1]):
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    email = input("Enter your email: ")
    print(isValid(email.lower()))