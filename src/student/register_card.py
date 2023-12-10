import sys
sys.path.append("./src")

import student.student_frame_factory as sff
import exc.exceptions as exc
import gui.errorlabel as el
import main

def send_request(frame):
    """
    Sends a request to the database to register a card.

    :param frame: The frame object containing the card registration form.
    :type frame: Frame
    """
    
    if frame.warning != None:
        frame.warning.destroy()

    try:
        name = str(frame.name_entry.get())
        if frame.card_num_entry.get()[0] == "0":
            raise exc.LeftZeroError
        number = int(frame.card_num_entry.get())
        card_type = str(frame.clicked.get())
        date = str(frame.card_date_entry.get())
        cvv = int(frame.card_cvv_entry.get())

        has_errors(name, number, card_type, date, cvv)

        date = "20" + date[0:2] + "-" + date[3:5] + "-01"
        
        query = (f"UPDATE Card SET CardHolderName = \'{name}\'," +
                                 f"CardNum = \'{number}\'," +
                                 f"CardType = \'{card_type}\', " +
                                 f"ValidityDate = \'{date}\', " +
                                 f"CVV = \'{cvv}\' " + 
                                 f"WHERE IdUser = {main.System().user};")

        system = main.System()
        return_message = system.database.query(query)
        print(return_message)
        
        for frame in frame.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        sff.StudentFrameFactory.get_frame("ThankYouFrame", frame.window)
    
    except (exc.EmptyFieldError,
            exc.WrongTypeError,
            exc.NonLetterError,
            exc.WrongLengthError,
            exc.WrongFormatError,
            exc.InvalidCardTypeError,
            exc.LeftZeroError) as error: 
            frame.warning = el.ErrorLabel(frame, 
                                    str(error), 
                                    pos_x = 180, pos_y = 350,
                                    width=600, height=40)
            
    except (ValueError, TypeError) as error:
        frame.warning = el.ErrorLabel(frame, 
                                "Preencha todos os campos corretamente", 
                                pos_x = 180, pos_y = 350,
                                width=600, height=40)

""" Version 0.0.0: test_none_name - red
def has_errors(name, number, card_type, date, cvv):
    return False
"""

""" Version 0.0.1: test_none_name - green
def has_errors(name, number, card_type, date, cvv):
    if name == None:
        raise exc.EmptyFieldError("Nome")
"""

""" Version 0.0.1: test_empty_name - red
def has_errors(name, number, card_type, date, cvv):
    if name == None:
        raise exc.EmptyFieldError("Nome")
"""

""" Version 0.0.2: test_empty_name - green
def has_errors(name, number, card_type, date, cvv):
    if name == None:
        raise exc.EmptyFieldError("Nome")
    if name == "":
        raise exc.EmptyFieldError("Nome")
"""

""" Version 0.1.0: test_empty_name - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
"""

""" Version 0.1.0: test_wrong_name_type - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
"""

""" Version 0.1.1: test_wrong_name_type - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
"""

""" Version 0.1.1: test_name_contains_non_letters - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
"""

""" Version 0.1.2: test_name_contains_non_letters - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    for char in name:
        if not char.isalpha() and char != " ":
            raise exc.NonLetterError("Nome")
"""

""" Version 0.2.0: test_name_contains_non_letters - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
"""

""" Version 0.2.0: test_none_number - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
"""

""" Version 0.2.1: test_none_number - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None or number == "":
        raise exc.EmptyFieldError("Número do Cartão")
"""

""" Version 0.2.1: test_number_is_not_int - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None or number == "":
        raise exc.EmptyFieldError("Número do Cartão")
"""

""" Version 0.2.2: test_number_is_not_int - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None or number == "":
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
"""

""" Version 0.3.0: test_number_is_not_int - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
"""

""" Version 0.3.0: test_number_length_is_not_16 - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
"""

""" Version 0.3.1: test_number_length_is_not_16 - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
"""

""" Version 0.3.1: test_card_type_is_not_string - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
"""

""" Version 0.3.2: test_card_type_is_not_string - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
"""

""" Version 0.4.0: test_card_type_is_not_string - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
"""
    
""" Version 0.4.0: test_invalid_card_type - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
"""

""" Version 0.4.1: test_invalid_card_type - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    
    raise exc.InvalidCardTypeError(card_type)
"""

""" Version 0.5.0: test_invalid_card_type - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
"""

""" Version 0.5.0: test_date_is_not_string - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
"""

""" Version 0.5.1: test_date_is_not_string - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    raise exc.WrongTypeError("Data de Validade", str, type(date))
"""

""" Version 0.6.0: test_date_is_not_string - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
"""

""" Version 0.6.0: test_date_length_is_not_5 - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
"""

""" Version 0.6.1: test_date_length_is_not_5 - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    raise exc.WrongLengthError("Data de Validade", 5, len(date))
"""

""" Version 0.7.0: test_cvv_is_not_string - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
"""

""" Version 0.7.0: test_middle_date_slash_is_missing - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
"""

""" Version 0.7.1: test_middle_date_slash_is_missing - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    raise exc.WrongFormatError("Data de Validade")
"""

""" Version 0.8.0: test_middle_date_slash_is_missing - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
"""

""" Version 0.8.0: test_non_numerical_date - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
"""

""" Version 0.8.1: test_non_numerical_date - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
"""

""" Version 0.9.0: test_non_numerical_date - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
"""

""" Version 0.9.0: test_cvv_is_not_int - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
"""

""" Version 0.9.1: test_cvv_is_not_int - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
    
    raise exc.WrongTypeError("CVV", int, type(cvv))
"""

""" Version 1.0.0: test_cvv_is_not_int - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
    
    if type(cvv) != int:
        raise exc.WrongTypeError("CVV", int, type(cvv))
"""

""" Version 1.0.0: test_cvv_length_is_not_3 - red
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
    
    if type(cvv) != int:
        raise exc.WrongTypeError("CVV", int, type(cvv))
"""

""" Version 1.0.1: test_cvv_length_is_not_3 - green
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
    
    if type(cvv) != int:
        raise exc.WrongTypeError("CVV", int, type(cvv))
    raise exc.WrongLengthError("CVV", 3, len(str(cvv)))
"""

""" Version 1.1.0: test_cvv_length_is_not_3 - refactor
def has_errors(name, number, card_type, date, cvv):
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "O formato esperado é \'MM/AA\'")
    
    if type(cvv) != int:
        raise exc.WrongTypeError("CVV", int, type(cvv))
    if len(str(cvv)) != 3:
        raise exc.WrongLengthError("CVV", 3, len(str(cvv)))
"""

def has_errors(name, number, card_type, date, cvv):
    """
    Check if there are any errors in the provided card information.

    :param name: The name on the card.
    :type name: str
    :param number: The card number.
    :type number: int
    :param card_type: The type of the card (Credit or Debit).
    :type card_type: str
    :param date: The expiration date of the card (format: MM/YY).
    :type date: str
    :param cvv: The CVV code of the card.
    :type cvv: int
    :raises exc.EmptyFieldError: If any required field is empty.
    :raises exc.WrongTypeError: If any field has an unexpected type.
    :raises exc.NonLetterError: If the name contains non-letter characters.
    :raises exc.WrongLengthError: If any field has an invalid length.
    :raises exc.InvalidCardTypeError: If the card type is not valid.
    :raises exc.WrongFormatError: If the date has an invalid format.
    """
    if name == None or name == "":
        raise exc.EmptyFieldError("Nome")
    if type(name) != str:
        raise exc.WrongTypeError("Nome", str, type(name))
    if not name.replace(" ", "").isalpha():
        raise exc.NonLetterError("Nome")
    
    if number == None:
        raise exc.EmptyFieldError("Número do Cartão")
    if type(number) != int:
        raise exc.WrongTypeError("Número do Cartão", int, type(number))
    if len(str(number)) != 16:
        raise exc.WrongLengthError("Número do Cartão", 16, len(str(number)))
    
    if type(card_type) != str:
        raise exc.WrongTypeError("Tipo do Cartão", str, type(card_type))
    if card_type != "Crédito" and card_type != "Débito":
        raise exc.InvalidCardTypeError(card_type)
    
    if type(date) != str:
        raise exc.WrongTypeError("Data de Validade", str, type(date))
    if len(date) != 5:
        raise exc.WrongLengthError("Data de Validade", 5, len(date))
    if date[2] != "/":
        raise exc.WrongFormatError("Data de Validade")
    if not date[:2].isnumeric() or not date[3:].isnumeric():
        raise exc.WrongTypeError("Data de Validade", int, type(date),
                            "The expected format is 'MM/YY'")
    
    if type(cvv) != int:
        raise exc.WrongTypeError("CVV", int, type(cvv))
    if len(str(cvv)) != 3:
        raise exc.WrongLengthError("CVV", 3, len(str(cvv)))