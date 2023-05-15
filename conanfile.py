# noqa: D100

from conan import ConanFile
from conan.tools.files import get, copy


class visit_structRecipe(ConanFile):  # noqa: D101
    name = "visit_struct"
    user = "gtel"
    channel = "stable"
    license = "Boost Software License"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-visit_struct"
    description = "A miniature library for struct-field reflection in C++ "
    topics = ("reflection", "introspection", "visitor")
    no_copy_source = True
    homepage = "https://github.com/cbeck88/visit_struct"

    package_type = "header-library"
    
    def source(self):  # noqa: D102
        get(self, self.conan_data['sources'][self.version], strip_root=True)

    def package(self):  # noqa: D102
        copy(self, "*.hpp", self.source_folder, self.package_folder)

    def package_info(self):  # noqa: D102
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
