from selenium import webdriver
from selenium_config import configure_chromedriver

configure_chromedriver()
# Configuración para ejecutar Chrome en modo headless (sin interfaz gráfica)
chrome_options = webdriver.ChromeOptions()
# Comentar esta línea si deseas ver el navegador
chrome_options.add_argument('--headless')

# Crear una instancia del navegador Chrome con el controlador en el PATH
driver = webdriver.Chrome(options=chrome_options)

# Navegar a una URL
url = 'https://www.ejemplo.com'
driver.get(url)

# Realizar acciones automatizadas, por ejemplo, hacer clic en un botón
element = driver.find_element_by_id('id_del_elemento')
element.click()

# Realizar otras acciones según tus necesidades

# Cerrar el navegador al finalizar
driver.quit()
