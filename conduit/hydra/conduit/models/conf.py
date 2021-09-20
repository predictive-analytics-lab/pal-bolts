# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from kit.torch.data import TrainingMode
from omegaconf import MISSING
from typing import Any


@dataclass
class ERMClassifierConf:
    _target_: str = "conduit.models.ERMClassifier"
    model: Any = MISSING  # Module
    lr: float = 0.0003
    weight_decay: float = 0.0
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1
    loss_fn: Any = None  # Optional[Loss]
