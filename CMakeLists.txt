cmake_minimum_required(VERSION 3.15)
project(visit_struct CXX)




add_library(visit_struct src/visit_struct.cpp)
target_include_directories(visit_struct PUBLIC include)



set_target_properties(visit_struct PROPERTIES PUBLIC_HEADER "include/visit_struct.h")
install(TARGETS visit_struct)
