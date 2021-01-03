import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colors-boss_space", # Replace with your own username
    version="0.0.2",
    author="boss_space",
    author_email="buhoizeon@gmail.com",
    description="colors!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boss-space/colors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)