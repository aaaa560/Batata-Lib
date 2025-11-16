from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='batata-lib',
    version='0.1.2',
    author='Decaptado',
    description='Biblioteca pessoal pra facilitar minha vida',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aaaa560/potato-lib',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.10',
    install_requires=['requests>=2.0', 'bs4>=4.0'],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=4.0',
        ],
    },
)