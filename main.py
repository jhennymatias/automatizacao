"""
    Autor: Jhennifer Cristine Matias
    Projeto: Preenchimento de dados do Project English de modo automizado
"""

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

palavras = []

def le():
    arquivo = open('dados.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
        

def insert():
    id_e = 'english'
    id_p = 'portuguese'
    id_d = 'description'
    id_s = 'syno'
    id_b = 'btn_e'
    driver.get('http://localhost:3000/cadastro')
    input_e = driver.find_element_by_id(id_e)
    input_p = driver.find_element_by_id(id_p)
    input_d = driver.find_element_by_id(id_d)
    input_s = driver.find_element_by_id(id_s)
    input_b = driver.find_element_by_id(id_b)
    
    for item in palavras:
        dados = []
        dados = item.split(';')
        input_e.send_keys(dados[0])
        input_p.send_keys(dados[1])
        input_d.send_keys(dados[2])
        input_s.send_keys(dados[3])
        input_b.click()

le()
insert()