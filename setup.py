from setuptools import setup, find_packages

setup(
    name="foroyskt",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "cffi>=1.15.1",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for Faroese language processing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ForoyskPackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    setup_requires=["cffi>=1.15.1"],
    cffi_modules=["src/foroyskt/bin_build.py:ffibuilder"],
)