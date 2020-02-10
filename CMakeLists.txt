cmake_minimum_required(VERSION 2.8.12)

project(cmake_wrapper)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Brotli REQUIRED)
set(BROTLIDEC_FOUND ON)
set(BROTLIDEC_LIBRARIES Brotli::Brotli)
get_target_property(BROTLIDEC_INCLUDE_DIRS Brotli::Brotli INTERFACE_INCLUDE_DIRECTORIES)

set(BROTLIENC_FOUND ON)
set(BROTLIENC_LIBRARIES Brotli::Brotli)
get_target_property(BROTLIENC_INCLUDE_DIRS Brotli::Brotli INTERFACE_INCLUDE_DIRECTORIES)

include(CMakeLists_original.txt)
