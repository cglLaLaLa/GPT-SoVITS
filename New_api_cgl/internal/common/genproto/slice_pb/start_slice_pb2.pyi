from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SliceRequest(_message.Message):
    __slots__ = ("input_path", "output_root", "threshold", "min_length", "min_interval", "hop_size", "max_sil_kept", "_max", "alpha", "n_parts")
    INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ROOT_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MIN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    HOP_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_SIL_KEPT_FIELD_NUMBER: _ClassVar[int]
    _MAX_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    N_PARTS_FIELD_NUMBER: _ClassVar[int]
    input_path: str
    output_root: str
    threshold: float
    min_length: int
    min_interval: int
    hop_size: int
    max_sil_kept: int
    _max: int
    alpha: float
    n_parts: int
    def __init__(self, input_path: _Optional[str] = ..., output_root: _Optional[str] = ..., threshold: _Optional[float] = ..., min_length: _Optional[int] = ..., min_interval: _Optional[int] = ..., hop_size: _Optional[int] = ..., max_sil_kept: _Optional[int] = ..., _max: _Optional[int] = ..., alpha: _Optional[float] = ..., n_parts: _Optional[int] = ...) -> None: ...

class StartResponse(_message.Message):
    __slots__ = ("status", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    data: _containers.RepeatedCompositeFieldContainer[KeyValuePair]
    def __init__(self, status: _Optional[str] = ..., data: _Optional[_Iterable[_Union[KeyValuePair, _Mapping]]] = ...) -> None: ...

class KeyValuePair(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
