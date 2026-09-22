from __future__ import annotations
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Iterable

class ExecutionClass(StrEnum):
    SCANNER="scanner"; FUZZER="fuzzer"; RESEARCH="research"; VALIDATOR="validator"; EXPLOIT="exploit"

@dataclass(frozen=True)
class ResearchRepository:
    name: str
    url: str
    execution_class: ExecutionClass
    version: str|None=None
    license: str|None=None
    capabilities: tuple[str,...]=()
    inputs: tuple[str,...]=()
    outputs: tuple[str,...]=()
    dependencies: tuple[str,...]=()
    execution_requirements: tuple[str,...]=()
    destructive: bool=False
    requires_authorization: bool=True
    resource_limits: dict[str,int|float]=field(default_factory=dict)
    adapter: str|None=None
    parser: str|None=None
    evidence_mapping: dict[str,str]=field(default_factory=dict)
    @property
    def safe_by_default(self)->bool: return not self.destructive

class ResearchRegistry:
    def __init__(self,repositories:Iterable[ResearchRepository]=()):
        self._repositories={}
        for r in repositories: self.register(r)
    def register(self,r:ResearchRepository)->None:
        if r.name in self._repositories: raise ValueError(f"duplicate research repository: {r.name}")
        self._repositories[r.name]=r
    def get(self,name:str)->ResearchRepository: return self._repositories[name]
    def all(self)->tuple[ResearchRepository,...]: return tuple(self._repositories[k] for k in sorted(self._repositories))
    def by_class(self,c:ExecutionClass)->tuple[ResearchRepository,...]: return tuple(r for r in self.all() if r.execution_class==c)
    def safe(self,*,authorized:bool,include_destructive:bool=False)->tuple[ResearchRepository,...]:
        return tuple(r for r in self.all() if (authorized or not r.requires_authorization) and (include_destructive or not r.destructive))
    def eligible(self,*,authorized:bool,safe_mode:bool=True)->tuple[ResearchRepository,...]:
        return self.safe(authorized=authorized,include_destructive=not safe_mode)
