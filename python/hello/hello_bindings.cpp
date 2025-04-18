#include <pybind11/pybind11.h>
#include "hello.hpp"

namespace py = pybind11;

// The first argument ("hello_cpp") must match the module name from CMake
PYBIND11_MODULE(hello_cpp, m) {
    m.def("say_hello", &say_hello, "A function that says hello");
}