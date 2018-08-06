import os

from conans import ConanFile, CMake, tools

class Sol2Conan(ConanFile):
    name = "sol2"
    version = "2.20.4"
    license = "MIT License"
    url = "https://github.com/AtaLuZiK/conan-sol2"
    description = "Sol is a C++ library binding to Lua."
    exports_sources = ["sol2-config.cmake"]
    options = {
        "lua_version": ["5.3.4"],
        "single_header": [True, False],
    }
    default_options = (
        "lua_version=5.3.4",
        "single_header=False",
    )
    generators = "cmake"

    def requirements(self):
        self.requires("lua/%s@zimmerk/stable" % self.options.lua_version)

    @property
    def zip_folder_name(self):
        return "%s-%s" % (self.name, self.version)

    def source(self):
        zip_name = "%s-cpp-%s.tar.gz" % (self.name, self.version)
        tools.download("https://github.com/ThePhD/sol2/archive/v%s.tar.gz" % self.version, zip_name)
        # tools.check_md5(zip_name, "b12ab43ed0ea7618035421ccc330be25")
        tools.unzip(zip_name)
        os.unlink(zip_name)
        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file("CMakeLists.txt", "project(sol2 VERSION 2.20.0 LANGUAGES CXX C)",
                '''project(sol2 VERSION 2.20.0 LANGUAGES CXX C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def package(self):
        if self.options.single_header:
            self.copy("*.hpp", dst="include", src=self.zip_folder_name + "/single/sol")
        else:
            self.copy("sol.hpp", dst="include", src=self.zip_folder_name)
            self.copy("*.hpp", dst="include/sol", src=self.zip_folder_name + "/sol")
        # Copy the license files
        self.copy(pattern="LICENSE.txt", src=self.zip_folder_name)
        # Copy the cmake find module
        self.copy("sol2-config.cmake", ".", ".")
