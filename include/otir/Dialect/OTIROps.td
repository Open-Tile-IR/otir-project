#ifndef OTIR_OPS
#define OTIR_OPS

include "mlir/IR/OpBase.td"

def OTIR_Dialect : Dialect {
  let name = "otir";
  let cppNamespace = "::mlir::otir";
  let summary = "The Open Tile Intermediate Representation dialect.";
  let description = [{
    This dialect defines the core operations for the Open Tile IR,
    focusing on a hardware-agnostic, tile-centric programming model.
  }];
  let dependentDialects = ["mlir::func::FuncDialect"];
}

class OTIR_Op<string mnemonic, list<Trait> traits = []> :
    Op<OTIR_Dialect, mnemonic, traits>;

def OTIR_ProgramIdOp : OTIR_Op<"program_id"> {
  let summary = "Get the program ID for the current workgroup.";
  let description = [{
    Returns the index of the current workgroup within the grid along a
    specified axis. This is fundamental for partitioning work among workgroups.
  }];

  let arguments = (ins
    I64Attr:$axis
  );

  let results = (outs
    IndexType:$result
  );

  let assemblyFormat = "attr-dict `axis` `(` $axis `)`";
}

#endif // OTIR_OPS