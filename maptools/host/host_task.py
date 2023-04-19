import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Iterator
from maptools.core import HostGraph
from maptools.host.host_operator import HostOperator

__all__ = ['HostTask']

class HostTask(nn.Module):

    def __init__(self, host_graph: HostGraph) -> None:
        super().__init__()
        self.host_graph = host_graph
        self._modules: Dict[str, nn.Module] = {}
        self._buffers: Dict[str, torch.Tensor] = {}
        self._construct_operators()

    def _construct_operators(self) -> None:
        for n in self.host_graph.nodes:
            self._modules[n] = HostOperator(self.host_graph.config(n))

    def forward(self, *x: Tuple[torch.Tensor, ...]) -> torch.Tensor:
        for n in self.host_graph.nodes:
            if self.host_graph.is_input(n): # input operator
                input = x[self.host_graph.dicts[n]['bridge_idx']]
                self._buffers[n] = self._modules[n]([input])
            
            else:
                input_list = [self._buffers[pred] for pred in self.host_graph.preds(n)]
                res = self._modules[n](input_list)
                if self.host_graph.is_output(n): # output operator
                    return res
                self._buffers[n] = res


