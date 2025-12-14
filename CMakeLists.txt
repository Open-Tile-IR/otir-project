cmake_minimum_required(VERSION 3.20)
project(OTIR CXX C)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Handle third-party dependencies, specifically LLVM/MLIR.
add_subdirectory(third_party)

# --- Generate Dialect Classes from TableGen files ---
# This is a crucial step for any MLIR dialect.
include(MLIRTableGen)
set(OTIR_TABLEGEN_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include/otir/Dialect)
set(OTIR_TABLEGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/include/otir/Dialect)

add_mlir_dialect(OTIRDialect OTIROps
    GEN_DIR ${OTIR_TABLEGEN_OUTPUT_DIR}
    TD_FILES ${OTIR_TABLEGEN_DIR}/OTIROps.td
)

# --- Define the OTIR Dialect Library ---
add_library(OTIRDialect
    lib/Dialect/OTIROps.cpp
)
target_include_directories(OTIRDialect PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${OTIR_TABLEGEN_OUTPUT_DIR}
)
target_link_libraries(OTIRDialect PUBLIC ${MLIR_LIBS})


# --- Define the 'otir-opt' tool ---
add_executable(otir-opt tools/otir-opt.cpp)
target_link_libraries(otir-opt PRIVATE OTIRDialect)


# --- Testing Configuration ---
option(OTIR_ENABLE_TESTING "Enable testing" ON)

if(OTIR_ENABLE_TESTING)
  enable_testing()
  add_subdirectory(test)
endif()