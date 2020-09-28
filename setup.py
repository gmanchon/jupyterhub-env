from setuptools import setup

REQUIRED_PACKAGES = [
    'jupyter-offlinenotebook==0.1.0',
    'pandas==1.1.2',
    'seaborn==0.10.1']

setup(
    name='WagonIntroToDS',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    description='Wagon Intro to Data Science'
)
