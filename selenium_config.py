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

# Probamos la configuración
