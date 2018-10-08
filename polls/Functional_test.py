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
        #self.browser.get('http://localhost:8000')
        #span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        #span.click()

        #h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        #self.assertIn('Juan Daniel Arevalo', h2.text)