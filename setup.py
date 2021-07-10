import setuptools

setuptools.setup(
    name="bojmaker",
    version="1.0",
    license='MIT',
    author="6Soo",
    author_email="kkokko-hero@hanmail.net",
    description="Setting up bothering BOJ problems all at once.",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    entry_points={
        "console_scripts": [
            "bojmaker = bojmaker.main:main"
        ]
    },
    url="https://github.com/6Soo/BOJ_maker_for_python",
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)