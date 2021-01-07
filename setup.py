from setuptools import find_packages, setup


def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


setup(
    name="jfa",
    version="0.1",
    author="Yotam loewenbach",
    author_email="yotam12341@gmail.com",
    description="CLI tool for Jfrog artifactory",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests', 'click==7.1.2'],
    entry_points="""
        [console_scripts]
        jfa=jfa.cli:cli
    """,
)
