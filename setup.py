import os

from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

service_name = os.path.basename(os.getcwd())

setup(
    name=service_name,
    version="0.1.0",
    author="Origo Dataplattform",
    author_email="dataplattform@oslo.kommune.no",
    description="Serverless FastAPI demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.oslo.kommune.no/origo-dataplatform/fastapi-demo",
    py_modules=["app"],
    install_requires=["fastapi==0.61.1", "mangum==0.9.2"],
)
