# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from ethicml.data.tabular_data.admissions import AdmissionsSplits
from ethicml.data.tabular_data.adult import AdultSplits
from ethicml.data.tabular_data.compas import CompasSplits
from ethicml.data.tabular_data.credit import CreditSplits
from ethicml.data.tabular_data.crime import CrimeSplits
from ethicml.data.tabular_data.german import GermanSplits
from ethicml.data.tabular_data.health import HealthSplits
from ethicml.data.tabular_data.law import LawSplits
from ethicml.data.tabular_data.sqf import SqfSplits
from omegaconf import MISSING
from ranzen.torch.data import TrainingMode
from typing import Any
from typing import Optional


@dataclass
class AdmissionsDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.AdmissionsDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: AdmissionsSplits = AdmissionsSplits.GENDER
    disc_feats_only: bool = False


@dataclass
class AdultDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.AdultDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    bin_nationality: bool = False
    sens_feat: AdultSplits = AdultSplits.SEX
    bin_race: bool = False
    disc_feats_only: bool = False


@dataclass
class CompasDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.CompasDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: CompasSplits = CompasSplits.SEX
    disc_feats_only: bool = False


@dataclass
class CreditDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.CreditDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: CreditSplits = CreditSplits.SEX
    disc_feats_only: bool = False


@dataclass
class CrimeDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.CrimeDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: CrimeSplits = CrimeSplits.RACE_BINARY
    disc_feats_only: bool = False


@dataclass
class GermanDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.GermanDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: GermanSplits = GermanSplits.SEX
    disc_feats_only: bool = False


@dataclass
class HealthDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.HealthDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: HealthSplits = HealthSplits.SEX
    disc_feats_only: bool = False


@dataclass
class LawDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.LawDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: LawSplits = LawSplits.SEX
    disc_feats_only: bool = False


@dataclass
class SqfDataModuleConf:
    _target_: str = "conduit.fair.data.datamodules.SqfDataModule"
    train_batch_size: int = 64
    eval_batch_size: Optional[int] = None
    val_prop: float = 0.2
    test_prop: float = 0.2
    num_workers: int = 0
    seed: int = 47
    persist_workers: bool = False
    pin_memory: bool = True
    stratified_sampling: bool = False
    instance_weighting: bool = False
    training_mode: TrainingMode = TrainingMode.epoch
    scaler: Any = MISSING  # ScalerType
    invert_s: bool = False
    sens_feat: SqfSplits = SqfSplits.SEX
    disc_feats_only: bool = False
