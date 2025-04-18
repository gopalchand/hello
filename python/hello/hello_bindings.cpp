#include <pybind11/pybind11.h>
#include <hello.hpp>

namespace py = pybind11;

PYBIND__MODULE(hello_cpp, m) {
    m.def("say_hello", &say_hello);
}
