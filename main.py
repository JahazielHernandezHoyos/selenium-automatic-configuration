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


def configure_chromedriver():
    """Configura ChromeDriver para que funcione con Selenium."""

    import os
    import subprocess

    chrome_version = "119.0.6045.105"

    if chrome_version is not None:
        # Descargar el controlador de Chrome para la versión especificada
        chromedriver_url = f'https://chromedriver.storage.googleapis.com/{
            chrome_version}/chromedriver_linux64.zip'
        chromedriver_filename = chromedriver_url.split('/')[-1]
        subprocess.call(['wget', chromedriver_url])

        # Descomprimir el controlador de Chrome
        subprocess.call(['unzip', chromedriver_filename])

        # Mover el controlador de Chrome al directorio de PATH
        chromedriver_path = os.path.join(
            os.path.dirname(chromedriver_filename), 'chromedriver')
        os.environ['PATH'] += f':{chromedriver_path}'

        # Instalar la última versión de la biblioteca Selenium
        subprocess.call(['pip', 'install', '-U', 'selenium'])

    # Mover el controlador de Chrome al directorio de PATH
    os.environ['PATH'] += f':{chromedriver_path}'

    # Instalar la última versión de la biblioteca Selenium
    subprocess.call(['pip', 'install', '-U', 'selenium'])
