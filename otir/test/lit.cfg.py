import os
import lit.formats
from lit.llvm import llvm_config
from lit.llvm.subst import ToolSubst

config.name = 'OTIR'
config.test_format = lit.formats.ShTest(True)
config.suffixes = ['.mlir']
config.test_source_root = os.path.dirname(__file__)

# The superbuild passes the necessary paths to us.
# @-signs are substituted by CMake's configure_file command if we use it,
# but for simplicity, we assume these are passed via environment or direct config.
# CMake will define these for CTest.
config.otir_tools_dir = "@OTIR_TOOLS_DIR@"
config.llvm_tools_dir = "@LLVM_TOOLS_DIR@"

llvm_config.with_environment('PATH', config.otir_tools_dir, append_path=True)
llvm_config.with_environment('PATH', config.llvm_tools_dir, append_path=True)

tool_substitutions = [
    ToolSubst('%otir-opt', os.path.join(config.otir_tools_dir, 'otir-opt')),
    ToolSubst('%FileCheck', os.path.join(config.llvm_tools_dir, 'FileCheck'))
]
config.substitutions.extend(tool_substitutions)