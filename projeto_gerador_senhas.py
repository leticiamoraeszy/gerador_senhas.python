
import secrets 
from rich import print
import string

class GeradorSenhas:
    def __init__(self, tamanho, usar_numeros=True, usar_maiusculas=False, usar_minusculas=True, usar_simbolos=False,):
        self.tamanho = tamanho 
        self.usar_maiusculas = usar_maiusculas
        self.usar_minusculas = usar_minusculas
        self.usar_simbolos = usar_simbolos
        self.usar_numeros = usar_numeros
      

    @property 

    def tamanho(self):
        return self._tamanho

    @tamanho.setter

    def tamanho(self, valor):  
        if valor <= 6:
            raise ValueError
        elif not isinstance(valor, int):
            raise ValueError
        elif valor > 16:
            raise ValueError
        self._tamanho = valor 


    def montar(self):
        alfabeto = ''
        if self.usar_numeros:
            alfabeto += string.digits
        if self.usar_simbolos:
            alfabeto += string.punctuation
        if self.usar_maiusculas:
            alfabeto += string.ascii_uppercase
        if self.usar_minusculas:
            alfabeto += string.ascii_lowercase

        return alfabeto

    def gerar(self):
        alfabeto = self.montar()
        senha = ''
        for _ in range(self._tamanho):
            senha += secrets.choice(alfabeto)

        return senha


    def verificar_forca(self):
        pontos = 0
        if 8 <= self._tamanho <= 12:
            pontos += 2
        if self.usar_minusculas:
            pontos += 1
        if self.usar_maiusculas:
            pontos += 1
        if self.usar_simbolos:
            pontos += 2

        if pontos > 7:
            print('--- VERIFICAÇÃO DA SENHA---')
            print(f'pontuação - {pontos}')
            print('senha considerada FORTE')
        if pontos <= 5:
            print('--- VERIFICAÇÃO DA SENHA---')
            print(f'pontuação - {pontos}')
            print('senha considerada FRACA')

    def ver_senha(self):
        senha = self.gerar()
        print(f'--GERADOR DE SENHAS--')
        print(f'{senha}')

senha = GeradorSenhas(tamanho=7, usar_maiusculas=True, usar_minusculas=True, usar_simbolos=True, usar_numeros=True)
senha.montar()
senha.gerar()
senha.verificar_forca()
senha.ver_senha()
