import eel
import pyautogui as pya
import pywinauto

from django.db import Error
from pywinauto import Application

# from bot_app.Models.models import (
#     Objects,
# )

eel.init(path="web")


@eel.expose
def get_objects_info(name):
    # список всех интересующих нас объектов
    objects_list = pywinauto.findwindows.find_elements(
        title_re=str(name),
    )
    result = []
    # их хендлы - аналог id
    for obj in objects_list:
        info = {
            "Handle": obj.handle,
            "Name": obj.name,
            "Top(Y)": obj.rectangle.top,
            "Bottom(Y)": obj.rectangle.bottom,
            "Left(X)": obj.rectangle.left,
            "Right(X)": obj.rectangle.right,
        }

        result.append(info)
    if not result:
        return 'Объект не найден'
    return str(result)
    # first_elem = Application().connect(
    #     handle=handles[0],
    # )
    # first_elem.window(title_re="Проводник", handle=handles[0]).set_focus()


@eel.expose
def save_objects_cords(name):
    # info = get_objects_info(name)
    # for info_dict in info:
    #     obj = Objects(
    #         handle_num=info_dict.get("Handle"),
    #         obj_name=info_dict.get("Name"),
    #         top_y=info_dict.get("Top(Y)"),
    #         bottom_y=info_dict.get("Bottom(Y)"),
    #         left_x=info_dict.get("Left(X)"),
    #         right_x=info_dict.get("Right(X)"),
    #     )
    #     try:
    #         obj.save()
    #     except Error as er:
    #         return str(er)

    return 'Сохранено!'


eel.start("app.html", size=(500, 500), mode='chrome')
