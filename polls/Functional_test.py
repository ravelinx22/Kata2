__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('William')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Ravelo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('323424579')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('wr.ravelo@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys(BASE_DIR + "/static/test.png")

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('wrravelo22')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="William Ravelo"]')

        self.assertIn('William Ravelo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="William Ravelo"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="William Ravelo"]')

        self.assertIn('William Ravelo', h2.text)

    def test_loginIndependiente(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(3)

        usuario = self.browser.find_element_by_id('username')
        usuario.send_keys('wrravelo22')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('clave123')

        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)

        editarPerfil = self.browser.find_element_by_id('id_editar')
        self.assertIn('Editar', editarPerfil.text)

    def test_editarIndependiente(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(3)

        usuario = self.browser.find_element_by_id('username')
        usuario.send_keys('wrravelo22')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('clave123')

        ingresar = self.browser.find_element_by_id('id_ingresar')
        ingresar.click()
        self.browser.implicitly_wait(10)
        self.browser.get('http://localhost:8000')

        editarPerfil = self.browser.find_element_by_id('id_editar')
        editarPerfil.click()
        self.browser.implicitly_wait(3)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Ricardo')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Mendez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('1')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('3012222222')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('wrravelo@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.clear()
        imagen.send_keys(BASE_DIR + "/static/test.png")

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        self.browser.get('http://localhost:8000')

        salir = self.browser.find_element_by_id('id_logout')
        salir.click()
        self.browser.implicitly_wait(3)

        span=self.browser.find_element(By.XPATH, '//span[text()="Ricardo Mendez"]')

        self.assertIn('Ricardo Mendez', span.text)