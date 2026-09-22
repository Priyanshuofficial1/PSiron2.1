from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, Mapping

@dataclass(frozen=True)
class TargetProfile:
    kind: str
    inputs: tuple[str, ...] = ()
    technologies: tuple[str, ...] = ()
    attributes: Mapping[str, str] = field(default_factory=dict)
    @classmethod
    def from_values(cls, *, kind: str, inputs: Iterable[str] = (), technologies: Iterable[str] = (), attributes: Mapping[str, str] | None = None) -> "TargetProfile":
        return cls(kind.strip().lower(), tuple(sorted({str(v).strip().lower() for v in inputs if str(v).strip()})), tuple(sorted({str(v).strip().lower() for v in technologies if str(v).strip()})), dict(sorted((attributes or {}).items())))

@dataclass(frozen=True)
class Capability:
    id: str
    description: str = ""
    required_inputs: tuple[str, ...] = ()
    target_kinds: tuple[str, ...] = ()
    technologies: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()

@dataclass(frozen=True)
class PlannedCapability:
    capability: Capability
    tools: tuple[str, ...]
    reason: str

class CapabilityCatalog:
    def __init__(self, capabilities: Iterable[Capability] = ()) -> None:
        self._capabilities = {c.id: c for c in capabilities}
    def add(self, capability: Capability) -> None:
        if capability.id in self._capabilities: raise ValueError(f"duplicate capability: {capability.id}")
        self._capabilities[capability.id] = capability
    def get(self, capability_id: str) -> Capability: return self._capabilities[capability_id]
    def all(self) -> tuple[Capability, ...]: return tuple(self._capabilities[k] for k in sorted(self._capabilities))
    def applicable(self, target: TargetProfile) -> tuple[Capability, ...]:
        result = []
        for c in self.all():
            if c.target_kinds and target.kind not in c.target_kinds: continue
            if c.required_inputs and not set(c.required_inputs).issubset(target.inputs): continue
            if c.technologies and not (set(c.technologies) & set(target.technologies)): continue
            result.append(c)
        return tuple(result)
