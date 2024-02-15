import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__='0.0.0'
REPO_NAME='plant-disease-prediction'
AUTHOR_USER_NAME='mauriceoboya'
SRC_REPO='cnnClassifier'
AUTHOR_EMAIL='mauriq97@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A project to classify plant diseases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mauriceoboya/plant-disease-prediction",
    project_urls={
        "Bug Tracker": "https://github.com/mauriceoboya/plant-disease-prediction/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",

    ]
)
