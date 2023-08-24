"""
Módulos Externos

Utilizamos o Gerenciador de Pacotes Python chamado: Pip -> Python Installer Package

Voce Pode conhecer todos os pacotes externos em: https://pypi.org

# Para instalar usamos no terminal o seguinte: 'pip install nome_do_módulo'
# Por exemplo: pip install colorama

Colorama -> É utilizado para permitir impressão de textos coloridos no terminal
"""

from colorama import init, Fore

init()

print(Fore.BLACK + 'Marcos Rodrigues')
print(Fore.BLUE + 'Marcos Rodrigues')
print(Fore.LIGHTMAGENTA_EX + 'Marcos Rodrigues')
print(Fore.RED + 'Marcos Rodrigues')
print(Fore.YELLOW + 'Marcos Rodrigues')
