from setuptools import setup, find_packages

# Lê o README pra usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='batata-lib',  # Nome único pro PyPI
    version='0.1.1',
    author='Decaptado',
    description='Biblioteca pessoal pra facilitar minha vida',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aaaa560/potato-lib',  # Coloca seu GitHub
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Se for MIT
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.10',  # Type hints com | precisa 3.10+
    install_requires=[],  # Sem dependências externas (bom!)
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=4.0',
        ],
    },
)