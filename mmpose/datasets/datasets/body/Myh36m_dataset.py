from mmpose.registry import DATASETS
from mmpose.datasets.datasets.base import BaseCocoStyleDataset

@DATASETS.register_module(name='Myh36mDataset')
class Myh36mDataset(BaseCocoStyleDataset):
    METAINFO: dict = dict(from_file='configs/_base_/datasets/Myh36m.py')