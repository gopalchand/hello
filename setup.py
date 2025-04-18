from skbuild import setup

setup(
    name="hello_cmake",
    version="0.1.0",
    description="A Hello World C++ extension with CMake and pybind11",
    author="Your Name",
    packages=["hellothere"],
    package_dir={"": "python"},
    python_requires=">=3.6",
)
