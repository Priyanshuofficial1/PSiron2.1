from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class EvidenceEdge:
    source: str
    relationship: str
    target: str

class EvidenceGraph:
    ALLOWED_RELATIONSHIPS = frozenset({"supported_by", "produced_by", "executed_against", "verified_by"})
    def __init__(self, edges: Iterable[EvidenceEdge] = ()):
        self._edges = set()
        for edge in edges:
            self.add_edge(edge)
    def add_edge(self, edge: EvidenceEdge) -> None:
        if edge.relationship not in self.ALLOWED_RELATIONSHIPS:
            raise ValueError(f"unsupported evidence relationship: {edge.relationship}")
        if not edge.source or not edge.target:
            raise ValueError("evidence graph nodes cannot be empty")
        self._edges.add(edge)
    def link(self, source: str, relationship: str, target: str) -> EvidenceEdge:
        edge = EvidenceEdge(source, relationship, target)
        self.add_edge(edge)
        return edge
    def edges(self) -> tuple[EvidenceEdge, ...]:
        return tuple(sorted(self._edges, key=lambda e: (e.source, e.relationship, e.target)))
    def related(self, source: str, relationship: str | None = None) -> tuple[str, ...]:
        return tuple(sorted(e.target for e in self._edges if e.source == source and (relationship is None or e.relationship == relationship)))
    def has_provenance(self, finding_id: str) -> bool:
        return bool(self.related(finding_id, "supported_by"))
    def trace(self, finding_id: str) -> tuple[EvidenceEdge, ...]:
        return tuple(e for e in self.edges() if e.source == finding_id or e.target == finding_id)
