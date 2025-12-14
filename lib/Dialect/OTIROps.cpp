#include "otir/Dialect/OTIROps.h"
#include "mlir/IR/Builders.h"
#include "mlir/IR/OpImplementation.h"

void mlir::otir::OTIRDialect::initialize() {
  addOperations<
#define GET_OP_LIST
#include "otir/Dialect/OTIROps.cpp.inc"
      >();
}

#define GET_OP_CLASSES
#include "otir/Dialect/OTIROps.cpp.inc"