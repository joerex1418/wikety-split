import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wikety-split',
    version='1.0.0',
    author='Joe Rechenmacher',
    author_email='joe.rechenmacher@gmail.com',
    long_description=long_description,
    url='https://github.com/joerex1418/wiki',
    project_urls = {
        "Issues": "https://github.com/joerex1418/wikety-split/issues",
    },
    license='GPU',
    packages=setuptools.find_packages(where='/wiki/wiki/',include=["__init__"]),
    install_requires=['requests','pandas','bs4'],
)
