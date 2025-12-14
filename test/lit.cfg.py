# test/lit.cfg.py
import os
import lit.formats
from lit.llvm import llvm_config
from lit.llvm.subst import ToolSubst

# This is a configuration file for the 'lit' test runner.

# name: The name of this test suite.
config.name = 'OTIR'

# test_format: The test format to use to interpret tests.
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)

# suffixes: A list of file extensions to treat as test files.
config.suffixes = ['.mlir']

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.path.join(config.otir_obj_root, 'test')

# Tweak the PATH to include the tools dir where `otir-opt` is built.
llvm_config.with_environment('PATH', config.otir_tools_dir, append_path=True)
# Also include the main LLVM/MLIR tools dir for utilities like `FileCheck`.
llvm_config.with_environment('PATH', config.llvm_tools_dir, append_path=True)

# Define substitutions for our tools. This allows us to use `%otir-opt` in
# our RUN lines in the .mlir test files.
tool_substitutions = [
    ToolSubst('%otir-opt', os.path.join(config.otir_tools_dir, 'otir-opt')),
    ToolSubst('%FileCheck', os.path.join(config.llvm_tools_dir, 'FileCheck'))
]
config.substitutions.extend(tool_substitutions)