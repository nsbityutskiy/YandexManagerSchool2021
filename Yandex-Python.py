# нам не сказано, что должна возвращать программа
# но пускай для удобства она возвращает булевые значения
def validatepassword(password):
    # Проверим, что программе подали на ввод строку, а не что-то другое. Ведь если там какое-либо число, пароль всё равно будет неверным.
    if type(password) == str:
        # будем проверять пароль пошагово - в мультипоточности смысла нет
        if len(password) > 6:
            if sum(i.isdigit() for i in password) >= 1:
                if sum(i.isupper() for i in password) >= 1:
                    if sum(i.islower() for i in password) >= 1:
                        if password.isalnum():
                            if len(set(password)) == len(password):
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

    # будем проверять пароль пошагово - в мультипоточности смысла нет
