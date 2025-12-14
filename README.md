# OTIR Project

This repository contains the reference implementation for the Open Tile Intermediate Representation (OTIR) as an MLIR dialect.

## Build Instructions

1.  **Prerequisites:**
    *   CMake (>= 3.20)
    *   A C++17 compliant compiler (GCC, Clang, MSVC)
    *   Ninja (recommended)

2.  **Configure:**
    ```bash
    cmake -S . -B build -G Ninja -DOTIR_ENABLE_TESTING=ON -DCMAKE_BUILD_TYPE=Release
    ```

3.  **Build:**
    ```bash
    cmake --build build
    ```

4.  **Run Tests:**
    ```bash
    cmake --build build --target check-otir
    ```