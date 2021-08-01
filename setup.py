import setuptools

setuptools.setup(
    name="bojmaker",
    version="1.2",
    license='MIT',
    author="6Soo",
    author_email="kkokko-hero@hanmail.net",
    description="Setting up bothering BOJ problems all at once.",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "bojmaker = bojmaker.main:main"
        ]
    },
    url="https://github.com/6Soo/BOJ_maker",
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
