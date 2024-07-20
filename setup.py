from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "anyio==4.2.0",
        "beerchan_bot @ git+https://github.com/beerchan-edu/beerchan-bot.git@a8c796cf7a24a80b3897b1e4b6bfc055c47f9200",
        "certifi==2023.11.17",
        "exceptiongroup==1.2.0",
        "greenlet==3.0.3",
        "h11==0.14.0",
        "httpcore==1.0.2",
        "httpx==0.25.2",
        "idna==3.6",
        "iniconfig==2.0.0",
        "packaging==23.2",
        "pluggy==1.4.0",
        "psycopg==3.1.18",
        "psycopg-binary==3.1.18",
        "pytest==8.0.1",
        "python-dotenv==1.0.0",
        "python-telegram-bot==20.7",
        "sniffio==1.3.0",
        "SQLAlchemy==2.0.25",
        "tomli==2.0.1",
        "typing_extensions==4.9.0",
    ],
    dependency_links=[
        "https://github.com/beerchan-edu/beerchan-bot.git"
    ],
)
