cmake_minimum_required(VERSION 3.15)
project(hellothere_project)

set(CMAKE_CXX_STANDARD 11)

include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.11.1
)
FetchContent_MakeAvailable(pybind11)

include_directories(${CMAKE_SOURCE_DIR}/src)

pybind11_add_module(hellothere_module
    python/hellothere_package/hellothere_bindings.cpp
    src/hello.cpp
)

#install(TARGETS hellothere_module
#        LIBRARY DESTINATION hellothere_package)

install(TARGETS hellothere_module
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/hellothere_package)
