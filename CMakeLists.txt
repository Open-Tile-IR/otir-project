cmake_minimum_required(VERSION 3.20)
project(OTIRSuperbuild)

include(FetchContent)

# --- STAGE 1: Fetch and build LLVM/MLIR ---
# This part's only job is to download and build MLIR, creating an "SDK".
FetchContent_Declare(
  llvm_project
  GIT_REPOSITORY https://github.com/llvm/llvm-project.git
  GIT_TAG        "llvmorg-18.1.5"
)

set(LLVM_ENABLE_PROJECTS "mlir" CACHE STRING "")
set(LLVM_ENABLE_RUNTIMES "" CACHE STRING "") # We don't need runtimes like libcxx
set(LLVM_TARGETS_TO_BUILD "X86" CACHE STRING "") # Host architecture
set(LLVM_ENABLE_ASSERTIONS ON CACHE BOOL "")
set(LLVM_BUILD_EXAMPLES OFF CACHE BOOL "")
set(LLVM_BUILD_TESTS OFF CACHE BOOL "")
set(LLVM_INCLUDE_TESTS OFF CACHE BOOL "")
set(CMAKE_BUILD_TYPE "Release" CACHE STRING "")

# This makes LLVM build as an "external project" which happens before our main project.
FetchContent_MakeAvailable(llvm_project)

# --- STAGE 2: Configure our main OTIR project ---
# Now that LLVM/MLIR is guaranteed to be built, we can add our main project.
# We pass the location of the now-built MLIR to our sub-project via CMake variables.
set(MLIR_DIR ${llvm_project_BINARY_DIR}/lib/cmake/mlir)
set(LLVM_DIR ${llvm_project_BINARY_DIR}/lib/cmake/llvm)
set(LLVM_EXTERNAL_LIT ${llvm_project_SOURCE_DIR}/llvm/utils/lit/lit.py)

add_subdirectory(otir)