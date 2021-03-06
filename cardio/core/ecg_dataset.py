"""Contains ECG Dataset class."""

from .. import dataset as ds
from .ecg_batch import EcgBatch


class EcgDataset(ds.Dataset):
    """Dataset that generates batches of ``EcgBatch`` class.

    Contains indices of ECGs and a specific ``batch_class`` to create and
    process batches - small subsets of data.

    Parameters
    ----------
    index : DatasetIndex or None, optional
        Unique identifiers of ECGs in a dataset. If ``index`` is not given, it
        is constructed by instantiating ``index_class`` with ``args`` and
        ``kwargs``.
    batch_class : type, optional
        Class of batches, generated by dataset. Must be inherited from
        ``Batch``.
    preloaded : tuple, optional
        Data to put in created batches. Defaults to ``None``.
    index_class : type, optional
        Class of built index if ``index`` is not given. Must be inherited from
        ``DatasetIndex``.
    args : misc, optional
        Additional positional argments to ``index_class.__init__``.
    kwargs : misc, optional
        Additional named argments to ``index_class.__init__``.
    """

    def __init__(self, index=None, batch_class=EcgBatch, preloaded=None, index_class=ds.FilesIndex, *args, **kwargs):
        if index is None:
            index = index_class(*args, **kwargs)
        super().__init__(index, batch_class, preloaded)
