# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Global flags for aot autograd
"""
import os

use_functionalize = True

use_fake_tensor = True

debug_partitioner = os.environ.get('AOT_PARTITIONER_DEBUG', False)
# Prints out forward + backwards FX graphs
debug_graphs = os.environ.get('AOT_FX_GRAPHS', False)
# Prints out joint graph traced, before partitioning
debug_joint = os.environ.get('AOT_FX_GRAPHS_JOINT', False)
