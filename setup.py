import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="energy_trading_api",
    version="0.0.22",
    author="jericmac",
    author_email="",
    description="API Wrappers for the Energy Markets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jericmac/energy-trading-api-wrappers",
    install_requires=["eia-python == 1.22","Scrapy==1.6.0"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)