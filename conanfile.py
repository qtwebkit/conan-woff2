from conans import ConanFile, CMake, tools
import os


class Woff2Conan(ConanFile):
    name = "woff2"
    version = "1.0.2"
    license = "The Web Open Font Format (WOFF) is a font format for use in web pages."
    author = "Bincrafters <bincrafters@gmail.com>"
    url = "https://github.com/qtwebkit/conan-woff2"
    description = "<Description of Woff2 here>"
    topics = ("conan", "font", "woff2")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake", "cmake_find_package_multi"
    exports_sources = ["CMakeLists.txt"]
    requires = "brotli/1.0.7"
    _source_subfolder = "sources"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        tools.get(url="https://github.com/google/woff2/archive/v{}.tar.gz".format(self.version),
                  sha256="add272bb09e6384a4833ffca4896350fdb16e0ca22df68c0384773c67a175594")
        os.rename("woff2-{}".format(self.version), self._source_subfolder)
        os.rename(os.path.join(self._source_subfolder, "CMakeLists.txt"),
                  os.path.join(self._source_subfolder, "CMakeLists_original.txt"))
        os.rename("CMakeLists.txt", os.path.join(self._source_subfolder, "CMakeLists.txt"))

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["woff2common", "woff2enc", "woff2dec"]
