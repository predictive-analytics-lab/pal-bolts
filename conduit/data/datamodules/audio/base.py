"""Base class for audio datasets."""
from pathlib import Path
from typing import Optional, Union

import attr
from ranzen.decorators import implements
from typing_extensions import final

from conduit.data.datamodules.base import CdtDataModule
from conduit.data.datasets.utils import AudioTform
from conduit.data.datasets.wrappers import AudioTransformer, InstanceWeightedDataset
from conduit.types import Stage

__all__ = ["CdtAudioDataModule"]


@attr.define(kw_only=True)
class CdtAudioDataModule(CdtDataModule):

    root: Union[str, Path] = attr.field(kw_only=False)
    _train_transforms: Optional[AudioTform] = None
    _test_transforms: Optional[AudioTform] = None

    @property
    @final
    def train_transforms(self) -> Optional[AudioTform]:
        return self._train_transforms

    @train_transforms.setter
    def train_transforms(self, transform: Optional[AudioTform]) -> None:
        self._train_transforms = transform
        if isinstance(self._train_data, AudioTransformer):
            self._train_data.transform = transform

    @property
    @final
    def test_transforms(self) -> Optional[AudioTform]:
        return self._test_transforms

    @test_transforms.setter
    @final
    def test_transforms(self, transform: Optional[AudioTform]) -> None:
        self._test_transforms = transform
        if isinstance(self._val_data, AudioTransformer):
            self._val_data.transform = transform
        if isinstance(self._test_data, AudioTransformer):
            self._test_data.transform = transform

    @implements(CdtDataModule)
    @final
    def _setup(self, stage: Optional[Stage] = None) -> None:
        train, val, test = self._get_splits()
        train = AudioTransformer(train, transform=self.train_transforms)
        if self.instance_weighting:
            train = InstanceWeightedDataset(train)
        self._train_data = train
        self._val_data = AudioTransformer(val, transform=self.test_transforms)
        self._test_data = AudioTransformer(test, transform=self.test_transforms)
