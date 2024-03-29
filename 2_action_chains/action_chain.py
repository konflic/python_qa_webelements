import random
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium import webdriver

chrome = webdriver.Chrome()

# Долгое открытие страницы
chrome.implicitly_wait(20)
chrome.maximize_window()

# Открываем страницу и закрываем поп-ап
chrome.get("https://konflic.github.io/examples/drawdivs/index.html")

# Получаем облассть в которой можно рисовать
draw_area = chrome.find_element(By.CSS_SELECTOR, "#board")
dims = draw_area.rect
print(dims)

# Создаем объект ActionChains в который будем записывать наши действия
actions = ActionChains(chrome)


# Наполняем actions 10 разными действиями
for i in range(10):
    # Определяем случайные координаты по x и y
    random_x = random.randint(-400, 0)
    random_y = random.randint(-400, 0)
    print(random_x, random_y)
    # Нажимаем на кнопку мыши в этих координатах и не отпускаем
    actions.move_to_element_with_offset(draw_area, random_x, random_y).click_and_hold()
    actions.pause(0.2)
    # Определяем случайные величины для смешения курсора от текущей точки
    offset_x = random.randint(10, 100)
    offset_y = random.randint(10, 100)
    print(offset_x, offset_y)
    # Выполняем движение мышью на заданное количество пикселей и отпускаем
    actions.move_by_offset(offset_x, offset_y)
    actions.release()

    # Выполняем все накопленные в цикле for действия начиная с первого

    actions.perform()
