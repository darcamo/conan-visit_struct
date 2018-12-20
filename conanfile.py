from conans import ConanFile, CMake, tools
# from conans.errors import ConanException
import os
import shutil


class VisitstructConan(ConanFile):
    name = "visit_struct"
    version = "1.0"
    license = "Boost Software License"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-visit_struct"
    description = "A miniature library for struct-field reflection in C++ "
    # topics = ("<Put some tag here>", "<here>", "<and here>")
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code
        in the folder and use exports instead of retrieving it with this
        source() method
        '''
        tools.get("https://github.com/cbeck88/visit_struct/archive/v{0}.zip".format(
                self.version))
        shutil.move("visit_struct-{}/".format(self.version), "sources")

    def package(self):
        self.copy("*", dst="include", src="sources/include")

    def package_id(self):
        self.info.header_only()
