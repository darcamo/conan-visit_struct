#include <visit_struct/visit_struct.hpp>
#include <string>
#include <iostream>

struct test_struct_one {
    int a;
    float b;
    std::string c;
};

VISITABLE_STRUCT(test_struct_one, a, b, c);

int main() {
    static_assert(visit_struct::traits::is_visitable<test_struct_one>::value, "WTF");
    static_assert(visit_struct::field_count<test_struct_one>() == 3, "WTF");
    std::cout << "Code with visit_struct run ok" << std::endl;
}
