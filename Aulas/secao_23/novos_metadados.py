"""
Metadata (Metadados)

# Serve para vermos as versoes dos nossos pacotes e outras coisas
"""

from importlib import metadata

print(metadata.version('pip'))  # 22.1

metadados_pip = metadata.metadata('pip')

print(list(metadados_pip))
print(metadados_pip['Version'])  # 22.1
print(metadados_pip['License'])  # MIT

print(len(metadata.files('pip')))  # 1060

print(metadata.requires('pip'))  # None

print(metadata.version('mypy'))  # 0.950

print(metadata.requires('mypy'))