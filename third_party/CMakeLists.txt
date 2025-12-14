# third_party/CMakeLists.txt
include(FetchContent)

# --- LLVM/MLIR Dependency ---
# Using a specific commit for reproducibility, but tags like llvmorg-18.1.5 are fine too.
set(LLVM_PROJECT_TAG "llvmorg-18.1.5" CACHE STRING "LLVM project tag to checkout")
set(LLVM_ENABLE_PROJECTS "mlir" CACHE STRING "Projects to build from the LLVM monorepo")
set(LLVM_TARGETS_TO_BUILD "X86" CACHE STRING "Host target to build") # Adjust for your CPU architecture if needed

FetchContent_Declare(
  llvm_project
  GIT_REPOSITORY https://github.com/llvm/llvm-project.git
  GIT_TAG        ${LLVM_PROJECT_TAG}
  GIT_SHALLOW    TRUE
  GIT_PROGRESS   TRUE
)

# --- Configure LLVM/MLIR Build Options ---
set(LLVM_ENABLE_ASSERTIONS ON CACHE BOOL "")
set(LLVM_ENABLE_RTTI ON CACHE BOOL "")
set(LLVM_BUILD_EXAMPLES OFF CACHE BOOL "")
set(LLVM_INCLUDE_EXAMPLES OFF CACHE BOOL "")
set(LLVM_BUILD_TESTS OFF CACHE BOOL "")
set(LLVM_INCLUDE_TESTS OFF CACHE BOOL "")
set(MLIR_ENABLE_BINDINGS_PYTHON OFF CACHE BOOL "")

FetchContent_MakeAvailable(llvm_project)

# --- Propagate LLVM/MLIR build settings to our project ---
include_directories(${LLVM_INCLUDE_DIRS})
link_directories(${LLVM_LIBRARY_DIRS})

# Define the list of MLIR libraries our project depends on.
set(MLIR_LIBS
  MLIRIR
  MLIRSupport
  MLIRParser
  MLIRPass
  MLIRTransforms
  MLIRAnalysis
  MLIRDialect
  MLIRSCF
  MLIRVector
  LLVMSupport
)