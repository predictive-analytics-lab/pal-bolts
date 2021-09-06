from __future__ import annotations
from enum import Enum
from typing import Any, Dict, Union

from kit.torch.loss import ReductionType
from pytorch_lightning.utilities.types import _METRIC_COLLECTION
from torch import Tensor
from torch.optim.lr_scheduler import CosineAnnealingWarmRestarts, ExponentialLR, StepLR
from typing_extensions import Protocol

__all__ = [
    "LRScheduler",
    "Loss",
    "MetricDict",
    "Stage",
]


class Loss(Protocol):
    def __call__(self, input: Tensor, target: Tensor, **kwargs: Any) -> Tensor:
        ...

    @property
    def reduction(self) -> ReductionType | str:
        ...

    @reduction.setter
    def reduction(self, value: ReductionType | str) -> None:
        ...


class Stage(Enum):
    fit = "fit"
    validate = "validate"
    test = "test"

    def __str__(self) -> str:
        return str(self.value)


LRScheduler = Union[CosineAnnealingWarmRestarts, ExponentialLR, StepLR]
MetricDict = Dict[str, _METRIC_COLLECTION]