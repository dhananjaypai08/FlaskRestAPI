from setuptools import find_packages, setup

setup(
    name='FlaskRestAPI',
    version='1.0.0',
    author='Dhananjay Pai',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
