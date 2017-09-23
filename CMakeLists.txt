cmake_minimum_required(VERSION 3.9)


function(add name)
    add_executable(${name} ${name}.cxx)
endfunction()

add(680)
