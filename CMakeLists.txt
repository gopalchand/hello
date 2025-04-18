cmake_minimum_required(VERSION 3.15)
project(hello_cmake)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)

# Include pybind11
include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.11.1  # Or the latest version
)
FetchContent_MakeAvailable(pybind11)

# Build the Python module
pybind11_add_module(hello_cpp
    python/hello/hello_bindings.cpp
    src/hello.cpp
)
