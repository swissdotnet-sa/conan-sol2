find_path(SOL2_INCLUDE_DIR NAMES sol.hpp PATHS ${CONAN_INCLUDE_DIRS_SOL2})

set(SOL2_INCLUDE_DIRS ${SOL2_INCLUDE_DIR})

add_library(sol2 INTERFACE IMPORTED)
target_include_directories(sol2
  INTERFACE ${SOL2_INCLUDE_DIRS}
)

mark_as_advanced(SOL2_INCLUDE_DIR)

message("** sol2 found by Conan!")
set(SOL2_FOUND TRUE)
message("   - includes: ${SOL2_INCLUDE_DIRS}")
