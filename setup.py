from setuptools import setup

def readme_file_contents():
    with open("README.md") as readme_file:
        data = readme_file.read()
    return data
setup(
        name="honeypot",
        version="1.0",
        description="Simple TCP Honeypot",
        long_description=readme_file_contents(),
        author="Jayhawk",
        author_email="v3sirion@gmail.com",
        license="MIT",
        packages=["honeypot"],
       # scripts=['bin/nanopot'],
        zip_safe=False,
        install_requires=[
            'docopt'
            ]
        )
