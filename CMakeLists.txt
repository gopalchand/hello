cmake_minimum_required(VERSION 3.15)
project(hello_cmake)

set(CMAKE_CXX_STANDARD 11)

include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.11.1
)
FetchContent_MakeAvailable(pybind11)

include_directories(${CMAKE_SOURCE_DIR}/src)

pybind11_add_module(hello_cpp
    python/hello/hello_bindings.cpp
    src/hello.cpp
)

install(TARGETS hello_cpp
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
