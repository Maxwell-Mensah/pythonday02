def my_division_modulo(first_number, oper_char, second_number):
    if oper_char=="/":
        try :
            res = first_number / second_number
            return res
        except Exception as e:
            print("Operation pas faisable:", e)
            return None
    elif oper_char=="%":
        try :
            res = first_number % second_number
            return res
        except Exception as e:
            print("Operation pas faisable:", e)
            return None
    else:
        print("The given arguments are not good")
        return None


print(my_division_modulo(2, '/', 4))