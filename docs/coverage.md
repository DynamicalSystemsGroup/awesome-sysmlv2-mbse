# Coverage and open questions

Collection reviewed on 2026-10-11. The task-based README maps the agreed build, analyze, validate and infrastructure categories to described resources. Sources and limitations are recorded in [resource notes](resources.md). This is a bounded primary-source collection, not an exhaustive market survey.

## How to read coverage

| Area | What the collection establishes | Remaining question |
| --- | --- | --- |
| Editors, engines and SDKs | Several documented implementation and frontend options | Exact language obligations and release compatibility |
| Libraries, packages and reference models | Importable libraries, package tooling and model collections | Compatibility, individual licenses and model expectations |
| Interchange and migration | Serialization libraries and an experimental migration implementation | Cross-engine semantic preservation and losses |
| Diagrams and editable layouts | Renderers, component libraries and a non-normative layout extension | Two-tool preservation of editable presentation and geometry |
| Queries, dependencies and impact | API recipes, package ordering and structural metrics | General semantic change-impact analysis |
| Constraints and engineering validation | Solver workflows and user-defined validation patterns | Reviewed rule meaning, applicability and undecided outcomes |
| Traceability, CAD and simulation | Modeling examples, one CAD integration and adjacent integration components | Native connectors and result mappings for specific tool pairs |
| Reporting and portals | Model interfaces, notebooks and document-generation workflows | Revision-bound reports and stakeholder-specific needs |
| Testing, CI and provenance | Ledgers, contract runners and CLI automation hooks | Independent conformance scope and complete model-change workflows |
| Collaboration and diff/merge | Branch/commit recipes, web interfaces and API contracts | Conflict semantics and a general cross-engine semantic merge utility |
| AI skills and agents | General MBSE skills, engine-specific skills and MCP tool interfaces | Client invocation, workflow effectiveness and complete agent applications |
| Deployment | Development recipes and service setup documentation | Reviewed production operation and upgrade behavior |

## Important distinctions

- **Direct SysML resources:** implementations, editors, libraries, model collections and SysML API clients.
- **Adjacent integration components:** FMPy, StrictDoc and Eclipse Lyo are useful for simulation, requirements and lifecycle integrations. Their inclusion does not imply a ready-made native SysML v2 connector.
- **Legacy MBSE resources:** View Editor and Cameo MDK/DocGen illustrate model-based documentation and repository integration; native v2 support was not established. View Editor backend compatibility with Flexo also remains unverified.
- **Project-specific tests/extensions:** OpenSysML's service suite and layout metadata have defined local contracts. Neither is an OMG certification or an adopted diagram-interchange standard.

## Further collection and review

Investigate concrete semantic diff/merge utilities, cross-tool diagram interchange, requirement verification adapters, domain rule libraries and complete CI integrations. Extend coverage with additional engines, editors, libraries and commercial options when their role and access terms are clear.

For current entries, the next deeper review would pin source revisions, verify uncertain licenses/publication names, record lifecycle notices and test selected workflows. Missing or uncertain coverage is an evidence limit, not proof that tools do not exist. No automated upkeep, runtime evaluation, release publication or upstream endorsement is claimed by this collection.
