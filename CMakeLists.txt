set (CMAKE_CXX_STANDARD 11)
cmake_minimum_required(VERSION 3.9)


function(add name)
    add_executable(${name} ${name}.cxx)
    add_custom_command(OUTPUT ${name}.log
            COMMAND time ./${name} | tee ${name}.log
            DEPENDS ${name})
    add_custom_target(run-${name} ALL
            DEPENDS ${name}.log)
endfunction()

add(674)
add(678)
add(680)
