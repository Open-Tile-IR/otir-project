cmake_minimum_required(VERSION 3.20)
project(OTIR CXX C)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- Find the pre-built MLIR package ---
# This will use the MLIR_DIR and LLVM_DIR variables passed from the superbuild.
find_package(MLIR REQUIRED CONFIG)
find_package(LLVM REQUIRED CONFIG)
find_package(Python3 COMPONENTS Interpreter REQUIRED)

# The MLIR CMake modules are now available.
include(MLIRTableGen)
include(AddMLIR)
include(MLIRInstall)

# --- Project Definition (this part remains mostly the same) ---
include_directories(${MLIR_INCLUDE_DIRS})
include_directories(include)
include_directories(${CMAKE_BINARY_DIR}/include)

set(OTIR_TABLEGEN_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include/otir/Dialect)
set(OTIR_TABLEGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/include/otir/Dialect)

add_mlir_dialect(OTIRDialect OTIROps
    GEN_DIR ${OTIR_TABLEGEN_OUTPUT_DIR}
    TD_FILES ${OTIR_TABLEGEN_DIR}/OTIROps.td
)

add_library(OTIRDialect
    lib/Dialect/OTIROps.cpp
)
target_link_libraries(OTIRDialect PUBLIC MLIR::MLIRCore MLIR::Support)
target_include_directories(OTIRDialect PUBLIC
    include
    ${OTIR_TABLEGEN_OUTPUT_DIR}
)

add_executable(otir-opt tools/otir-opt.cpp)
target_link_libraries(otir-opt PRIVATE OTIRDialect)

# --- Testing Configuration ---
option(OTIR_ENABLE_TESTING "Enable testing" ON)
if(OTIR_ENABLE_TESTING)
  enable_testing()
  # Pass variables to lit
  set(LIT_EXECUTABLE ${LLVM_EXTERNAL_LIT})
  set(OTIR_TOOLS_DIR ${CMAKE_BINARY_DIR}/bin)
  set(LLVM_TOOLS_DIR ${LLVM_TOOLS_BINARY_DIR})
  add_subdirectory(test)
endif()