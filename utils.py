from telebot import types

def create_buttons(equipmentList: list[str]) -> types.InlineKeyboardMarkup:
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.row_width = 2

    for equipment in equipmentList:
        newButton = types.InlineKeyboardButton(text=equipment, callback_data=equipment)
        markup_inline.add(newButton)
    
    return markup_inline

# TODO
def get_equipment(message: str) -> list[str]:
  """функция для получения списка оборудования с сервера"""
  equipmentList = message.split(" ")
  equipmentList.remove("+")
  return equipmentList

# TODO
def send_equipment(message):
    """функция для отправки результата на сервер"""
    print(message + "\n")
    pass