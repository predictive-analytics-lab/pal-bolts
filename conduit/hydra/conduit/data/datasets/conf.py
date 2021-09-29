# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass
from conduit.data.datasets.vision.isic import IsicAttr
from conduit.data.datasets.vision.ssrp import SSRPSplit
from omegaconf import MISSING
from typing import Any
from typing import Dict
from typing import List
from typing import Optional


@dataclass
class CelebAConf:
    _target_: str = "conduit.data.datasets.CelebA"
    root: Any = MISSING  # Union[str, Path]
    download: bool = True
    superclass: Any = smiling  # Union[CelebAttr, str]
    subclass: Any = male  # Union[CelebAttr, str]
    transform: Any = None  # Union[Compose, BasicTransform, Callable[[Image], Any], NoneType]
    split: Any = None  # Union[CelebASplit, str, NoneType]


@dataclass
class ColoredMNISTConf:
    _target_: str = "conduit.data.datasets.ColoredMNIST"
    root: Any = MISSING  # Union[str, Path]
    download: bool = True
    transform: Any = None  # Union[Compose, BasicTransform, Callable[[Image], Any], NoneType]
    label_map: Optional[Dict[str, int]] = None
    colors: Optional[List[int]] = None
    num_colors: int = 10
    scale: float = 0.2
    correlation: float = 1.0
    binarize: bool = False
    greyscale: bool = False
    background: bool = False
    black: bool = True
    split: Any = None  # Union[ColoredMNISTSplit, str, NoneType]


@dataclass
class ISICConf:
    _target_: str = "conduit.data.datasets.ISIC"
    root: Any = MISSING  # Union[str, Path]
    download: bool = True
    max_samples: int = 25000
    context_attr: IsicAttr = histo
    target_attr: IsicAttr = malignant
    transform: Any = None  # Union[Compose, BasicTransform, Callable[[Image], Any], NoneType]


@dataclass
class NICOConf:
    _target_: str = "conduit.data.datasets.NICO"
    root: Any = MISSING  # Union[str, Path]
    download: bool = True
    transform: Any = None  # Union[Compose, BasicTransform, Callable[[Image], Any], NoneType]
    superclass: Any = animals  # Union[NicoSuperclass, str, NoneType]


@dataclass
class SSRPConf:
    _target_: str = "conduit.data.datasets.SSRP"
    root: Any = MISSING  # Union[str, Path]
    split: Any = SSRPSplit.pretrain  # Union[SSRPSplit, str]
    download: bool = True
    transform: Any = None  # Union[Compose, BasicTransform, Callable[[Image], Any], NoneType]


@dataclass
class WaterbirdsConf:
    _target_: str = "conduit.data.datasets.Waterbirds"
    root: Any = MISSING  # Union[str, Path]
    download: bool = True
    transform: Any = None  # Union[Compose, BasicTransform, Callable[[Image], Any], NoneType]
    split: Any = None  # Union[WaterbirdsSplit, str, NoneType]
