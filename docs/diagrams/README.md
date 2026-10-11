# SysML v2 and MBSE ecosystem map

[Open the interactive HTML](ecosystem.html) or [view the SVG](ecosystem.svg). Download the HTML and open it locally; GitHub does not execute the viewer. The HTML is standalone and offers light/dark themes, node exploration and image exports.

## Scope and meaning

This is an architecture-style ecosystem overview with representative resources, not a deployment architecture or exhaustive inventory of the catalog's 39 entries.

The upper rows show roles: agent guidance, standards, reusable libraries, authoring, interchange, engines, model services, analysis, portals, evidence and adjacent engineering integrations. Dashed arrows express conceptual relationships; a particular tool pair still needs integration and version checks.

The lower example shows selected documented Flexo connections: the Python API client accesses the SysML v2 adapter, that adapter uses Layer 1, and the MCP server accesses Layer 1 separately. Solid arrows reflect documentation review, not reproduced runtime behavior. Deployment examples support setting up the stack.

View Editor and Cameo MDK are legacy workflow references. Direct View Editor-to-Flexo compatibility and native v2 support remain unverified. Open-source code licensing, proprietary host access and unresolved artifact terms are separate concerns; consult [resource notes](../resources.md) and the catalog's access sections.

## Sources and maintenance

[Editable diagram specification](ecosystem.architecture.json) records component sources against catalog commit `af53ca244f2ecec1a438b4c706f31ce098f37fcf`, reviewed on 2026-10-11. These are catalog documentation sources with upstream links, not an independent audit of each implementation. Update the source ranges and pinned catalog revision when revising the map.

Generated with [Archify](https://github.com/tt-a1i/archify). With its CLI installed and Node available, run from the catalog root:

```bash
node "$ARCHIFY_CLI" finalize architecture \
  docs/diagrams/ecosystem.architecture.json \
  docs/diagrams/ecosystem.html --repo-root . --quality showcase --json
```

Set `ARCHIFY_CLI` to the installed `bin/archify.mjs` path. Export the SVG from the checked HTML's export menu. Archify is an authoring tool, not a runtime dependency of the catalog or standalone viewer. Local delivery/browser receipts are ignored; preserve them when reproducing a review.

The generated HTML and SVG are retained verbatim. Git attributes mark them as generated and exempt their generator-supplied trailing whitespace; authored Markdown and JSON retain normal whitespace checks.

## Recorded checks

- Showcase validation, artifact delivery, provenance check and automated browser checks passed without diagnostics.
- Light/dark browser captures of the same HTML bytes were visually inspected; the SVG was exported using the viewer's canonical export.
- Specification SHA-256: `d7e93d4a78c0647b324e003f12424eb900be1d4aa7ac8fa36318079c5adb7289`.
- HTML SHA-256: `19497df4587c069121f1fc4c5cc211d59c429b95cba13f1b4a4e512e37c46840`.

Diagram checks establish artifact integrity and presentation, not SysML conformance or engineering approval. The SVG is a communication export; the HTML and specification retain the interactive map and evidence context.
