
from setuptools import setup, find_packages

setup(
    name="pad",
    version="0.0.1",
    author="Marcos Palacio",
    author_email="marcos.palacio@est.iudigital.edu.co",
    description="Paquete para análisis y gráficos",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "requests",
        "matplotlib"
    ]
)