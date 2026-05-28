from setuptools import setup, find_packages

setup(
    name="medcodes",
    version="0.2",
    url="https://github.com/topspinj/medcodes",

    author="Jill Cates",
    author_email="jill@biosymetrics.com",

    description="Tools for working with medical codes such as ICD and CPT, forked from https://github.com/mark-hoffmann/icd",

    packages=find_packages(),

    install_requires=['pandas'],

    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
)
