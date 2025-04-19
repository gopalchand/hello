from skbuild import setup

setup(
    name="hellothere_package",
    version="0.1",
    description="A Hello World C++ extension with CMake and pybind11",
    author="Your Name",
    packages=["hellothere_package"],
    package_dir={"": "python"},
    python_requires=">=3.6",
    cmake_install_dir="python/hellothere_package",
)
