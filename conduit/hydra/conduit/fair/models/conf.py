# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from conduit.fair.misc import FairnessType
from omegaconf import MISSING
from ranzen.torch.data import TrainingMode
from typing import Any
from typing import Optional


@dataclass
class DANNConf:
    _target_: str = "conduit.fair.models.DANN"
    adv: Any = MISSING  # Module
    enc: Any = MISSING  # Module
    clf: Any = MISSING  # Module
    lr: float = 0.0003
    weight_decay: float = 0.0
    grl_lambda: float = 1.0
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1


@dataclass
class ERMClassifierFConf:
    _target_: str = "conduit.fair.models.ERMClassifierF"
    encoder: Any = MISSING  # Module
    clf: Any = MISSING  # Module
    lr: float = 0.0003
    weight_decay: float = 0.0
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1
    loss_fn: Any = None  # Optional[Loss]


@dataclass
class FairMixupConf:
    _target_: str = "conduit.fair.models.FairMixup"
    encoder: Any = MISSING  # Module
    clf: Any = MISSING  # Module
    lr: float = MISSING
    weight_decay: float = MISSING
    fairness: FairnessType = MISSING
    mixup_lambda: Optional[float] = None
    alpha: float = 1.0
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1


@dataclass
class GPDConf:
    _target_: str = "conduit.fair.models.GPD"
    adv: Any = MISSING  # Module
    enc: Any = MISSING  # Module
    clf: Any = MISSING  # Module
    lr: float = 0.0003
    weight_decay: float = 0.0
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1


@dataclass
class KCConf:
    _target_: str = "conduit.fair.models.KC"
    encoder: Any = MISSING  # Module
    clf: Any = MISSING  # Module
    lr: float = 0.0003
    weight_decay: float = 0.0
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1


@dataclass
class LAFTRConf:
    _target_: str = "conduit.fair.models.LAFTR"
    lr: float = MISSING
    weight_decay: float = MISSING
    disc_steps: int = MISSING
    fairness: FairnessType = MISSING
    recon_weight: float = MISSING
    clf_weight: float = MISSING
    adv_weight: float = MISSING
    enc: Any = MISSING  # Module
    dec: Any = MISSING  # Module
    adv: Any = MISSING  # Module
    clf: Any = MISSING  # Module
    lr_initial_restart: int = 10
    lr_restart_mult: int = 2
    lr_sched_interval: TrainingMode = TrainingMode.epoch
    lr_sched_freq: int = 1
