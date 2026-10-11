"""Build a standalone category-bubble map from the catalog's resource notes."""

from pathlib import Path
import html
import json
import math
import re
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/diagrams"

# Each entry has one primary home. Its full task/category text remains searchable.
GROUPS = [
    ("engines", "Engines & interchange", "#deeae5", [
        ("SysML Toolkit", "SysML Toolkit"), ("OpenSysML", "OpenSysML"),
        ("SysML v2 Java pilot", "Java pilot"), ("SysML2.NET", "SysML2.NET"),
        ("OpenSysML v1 migration", "v1 migration"),
        ("OpenSysML diagram layout metadata", "Layout metadata"),
    ]),
    ("authoring", "Authoring & diagrams", "#deebf5", [
        ("Eclipse SysON", "SysON"), ("SysML v2 Language Server", "SysML v2 LSP"),
        ("SysML v2 VS Code Extension", "VS Code"),
        ("OpenMBEE web modeler", "Web modeler"),
        ("SysML React Flow components", "React Flow"),
        ("SysMD Notebook", "SysMD"), ("sysml-style", "sysml-style"),
    ]),
    ("libraries", "Libraries & model examples", "#f5e4cf", [
        ("Sysand", "Sysand"), ("Structured Use Cases", "Structured use cases"),
        ("Official libraries and examples", "Official models"),
        ("SYSMOD library", "SYSMOD"), ("Airbus Apollo 11 reference model", "Apollo 11"),
        ("GfSE SysML v2 model collection", "GfSE models"),
    ]),
    ("repositories", "Repositories & APIs", "#e4e3f3", [
        ("Flexo MMS SysML v2 microservice", "Flexo v2 API"),
        ("Flexo MMS Layer 1", "Flexo Layer 1"),
        ("OpenMBEE Python API client", "Python API client"),
        ("SysML v2 API Services pilot", "API pilot"),
        ("SysML v2 API Cookbook", "API Cookbook"),
    ]),
    ("analysis", "Analysis & integrations", "#f2dfe3", [
        ("SysML v2 geometry and Onshape connector", "Onshape connector"),
        ("FMPy", "FMPy"), ("StrictDoc", "StrictDoc"),
        ("Eclipse Lyo", "Eclipse Lyo"),
        ("Refinery SysML v2 Validator", "Refinery validator"),
    ]),
    ("evidence", "Evidence & reporting", "#dfedde", [
        ("Windseeker", "Windseeker"),
        ("OpenMBEE SysML v2 testing ledger", "Testing ledger"),
        ("OpenSysML service contract suite", "Contract suite"),
        ("OpenMBEE Cameo MDK and DocGen", "Cameo MDK"),
        ("OpenMBEE View Editor", "View Editor"),
    ]),
    ("agents", "AI skills & agents", "#f1e8c9", [
        ("DSG MBSE agent skills", "DSG MBSE skills"),
        ("OpenSysML agent skills", "OpenSysML skills"),
        ("Flexo MMS Layer 1 MCP server", "Flexo MCP"),
    ]),
    ("deployment", "Deployment & environments", "#dcecef", [
        ("Flexo MMS deployment", "Flexo deployment"),
        ("SysON Podman Compose recipe", "SysON Podman"),
    ]),
]
REVIEW = {
    "SysML v2 API Cookbook", "Airbus Apollo 11 reference model",
    "OpenSysML diagram layout metadata", "Windseeker", "sysml-style",
    "SysON Podman Compose recipe",
}
HOST = {"SysML v2 geometry and Onshape connector", "OpenMBEE Cameo MDK and DocGen"}


def slug(value):
    return re.sub(r"[^\w-]", "", value.lower().replace(" ", "-"))


def plain(value):
    return value.replace("`", "").replace("**", "")


def build():
    records = {}
    for section in re.split(r"^## ", (ROOT / "docs/resources.md").read_text(), flags=re.M)[1:]:
        title = section.splitlines()[0]
        fields = dict(re.findall(r"^- \*\*([^:]+):\*\* (.+)$", section, re.M))
        sources = fields.get("Sources", fields.get("Source", ""))
        upstream = re.search(r"\]\((https://[^)]+)\)", sources)
        records[title] = {
            "id": slug(title), "name": title,
            "purpose": plain(fields["Purpose"]), "tasks": plain(fields["Tasks/categories"]),
            "interfaces": plain(fields["Interfaces"]), "license": plain(fields["License"]),
            "limits": plain(fields["Limits"]),
            "notes": "../resources.md#" + slug(title),
            "upstream": upstream.group(1) if upstream else "",
            "access": "host" if title in HOST else "review" if title in REVIEW else
                "artifacts" if title == "Official libraries and examples" else "open",
        }
    nodes, groups, svg, assigned = [], [], [], []
    svg.append('<svg id="ecosystem-map" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1320 1320" role="img" aria-labelledby="ecosystem-map-title ecosystem-map-desc">')
    svg.append('<title id="ecosystem-map-title">SysML v2 and MBSE resource ecosystem</title><desc id="ecosystem-map-desc">Thirty-nine catalog resources grouped by primary role, with engines at the center and authoring, libraries, repositories, analysis, evidence, AI and deployment around them.</desc>')
    svg.append('<style>text{font-family:system-ui,sans-serif;fill:#26332f;text-anchor:middle;pointer-events:none}.category-title{font-size:20px;font-weight:650}.category-count{font-size:13px;fill:#596861}.tool-label{font-size:14px;font-weight:550}.tool-circle{fill:#ffffff;fill-opacity:.88;stroke:#ffffff;stroke-width:2}.access-review .tool-circle{stroke:#8b7352;stroke-dasharray:4 3}.access-host .tool-circle{stroke:#7b5760}.access-artifacts .tool-circle{stroke:#8b7352}.category-ring{stroke:#ffffff;stroke-width:2}</style>')
    svg.append('<circle class="ecosystem-boundary" cx="660" cy="660" r="630" fill="#f7f4e8"/>')
    for index, (gid, label, color, members) in enumerate(GROUPS):
        if index == 0:
            cx, cy = 660, 660
        else:
            angle = -math.pi / 2 + (index - 1) * 2 * math.pi / 7
            cx, cy = round(660 + 414 * math.cos(angle), 2), round(660 + 414 * math.sin(angle), 2)
        group = {"id": gid, "name": label, "color": color, "x": cx, "y": cy, "r": 176, "count": len(members)}
        groups.append(group)
        svg.append(f'<g class="category" data-category="{gid}" tabindex="0" role="button" aria-label="Explore {html.escape(label)}">')
        svg.append(f'<circle class="category-ring" cx="{cx}" cy="{cy}" r="176" fill="{color}"/>')
        svg.append(f'<text class="category-title" x="{cx}" y="{cy-144}">{html.escape(label)}</text><text class="category-count" x="{cx}" y="{cy-124}">{len(members)} resources</text>')
        count = len(members)
        for j, (name, short) in enumerate(members):
            record = dict(records[name], group=gid, short=short)
            if count == 7 and j == 6:
                dx, dy = 0, 24
            elif count == 2:
                dx, dy = (-60 if j == 0 else 60), 20
            else:
                ring_count = 6 if count == 7 else count
                angle = -math.pi / 2 + j * 2 * math.pi / ring_count
                radius = 100 if count >= 6 else 92 if count == 5 else 80
                dx, dy = radius * math.cos(angle), radius * math.sin(angle) + 24
            record.update(x=round(cx+dx, 2), y=round(cy+dy, 2), r=44)
            nodes.append(record); assigned.append(name)
            x,y = record["x"],record["y"]
            svg.append(f'<g class="resource access-{record["access"]}" data-resource="{record["id"]}" tabindex="0" role="button" aria-label="{html.escape(name)}">')
            svg.append(f'<title>{html.escape(name)}</title><circle class="tool-circle" cx="{x}" cy="{y}" r="44"/>')
            wrapped = textwrap.wrap(short, width=12, break_long_words=False)
            svg.append(f'<text class="tool-label" x="{x}" y="{y-(len(wrapped)-1)*8+5}">')
            for k, line in enumerate(wrapped):
                svg.append(f'<tspan x="{x}" dy="{0 if k==0 else 16}">{html.escape(line)}</tspan>')
            svg.append('</text></g>')
        svg.append('</g>')
    svg.append('</svg>')
    assert len(assigned) == len(set(assigned)) and set(assigned) == set(records), "Primary placement must cover every catalog entry exactly once"
    for group in groups:
        children = [n for n in nodes if n["group"] == group["id"]]
        for i,a in enumerate(children):
            assert math.hypot(a["x"]-group["x"],a["y"]-group["y"])+a["r"] <= group["r"], a["name"]
            for b in children[i+1:]:
                assert math.hypot(a["x"]-b["x"],a["y"]-b["y"]) >= a["r"]+b["r"]+4, (a["name"],b["name"])
    for i,a in enumerate(groups):
        for b in groups[i+1:]:
            assert math.hypot(a["x"]-b["x"],a["y"]-b["y"]) >= a["r"]+b["r"]+4
    svg_text = "\n".join(svg)
    nav = ''.join(f'<button class="category-nav" data-group="{g["id"]}"><span class="swatch" style="background:{g["color"]}"></span><span>{html.escape(g["name"])}</span><span class="nav-count">{g["count"]}</span></button>' for g in groups)
    listing = ''.join(f'<li data-list-resource="{n["id"]}"><a href="{n["notes"]}" data-resource-link="{n["id"]}">{html.escape(n["name"])}</a></li>' for n in sorted(nodes,key=lambda n:n['name'].lower()))
    data = json.dumps({"groups":groups,"resources":nodes},ensure_ascii=False).replace('</','<\\/')
    template = (ROOT / "scripts/templates/ecosystem-map.html").read_text()
    for marker,content in {"__SVG__":svg_text,"__NAV__":nav,"__LIST__":listing,"__DATA__":data,"__COUNT__":str(len(nodes))}.items():
        template=template.replace(marker,content)
    OUT.mkdir(exist_ok=True)
    (OUT / "ecosystem-bubbles.html").write_text(template)
    (OUT / "ecosystem-bubbles.svg").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+svg_text+'\n')
    print(f'Built {len(nodes)} resources in {len(groups)} groups; unique placement, containment and spacing verified.')


if __name__ == "__main__":
    build()
