#include "mlir/IR/Dialect.h"
#include "mlir/IR/MLIRContext.h"
#include "mlir/InitAllDialects.h"
#include "mlir/InitAllPasses.h"
#include "mlir/Tools/mlir-opt/MlirOptMain.h"

#include "otir/Dialect/OTIROps.h"

int main(int argc, char **argv) {
  mlir::registerAllPasses();

  mlir::DialectRegistry registry;
  
  // Register all standard dialects
  registerAllDialects(registry);

  // Register the OTIR dialect
  registry.insert<mlir::otir::OTIRDialect>();

  return mlir::asMainReturnCode(
      mlir::MlirOptMain(argc, argv, "OTIR optimizer driver\n", registry));
}