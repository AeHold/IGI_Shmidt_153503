import re
from abc import ABC, abstractmethod
from types import NoneType, FunctionType, MethodType, CodeType, ModuleType,\
CellType, BuiltinMethodType, BuiltinFunctionType, WrapperDescriptorType,\
MethodDescriptorType, MappingProxyType, GetSetDescriptorType, MemberDescriptorType
from typing import Any, IO, Hashable, Collection, Iterable


class Serializer(ABC):
    _IGNORED_FIELDS: set[str] = (
        '__weakref__',
        '__subclasshook__',
        '__dict__',
        '__doc__'
    )
    _IGNORED_FIELD_TYPES: set[str] = (
        BuiltinFunctionType, BuiltinMethodType,
        WrapperDescriptorType, MethodDescriptorType,
        MappingProxyType, GetSetDescriptorType,
        MemberDescriptorType
    )
    
    @staticmethod
    def __get_key(value: Hashable, obj: dict):
        return [key for key in obj if obj[key] == value][0]
    
    @classmethod
    def _type_from_str(cls, s: str, pattern: str) -> type:
        if not re.search(pattern, s):
            return NoneType