import os

__all__ = [
    'ROOT_DIR',
    'TRUNCATE_OPS',
    'MERGE_OPS',
    'VALID_OPS'
]

# This is the root directory of this project
ROOT_DIR = os.environ.get('NVCIM_HOME')

# These are the boundary operators for graph dispatching,
# where the original graph will be truncated at the boundary operators
# and then divided into host graph and device graph.
TRUNCATE_OPS = {
    'Conv', 
    'Relu', 'PRelu', 'HardSigmoid',
    'MaxPool', 'AveragePool'
}

# These are the operators that merges data from several branches to
# one operator, this constant helps to construct raw operator graph
MERGE_OPS = {
    'Mul','Add','Concat'
}

# Here list all valid operators that are supported by this tool,
# including valid device operators and valid host operators
VALID_OPS = {
    'Conv', 'Gemm',
    'Mul', 'Concat', 'Add',
    'Relu', 'PRelu', 'HardSigmoid', 'Softmax',
    'MaxPool', 'AveragePool', 'GlobalAveragePool',
    'Flatten', 'Reshape', 'Resize', 'Transpose'
}