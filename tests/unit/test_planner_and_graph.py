from engine.coverage.coverage import CoverageRecord
from engine.planner.capability import Capability, CapabilityCatalog, TargetProfile
from engine.planner.planner import DeterministicPlanner
from graph.evidence_graph import EvidenceGraph

def catalog():
    return CapabilityCatalog([
        Capability("web.recon", required_inputs=("url",), target_kinds=("web",), tools=("httpx", "nmap")),
        Capability("web.xss", required_inputs=("url",), target_kinds=("web",), tools=("dalfox",)),
        Capability("source.web-security", required_inputs=("git",), target_kinds=("source",), tools=("semgrep",)),
    ])

def test_planning_is_deterministic():
    planner = DeterministicPlanner(catalog())
    target = TargetProfile.from_values(kind="web", inputs=["url"], technologies=["nextjs"])
    assert planner.plan(target) == planner.plan(target)

def test_capabilities_are_input_driven():
    planner = DeterministicPlanner(catalog())
    assert [x.capability.id for x in planner.plan_from_values(kind="web", inputs=["url"]).capabilities] == ["web.recon", "web.xss"]
    assert [x.capability.id for x in planner.plan_from_values(kind="source", inputs=["git"]).capabilities] == ["source.web-security"]

def test_evidence_graph_preserves_provenance():
    graph = EvidenceGraph()
    graph.link("finding-1", "supported_by", "evidence-1")
    graph.link("evidence-1", "produced_by", "toolrun-1")
    graph.link("toolrun-1", "executed_against", "asset-1")
    assert graph.has_provenance("finding-1")
    assert graph.related("finding-1", "supported_by") == ("evidence-1",)

def test_coverage_calculation():
    coverage = CoverageRecord()
    coverage.discover("a", "b", "c")
    coverage.mark_tested("a", "b", "not-discovered")
    assert coverage.covered == {"a", "b"}
    assert coverage.uncovered == {"c"}
    assert coverage.ratio == 2 / 3
