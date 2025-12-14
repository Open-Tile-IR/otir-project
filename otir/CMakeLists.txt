cmake_minimum_required(VERSION 3.20)
project(OTIR CXX C)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(third_party)

# After `add_subdirectory(third_party)` has run, MLIR's CMake modules are
# available. Now we can safely include them.
include(MLIRTableGen)
include(AddMLIR)
include(MLIRInstall)

# --- Set up include directories ---
# Add our own project's include path.
include_directories(include)
# Add the directory where TableGen will place the generated files.
include_directories(${CMAKE_BINARY_DIR}/include)


# --- Generate Dialect Classes from TableGen files ---
# This is the core of defining our dialect.
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
# We must link against the MLIR libraries we depend on.
target_link_libraries(OTIRDialect PUBLIC ${MLIR_LIBS})
# We must include our own source tree and the generated files.
target_include_directories(OTIRDialect PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${OTIR_TABLEGEN_OUTPUT_DIR}
)


# --- Define the 'otir-opt' tool ---
add_executable(otir-opt tools/otir-opt.cpp)
target_link_libraries(otir-opt PRIVATE OTIRDialect)


# --- Testing Configuration ---
option(OTIR_ENABLE_TESTING "Enable testing" ON)

if(OTIR_ENABLE_TESTING)
  # This enables CTest, the CMake testing framework.
  enable_testing()
  # This adds our test subdirectory, which contains the lit configuration.
  add_subdirectory(test)
endif()