# pip install selenium webdriver-manager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Установка и настройка ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы
driver.get("https://www.yandex.ru")

# Вывод заголовка страницы
print(driver.title)

# Закрытие браузера
driver.quit()