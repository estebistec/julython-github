# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name="julython-github",
    version="0.1.0",
    scripts = [
        'scripts/julython_github.py'
    ],
    install_requires=[
        "PyGithub==1.17.0"
    ],

    # metadata for upload to PyPI
    author="Steven Cummings",
    author_email="cummingscs@gmail.com",
    description="Script to ensure the julython webhook on your GitHub python repos",
    license="MIT",
    keywords="julython python github webhook",
    url="https://github.com/estebistec/julython-github",
    download_url="http://pypi.python.org/pypi/julython-github",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
