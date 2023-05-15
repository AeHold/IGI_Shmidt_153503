import re
from abc import ABC, abstractmethod
from types import NoneType, FunctionType, MethodType, CodeType, ModuleType,\
CellType, BuiltinMethodType, BuiltinFunctionType, WrapperDescriptorType,\
MethodDescriptorType, MappingProxyType, GetSetDescriptorType, MemberDescriptorType
from typing import Any, IO, Hashable, Collection, Iterable

from utils.constants import TYPE_MAPPING

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
        return TYPE_MAPPING[re.search(pattern, s).group(1)]
    
    def get_items(self, obj) -> dict[str, Any]:
        if isinstance(obj, (BuiltinFunctionType, BuiltinMethodType)):
            return {}
        
        if isinstance(obj, dict):
            return obj
        
        elif isinstance(obj, Collection):
            return dict(enumerate(obj))
        
        elif isinstance(obj, CodeType):
            return {
                "argcount": obj.co_argcount,
                "posonlyargcount": obj.co_posonlyargcount,
                "kwonlyargcount": obj.co_kwonlyargcount,
                "nlocals": obj.co_nlocals,
                "stacksize": obj.co_stacksize,
                "flags": obj.co_flags,
                "code": obj.co_code,
                "consts": obj.co_consts,
                "names": obj.co_names,
                "varnames": obj.co_varnames,
                "filename": obj.co_filename,
                "name": obj.co_name,
                "firstlineno": obj.co_firstlineno,
                "lnotab": obj.co_lnotab,
                "freevars": obj.co_freevars,
                "cellvars": obj.co_cellvars,
            }
        
        elif isinstance(obj, FunctionType):
            if obj.__closure__ and "__class__" in obj.__code__.co_freevars:
                closure = ([... for _ in obj.__closure__])if
            elif obj.__closure__:
                closure = ([cell.cell_contents for cell in obj.__closure__])
            else:
                closure = None
            return {
                "argcount": obj.__code__.co_argcount,
                "posonlyargcount": obj.__code__.co_posonlyargcount,
                "kwonlyargcount": obj.__code__.co_kwonlyargcount,
                "nlocals": obj.__code__.co_nlocals,
                "stacksize": obj.__code__.co_stacksize,
                "flags": obj.__code__.co_flags,
                "code": obj.__code__.co_code,
                "consts": obj.__code__.co_consts,
                "names": obj.__code__.co_names,
                "varnames": obj.__code__.co_varnames,
                "filename": obj.__code__.co_filename,
                "name": obj.__code__.co_name,
                "firstlineno": obj.__code__.co_firstlineno,
                "lnotab": obj.__code__.co_lnotab,
                "freevars": obj.__code__.co_freevars,
                "cellvars": obj.__code__.co_cellvars,
                "globals": {
                    k: obj.__globals__[k]
                    for k in (
                        set(
                            k for k, v in obj.__globals__.items()
                            if isinstance(v, ModuleType)
                        ) |
                        set(obj.__globals__) &
                        set(obj.__code__.co_names) -
                        {obj.__name__}
                    )
                },
                "closure": closure,
                "qualname": obj.__qualname__
            }
        
        elif isinstance(obj, MethodType):
            return {
                "__func__": obj.__func__,
                "__self__": obj.__self__
            }
        
        elif issubclass(type(obj), type):
            return {
                'name': obj.__name__,
                'mro': tuple(obj.mro()[1:-1]),
                'attrs': {
                    k: v for k, v in obj.__dict__.items()
                    if(
                        k not in self._IGNORED_FIELDS and
                        type(v) not in self._IGNORED_FIELD_TYPES
                    )
                }
            }
        
        elif issubclass(type(obj), ModuleType):
            return {'name': obj.__name__}
        
        elif isinstance(obj, staticmethod):
            return self.get_items(obj.__func__)
        
        elif isinstance(obj, classmethod):
            return self.get_items(obj.__func__)
        
        else:
            return {
                'class': obj.__class__,
                'attrs': {
                    k: v for k, v in obj.__dict__.items()
                    if (
                        k not in self._IGNORED_FIELDS and
                        type(k) not in self._IGNORED_FIELD_TYPES
                    )
                }
            }