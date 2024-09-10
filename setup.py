from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'lanchain',
        'python-dotenv',
        'setuptools',
        'wheel',
        'streamlit',
        'PyPDF2'
    ],
    author='Moussa Moustapha',
)