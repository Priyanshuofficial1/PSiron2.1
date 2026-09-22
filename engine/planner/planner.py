from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from engine.planner.capability import CapabilityCatalog, PlannedCapability, TargetProfile

@dataclass(frozen=True)
class AssessmentPlan:
    target: TargetProfile
    capabilities: tuple[PlannedCapability, ...]
    @property
    def tools(self) -> tuple[str, ...]:
        return tuple(sorted({t for p in self.capabilities for t in p.tools}))

class DeterministicPlanner:
    def __init__(self, catalog: CapabilityCatalog) -> None:
        self.catalog = catalog
    def plan(self, target: TargetProfile) -> AssessmentPlan:
        planned = []
        for c in self.catalog.applicable(target):
            parts = [f"target kind={target.kind}"]
            if c.required_inputs: parts.append("inputs=" + ",".join(c.required_inputs))
            matched = sorted(set(c.technologies) & set(target.technologies))
            if matched: parts.append("technologies=" + ",".join(matched))
            planned.append(PlannedCapability(c, c.tools, "; ".join(parts)))
        return AssessmentPlan(target, tuple(planned))
    def plan_from_values(self, *, kind: str, inputs: Iterable[str] = (), technologies: Iterable[str] = ()) -> AssessmentPlan:
        return self.plan(TargetProfile.from_values(kind=kind, inputs=inputs, technologies=technologies))
