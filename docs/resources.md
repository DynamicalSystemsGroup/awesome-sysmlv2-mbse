# Resource notes

These records summarize upstream documentation reviewed on **2026-10-11**. Unless an entry states otherwise, that date is its last review, the evidence level is **documentation reviewed**, and maintenance activity and exact release compatibility are **not assessed**. No local execution was performed for this catalog. An accessible repository alone does not establish active maintenance. Sources point to moving upstream pages unless stated otherwise. Pin a release and exact sources before relying on compatibility or comparing implementations.

Entries distinguish tools, libraries, example models, deployment recipes, and technical reference material. A generic integration component is labeled explicitly rather than presented as a ready-made SysML v2 integration.

## SysML Toolkit

- **Purpose:** Rust toolchain for authoring, converting, checking, and analyzing SysML v2/KerML models.
- **Tasks/categories:** Build, analyze, validate; engine, LSP, formatter, lint, interchange, solver, visualization.
- **Interfaces:** Rust crates, CLI, language server/VS Code client, Python and WebAssembly bindings.
- **License:** Apache-2.0 for the toolkit; bundled artifacts can have separate terms.
- **Specification target:** README identifies SysML 2.0/KerML 1.0 and metamodel `20250201`; exact release compatibility has not been independently checked.
- **Getting started:** Follow the upstream CLI or SDK guides for conversion, checking, expression evaluation, and PlantUML views.
- **Limits:** Semantic coverage is partial; supported solving fragments and behavior execution boundaries matter. Its CBOR encoding is project-specific.
- **Sources:** [Repository and README](https://github.com/Open-MBEE/sysml-toolkit), [CLI guide](https://github.com/Open-MBEE/sysml-toolkit/blob/main/CLI.md), [SDK guide](https://github.com/Open-MBEE/sysml-toolkit/blob/main/SDK.md), [interchange](https://github.com/Open-MBEE/sysml-toolkit/blob/main/INTEROP.md).

## OpenSysML

- **Purpose:** Go runtime and development kit for model authoring and execution.
- **Tasks/categories:** Build, analyze, validate; engine, editor services, expressions, action/state execution.
- **Interfaces:** Go API, CLI/REPL, language server, service and client bindings; model-derived Markdown/HTML/PDF documents.
- **License:** Apache-2.0 for the repository; inspect dependency/library terms for your distribution.
- **Specification target:** Current README describes SysML v2 and KerML 1.1; this is a project declaration, not a compatibility assessment against the formal versions linked in the catalog.
- **Getting started:** Use the upstream installation guide and small runtime examples; choose a pinned artifact for evaluations.
- **Limits:** Feature support and extensions need checking for a specific model. No conformance certification is inferred from documentation or pilot comparisons.
- **Sources:** [Repository, guide, and capability documentation](https://github.com/Open-MBEE/OpenSysML), [document generation manual](https://opensysml.org/manual/).

## SysML v2 Java pilot

- **Purpose:** Pilot implementation of textual notation and visualization.
- **Tasks/categories:** Build, analyze, validate; language implementation, textual editor, diagrams, notebook integration.
- **Interfaces:** Java/Eclipse/Xtext components, Jupyter integration, PlantUML components.
- **License:** Repository identifies EPL-2.0; check artifact-specific terms.
- **Specification target:** Release-dependent SysML v2/KerML support; exact target not recorded in this initial review.
- **Getting started:** Follow the official release repository's installation material and the pilot's development instructions.
- **Limits:** A pilot is useful comparison evidence, but is not an unquestionable oracle for the standard. Installation requirements depend on the selected release.
- **Sources:** [Pilot repository](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation), [release and installation material](https://github.com/Systems-Modeling/SysML-v2-Release).

## Eclipse SysON

- **Purpose:** Open-source web tooling for editing SysML v2 models.
- **Tasks/categories:** Build, analyze; graphical and structured editing, visualization.
- **Interfaces:** Web editors built on Sirius Web; upstream describes graphical, textual, form-based, and table-oriented editing.
- **License:** Repository lists EPL-2.0 and LGPL-3.0 components; check the selected distribution.
- **Specification target:** SysML v2; exact supported release not assessed.
- **Getting started:** Follow the project website and documentation to try the modeling interfaces.
- **Limits:** Verify editor and exchange support in a chosen release. Graphical editing does not establish editable diagram portability to another product.
- **Sources:** [Repository](https://github.com/eclipse-syson/syson), [project website](https://mbse-syson.org/).

## Sysand

- **Purpose:** Package manager and index tooling for SysML v2 and KerML libraries.
- **Tasks/categories:** Build; dependencies, packages, registries.
- **Interfaces:** CLI and integration APIs; documentation describes public and private indexes.
- **License:** MIT OR Apache-2.0.
- **Specification target:** Based on model interchange projects, referencing KerML clause 10.3; library compatibility is package-specific.
- **Getting started:** Use its client documentation to install the tool and resolve or publish packages.
- **Limits:** Package resolution does not prove that a consuming engine supports the packaged model. Pin package and engine versions separately.
- **Sources:** [Repository and licensing](https://github.com/sensmetry/sysand), [client documentation](https://docs.sysand.com/client/).

## Structured Use Cases

- **Purpose:** SysML v2 library for structured use-case specifications and scenarios.
- **Tasks/categories:** Build; reusable domain libraries, scenario modeling, behavioral testing concepts.
- **Interfaces:** Importable SysML models, examples, and documentation.
- **License:** Apache-2.0.
- **Specification target:** SysML v2 extension library; exact engine/release compatibility not assessed.
- **Getting started:** Read the upstream examples and import the library into a compatible modeling environment.
- **Limits:** The project describes a proposed alternative library for OMG consideration. Do not treat that proposal as an adopted normative library or as a standalone execution/test engine.
- **Source:** [Repository, library, and examples](https://github.com/Open-MBEE/structured-use-cases).

## Official libraries and examples

- **Purpose:** Release repository containing specifications, model libraries, examples, training, and installation material.
- **Tasks/categories:** Build; reusable libraries, reference models, developer onboarding.
- **Interfaces:** Downloadable release artifacts and model files.
- **License:** Check licenses for the selected artifact; this catalog does not assign one license to the whole collection.
- **Specification target:** Varies by release; select a named release and retain its identity.
- **Getting started:** Read the repository README, select a release, and use examples with a compatible implementation.
- **Limits:** Distinguish normative libraries from informative examples. Example acceptance alone does not establish complete conformance.
- **Source:** [SysML v2 Release repository](https://github.com/Systems-Modeling/SysML-v2-Release).

## Flexo MMS SysML v2 microservice

- **Purpose:** REST/HTTP service implementing the platform-specific mapping for the Systems Modeling API and Services.
- **Tasks/categories:** Supporting infrastructure; model access, repositories, integration.
- **Interfaces:** REST/HTTP, Gradle/JDK development and Docker deployment instructions.
- **License:** Apache-2.0.
- **Specification target:** Systems Modeling API and Services; exact supported specification revision not assessed.
- **Getting started:** Follow upstream configuration and Compose documentation, including prerequisite services.
- **Limits:** API access and persistence do not establish language validation, simulation support, or engineering correctness. Test endpoint coverage against the selected deployment.
- **Source:** [Repository and setup instructions](https://github.com/Open-MBEE/flexo-mms-sysmlv2).

## Flexo MMS Layer 1

- **Purpose:** Graph-native repository service for version-controlled CRUD operations on RDF models, underlying the Flexo SysML v2 adapter.
- **Tasks/categories:** Analyze, supporting infrastructure; repositories, model queries, revision management.
- **Interfaces:** HTTP service and OpenAPI artifacts; quadstore backend with RDF/SPARQL interfaces.
- **License:** Apache-2.0; backend and complementary services have separate terms.
- **Specification target:** RDF model management, not a SysML language engine. Systems Modeling API access is provided by the separate SysML v2 adapter.
- **Getting started:** Follow the deployment guide, configure a quadstore, and initialize deployment-specific cluster data.
- **Limits:** Repository versioning does not establish semantic merge or model validation. The README describes development setup; Flexo's RDF architecture is not a drop-in replacement for Exec MMS's JSON architecture.
- **Sources:** [Repository and license](https://github.com/Open-MBEE/flexo-mms-layer1-service), [architecture overview](https://github.com/Open-MBEE), [deployment guide](https://flexo-mms-deployment-guide.readthedocs.io/en/latest/).

## Flexo MMS deployment

- **Purpose:** Deployment examples and configuration documentation for the Flexo MMS service stack.
- **Tasks/categories:** Supporting infrastructure; deployment, local environments, service integration.
- **Interfaces:** Docker Compose examples, Kubernetes manifests, and documentation for quadstore, authentication and storage configuration.
- **License:** Apache-2.0 for the repository; deployed images and services retain their own terms.
- **Specification target:** Flexo infrastructure; SysML/API compatibility depends on the selected service artifacts.
- **Getting started:** Select an upstream deployment example and follow its initialization and service configuration instructions.
- **Limits:** Example manifests do not establish production readiness or compatibility across arbitrary service versions. Pin artifacts and assess upgrades, access controls and recovery for the intended environment. No deployment was performed for this catalog.
- **Sources:** [Repository and license](https://github.com/Open-MBEE/flexo-mms-deployment), [deployment documentation](https://flexo-mms-deployment-guide.readthedocs.io/en/latest/).

## OpenMBEE View Editor

- **Purpose:** Web portal for viewing and modifying model-derived documents and values held in MMS, including cross-references between documents.
- **Tasks/categories:** Analyze, supporting infrastructure; stakeholder portals, documents, collaboration.
- **Interfaces:** Browser application, configurable MMS endpoint, static web or Docker deployment.
- **License:** Apache-2.0 for `exec-ve`; backend, integrations and optional publishing dependencies have separate terms.
- **Host/service requirements:** Requires a compatible MMS backend. The documented browser workflow does not require opening MagicDraw; authoring integrations can have separate product requirements.
- **Specification target:** Execubots/legacy MBSE ecosystem; native SysML v2 and direct Flexo Layer 1 compatibility were not established.
- **Getting started:** Use the repository's build/configuration instructions and user guide with a compatible backend.
- **Limits:** Distinguish this portal from the SysML v2 web modeler. Existing MMS endpoint configuration does not establish interoperability with the newer Flexo stack.
- **Sources:** [Canonical repository and license](https://github.com/Open-MBEE/exec-ve), [user guide](https://docs.openmbee.org/projects/ve/en/latest/about.html), [architecture context](https://github.com/Open-MBEE).

## SysML v2 Language Server

- **Purpose:** ANTLR4/TypeScript language server with navigation, diagnostics, structural complexity analysis, Mermaid previews, and an MCP interface.
- **Tasks/categories:** Build, analyze, validate; editing, language services, metrics, visualization, integration.
- **Interfaces:** LSP, VS Code, browser and Python example clients, MCP CLI.
- **License:** MIT.
- **Specification target:** SysML v2; exact grammar and semantic coverage require release-specific checking.
- **Getting started:** Use the upstream quick start or dev container and client examples.
- **Limits:** Listed checks and previews do not establish complete semantics or behavior equivalence; preview diff modes are not a general semantic merge engine.
- **Source:** [daltskin/sysml-v2-lsp](https://github.com/daltskin/sysml-v2-lsp).

## SysML v2 VS Code Extension

- **Purpose:** VS Code modeling interface combining textual authoring and interactive diagrams.
- **Tasks/categories:** Build, analyze, validate; editing, model exploration, visualization.
- **Interfaces:** VS Code extension; language features use `sysml-v2-lsp`.
- **License:** MIT.
- **Specification target:** Declares SysML v2.0; exact compatibility not assessed.
- **Getting started:** Open a `.sysml` file and use the model visualizer; follow installation links in the README.
- **Limits:** This is a frontend over language tooling, not an independent conformance oracle. Diagram views and image export are distinct from portable editable diagram exchange.
- **Source:** [daltskin/VSCode_SysML_Extension](https://github.com/daltskin/VSCode_SysML_Extension).

## SysML2.NET

- **Purpose:** C# SDK and reference web application for working with SysML v2 metamodel objects and representations.
- **Tasks/categories:** Build, supporting infrastructure; SDKs, serialization, interchange, repository clients.
- **Interfaces:** NuGet libraries for metamodel, semantics, JSON, XMI, MessagePack, textual notation, KPAR, REST and data access; reference viewer.
- **License:** Apache-2.0 libraries/application, with LGPL-3.0 metamodel-related files identified upstream.
- **Specification target:** README identifies generation from pilot commit `f1fd2b83e460f5695e8edcd780f43909f359d299`, described as Beta 4.
- **Getting started:** Choose the relevant NuGet packages and inspect reference application examples.
- **Limits:** Check metamodel vintage and serializer behavior against a chosen formal specification before exchanging data with another implementation.
- **Source:** [STARIONGROUP/SysML2.NET](https://github.com/STARIONGROUP/SysML2.NET).

## OpenMBEE web modeler

- **Purpose:** Container-oriented Java service for browser visualization and textual editing against a SysML v2 API backend.
- **Tasks/categories:** Build, analyze, validate, supporting infrastructure; web interfaces, rendering, API integration.
- **Interfaces:** Browser viewer/editor, HTTP endpoints, Pilot runtime, Docker.
- **License:** Apache-2.0 for the service; bundled Pilot and library terms are separate.
- **Specification target:** Dependent on supplied Pilot jars and backend API; exact compatibility not assessed.
- **Getting started:** Follow upstream container and backend configuration instructions.
- **Limits:** Repository-loaded models can fall back to generated SysML-like text. Commits replace the model rather than offering general conflict-aware merging; remote timeouts and Pilot JSON-loading limits are documented.
- **Source:** [Open-MBEE/sysmlv2-web-modeler](https://github.com/Open-MBEE/sysmlv2-web-modeler).

## OpenMBEE Python API client

- **Purpose:** Python client for model repository operations, with upstream testing focused on Flexo.
- **Tasks/categories:** Build, analyze, supporting infrastructure; APIs, automation, repository navigation.
- **Interfaces:** Python APIs for projects, commits, branches, tags, elements and relationships; notebook examples.
- **License:** Apache-2.0.
- **Specification target:** Systems Modeling API and Services; exact revision and non-Flexo compatibility not assessed.
- **Getting started:** Follow the README and example notebook; imports include `sysmlv2_client`. Check publication status before assuming a registry install is available.
- **Limits:** Repository CRUD does not validate the engineering meaning of changes. Test endpoint/authentication behavior for the selected server.
- **Source:** [Open-MBEE/sysmlv2-python-client](https://github.com/Open-MBEE/sysmlv2-python-client).

## SysML v2 API Services pilot

- **Purpose:** Proof-of-concept implementation of the REST/HTTP Systems Modeling API.
- **Tasks/categories:** Supporting infrastructure; persistence, model services, integration experiments.
- **Interfaces:** REST/HTTP and API documentation; JVM service with PostgreSQL.
- **License:** EPL-2.0 as identified by the repository.
- **Specification target:** Release-dependent API pilot; exact formal-version coverage not assessed.
- **Getting started:** Select a release and follow its database, JVM, and service setup instructions.
- **Limits:** The master README describes Play/sbt rather than Spring Boot; avoid inheriting framework claims from third-party lists. A pilot deployment is not proof of production readiness or full API coverage.
- **Source:** [Systems-Modeling/SysML-v2-API-Services](https://github.com/Systems-Modeling/SysML-v2-API-Services).

## SysML v2 API Cookbook

- **Purpose:** Notebook recipes for exploring models and managing repository revisions through the API.
- **Tasks/categories:** Build, analyze, supporting infrastructure; queries, decomposition, branching, API learning.
- **Interfaces:** Jupyter notebooks making REST/HTTP calls.
- **License:** Not established by the reviewed README; inspect artifact terms before reuse.
- **Specification target:** Release-dependent Systems Modeling API recipes.
- **Getting started:** Try the decomposition, project/commit/branch/tag, element CRUD, owned-element, and query recipes against a compatible test server.
- **Limits:** Examples are executable learning material, not a service or general semantic diff/merge tool. Adapt endpoints and payloads to your server version.
- **Source:** [Systems-Modeling/SysML-v2-API-Cookbook](https://github.com/Systems-Modeling/SysML-v2-API-Cookbook).

## SysML v2 geometry and Onshape connector

- **Purpose:** CAD-agnostic assembly representation and Onshape integration expressed through SysML-oriented geometry tooling.
- **Tasks/categories:** Build, analyze; CAD connectors, assembly structure, geometry interchange.
- **Interfaces:** Python `geometry_api`, `onshape_connector`, and transformation utilities.
- **License:** Apache-2.0 for the repository; bundled helpers/dependencies need their own review.
- **Host/service requirements:** Onshape connector operations require Onshape workspace access and API credentials; the generic geometry utilities are separate from that service dependency.
- **Specification target:** SysML v2 domain integration; exact schema/library compatibility not assessed.
- **Getting started:** Read the examples and connector configuration; test a small assembly before a larger workflow.
- **Limits:** Assembly ownership and placement exchange does not imply complete CAD geometry or bidirectional semantic synchronization. Onshape operations require configured access.
- **Source:** [Open-MBEE/sysmlv2_dls](https://github.com/Open-MBEE/sysmlv2_dls).

## SYSMOD library

- **Purpose:** Reusable SysML v2 definitions and examples implementing the SYSMOD engineering methodology.
- **Tasks/categories:** Build, analyze; methodology libraries, requirements patterns, architecture allocations, traceability.
- **Interfaces:** Importable `.sysml` library, delivery-drone examples, Sysand package link.
- **License:** Apache-2.0.
- **Specification target:** SysML v2 extension; exact engine compatibility not assessed.
- **Getting started:** Import `SYSMOD` and study the example project; requirement boilerplates provide quantitative patterns.
- **Limits:** The library organizes engineering artifacts; its prompts and process definitions do not independently verify requirements or approve a design.
- **Source:** [MBSE4U/sysmod-sysmlv2](https://github.com/MBSE4U/sysmod-sysmlv2).

## Airbus Apollo 11 reference model

- **Purpose:** Multi-layer mission model and research artifact illustrating architecture and traceability through the CoSMA framework.
- **Tasks/categories:** Build, analyze, validate; reference models, realistic evaluation inputs, architecture/requirement traceability.
- **Interfaces:** SysML model files, scripts, dependency documentation and research citation metadata.
- **License:** See the repository's `LICENSE.md`; identifier not established in this review.
- **Specification target:** SysML v2; use its dependency documentation to choose engine and library versions.
- **Getting started:** Follow the top-level model and architecture layers rather than loading isolated files without dependencies.
- **Limits:** Upstream explicitly describes an incomplete research scaffold. Treat it as an example and evaluation input, not a fully validated mission design or universal methodology.
- **Source:** [airbus/apollo-11-sysml-v2](https://github.com/airbus/apollo-11-sysml-v2).

## GfSE SysML v2 model collection

- **Purpose:** Curated model collection for teaching, reuse, and tool-development experiments.
- **Tasks/categories:** Build, validate; reference models, test inputs, model collections.
- **Interfaces:** Textual models with descriptions and repository CI material.
- **License:** BSD-3-Clause by default; subdirectory-specific licenses can override it.
- **Specification target:** Model-specific; exact release compatibility not assessed.
- **Getting started:** Select one model and read its accompanying documentation and license.
- **Limits:** The collection can include good and bad examples; inclusion alone is not a positive conformance verdict. Preserve individual model provenance and expected outcomes when using it as test data.
- **Source:** [GfSE/SysML-v2-Models](https://github.com/GfSE/SysML-v2-Models).

## SysON Podman Compose recipe

- **Purpose:** Small deployment recipe for running the SysON development environment with Podman Compose.
- **Tasks/categories:** Supporting infrastructure; deployment, local modeling environments.
- **Interfaces:** `compose.yaml`, Podman Compose and browser access.
- **License:** Not established in the reviewed repository; deployment image licenses are separate.
- **Specification target:** Depends on the selected SysON image.
- **Getting started:** Read the Compose file and upstream instructions; pin images for reproducible use.
- **Limits:** A development recipe does not provide production security, backups, upgrade policy, or maintenance guarantees.
- **Source:** [mycr0ft/SysON_podman_compose](https://github.com/mycr0ft/SysON_podman_compose).

## SysML React Flow components

- **Purpose:** TypeScript/React building blocks for creating SysML v2 diagram interfaces.
- **Tasks/categories:** Build, analyze; diagramming SDK, graphical interfaces, layout.
- **Interfaces:** Node/edge renderers, typed factories, viewpoints, and elkjs-based automatic layout.
- **License:** MIT.
- **Specification target:** Declares SysML v2.0; upstream completeness claims have not been independently checked.
- **Getting started:** Follow the component examples and layout documentation in a React Flow application.
- **Limits:** Diagram components are not a semantic engine or an established cross-tool diagram interchange contract.
- **Source:** [Hollando78/SysML-reactflow](https://github.com/Hollando78/SysML-reactflow).

## OpenSysML v1 migration

- **Purpose:** Experimental migration from SysML v1 UML/XMI exports into SysML v2, with per-element mapping reports.
- **Tasks/categories:** Build; migration, legacy model reuse, mapping diagnostics.
- **Interfaces:** OpenSysML migration CLI and client interfaces; optional MTIP layout augment.
- **License:** Part of the Apache-2.0 OpenSysML repository.
- **Specification target:** Implementation-specific migration; compare selected mappings against the OMG transformation specification.
- **Getting started:** Use the migration guide with a small exported model and inspect mapped, approximated, unmapped, and skipped report entries.
- **Limits:** Experimental and potentially lossy; units are not migrated according to the reviewed guide. Native diagram geometry requires separate handling. Supported content can change between releases.
- **Source:** [OpenSysML migration guide](https://github.com/Open-MBEE/OpenSysML/blob/develop/docs/reference/sysml-v1-migration.md).

## OpenSysML diagram layout metadata

- **Purpose:** Non-normative metadata library and tool support for retaining per-view geometry in textual models.
- **Tasks/categories:** Build, analyze; editable layouts, diagram presentation exchange experiments.
- **Interfaces:** Layout, route, canvas, style, note and picture metadata; renderer/editor support described upstream.
- **License:** Inspect the extension library's selected artifact terms; the design is documented in the Apache-2.0 OpenSysML repository.
- **Specification target:** SysML metadata extension, not an adopted OMG diagram-interchange standard.
- **Getting started:** Follow the guide's annotated-view example and check behavior in the chosen renderer.
- **Limits:** An implementation reading/writing its own metadata does not establish that another tool preserves or renders it. Cross-tool portability remains to be tested.
- **Source:** [Diagram layout design and implementation notes](https://github.com/Open-MBEE/OpenSysML/blob/develop/docs/project/diagram-layout-annotations.md).

## SysMD Notebook

- **Purpose:** Notebook environment combining model cells and Markdown with constraint-based value and unit analysis.
- **Tasks/categories:** Build, analyze, validate; notebooks, calculations, constraint solving, documentation.
- **Interfaces:** SysML v2/KerML model cells, solver and notebook UI.
- **License:** Apache-2.0.
- **Specification target:** SysML v2/KerML subset; exact revision not established.
- **Getting started:** Follow the README examples and supported-language section.
- **Limits:** Views and time slices are among documented omissions; constraint propagation has behavior-related limits. Do not infer complete language coverage or general simulation.
- **Source:** [tukcps/SysMD](https://github.com/tukcps/SysMD).

## Windseeker

- **Purpose:** Automate package dependency ordering, SysML notebook execution, and rendered-view extraction.
- **Tasks/categories:** Analyze, validate; dependency analysis, reports, execution automation, CI building block.
- **Interfaces:** CLI, Jupyter notebooks, installed SysML kernel, generated images.
- **License:** MIT according to publisher metadata; license-file verification remains open.
- **Specification target:** Depends on the chosen kernel and models.
- **Getting started:** Read the publisher's workflow and select the intended distribution before installation.
- **Limits:** Analysis is documented at top-level package/import granularity. `windseeker` and `sysml-windseeker` are both published names; their equivalence was not established. Failure exit codes support automation but do not constitute a complete CI service.
- **Sources:** [windseeker publisher page](https://pypi.org/project/windseeker/), [sysml-windseeker publisher page](https://pypi.org/project/sysml-windseeker/).

## sysml-style

- **Purpose:** Configurable style checking and formatting for textual models, based on sysmlpy.
- **Tasks/categories:** Build, validate; formatter, lint, authoring policy, CI building block.
- **Interfaces:** Check/format CLI with failure exit codes.
- **License:** Unknown; no explicit license established in the reviewed page. Inclusion is license-unverified.
- **Specification target:** SysML v2 textual style; exact supported revision not assessed.
- **Getting started:** Review configuration and CLI examples upstream.
- **Limits:** Style policy does not establish semantic correctness. Confirm license and parser compatibility before adoption.
- **Source:** [mycr0ft/sysml-style](https://github.com/mycr0ft/sysml-style).

## Refinery SysML v2 Validator

- **Purpose:** Fetch model elements through the API, transform them into a graph-solver representation, and check user-defined patterns.
- **Tasks/categories:** Analyze, validate; graph analysis, engineering rules, validation portal.
- **Interfaces:** API pipeline, Refinery patterns, interpreted findings, browser/Jupyter showcase.
- **License:** Apache-2.0 as stated in the README.
- **Specification target:** SysML v2 API workflow; exact API revision and server compatibility not assessed.
- **Getting started:** Follow the showcase and choose a model commit and validation patterns.
- **Limits:** A pattern's applicability and normative basis need review; user rules are not automatically language-conformance obligations. Archive status was not established in this review.
- **Source:** [ftsrg/sysmlv2-validator](https://github.com/ftsrg/sysmlv2-validator).

## FMPy

- **Purpose:** Run Functional Mock-up Units from Python for model exchange and co-simulation workflows.
- **Tasks/categories:** Analyze; external simulation, parameter studies, notebook integration.
- **Interfaces:** Python, CLI, GUI/web and notebook interfaces; documented FMI 1.0/2.0/3.0 support.
- **License:** BSD-2-Clause with third-party notices.
- **Specification target:** FMI, not SysML. This is an adjacent integration building block.
- **Getting started:** Run an FMU using upstream examples, then design any model-to-simulation mapping separately.
- **Limits:** No native SysML v2 connector was established. Mapping variables, units, parameters and results remains an integration responsibility.
- **Sources:** [CATIA-Systems/FMPy](https://github.com/CATIA-Systems/FMPy), [license and notices](https://github.com/CATIA-Systems/FMPy/blob/main/LICENSE.txt).

## OpenMBEE Cameo MDK and DocGen

- **Purpose:** Cameo plugin for MMS synchronization and generating model-based documents through views and viewpoints.
- **Tasks/categories:** Analyze, supporting infrastructure; document generation, reporting, repository integration.
- **Interfaces:** Cameo/No Magic plugin and DocGen workflow.
- **License:** Apache-2.0 plugin; host-product access and dependency terms are separate.
- **Host/service requirements:** Requires the proprietary Cameo/No Magic host; the plugin's open-source license does not cover host-product access.
- **Specification target:** Legacy Cameo/SysML ecosystem; native SysML v2 support not established.
- **Getting started:** Follow the MDK DocGen guide and sample models in a supported host version.
- **Limits:** Useful as a related MBSE resource and workflow precedent; do not present it as a drop-in v2 reporting solution.
- **Sources:** [Open-MBEE/exec-cameo-mdk](https://github.com/Open-MBEE/exec-cameo-mdk), [DocGen guide](https://docs.openmbee.org/projects/mdk/en/latest/docgen.html).

## StrictDoc

- **Purpose:** File-based requirements and technical documentation with traceability and generated reports.
- **Tasks/categories:** Build, analyze; requirements, traceability, reporting, interchange building block.
- **Interfaces:** Requirement files, source/test links, traceability matrix, HTML reports, ReqIF import/export.
- **License:** Apache-2.0.
- **Specification target:** Generic requirements tooling; native SysML v2 integration not established.
- **Getting started:** Follow the feature documentation and ReqIF conversion guidance.
- **Limits:** ReqIF mappings vary by tool/profile. A connector to SysML elements and revision-bound links would require separate assessment.
- **Sources:** [strictdoc-project/strictdoc](https://github.com/strictdoc-project/strictdoc), [features](https://strictdoc-project.github.io/features/), [ReqIF guidance](https://strictdoc.readthedocs.io/en/stable/stable/docs/strictdoc_01_user_guide-TRACE.html).

## Eclipse Lyo

- **Purpose:** Java SDK for developing OSLC lifecycle integrations using REST and RDF.
- **Tasks/categories:** Supporting infrastructure; traceability connectors, lifecycle integration, validation building block.
- **Interfaces:** Client/server/domain/store libraries, tracked resource sets, validation components.
- **License:** EPL-2.0 and Eclipse Distribution License files; inspect module-specific notices.
- **Specification target:** Generic OSLC tooling; exact SysML v2/Systems Modeling API mapping support not established.
- **Getting started:** Select the relevant SDK modules and review adapter lifecycle status.
- **Limits:** SDK modules are not ready-made connectors for every engineering product. Upstream distinguishes current and historical adapters.
- **Source:** [eclipse-lyo/lyo](https://github.com/eclipse-lyo/lyo).

## OpenMBEE SysML v2 testing ledger

- **Purpose:** Record implementation runs and assessment evidence in a knowledge-graph ledger using EARL and PROV-O.
- **Tasks/categories:** Validate, supporting infrastructure; implementation testing, reports, reproducibility, provenance.
- **Interfaces:** Pinned runs, retained raw outputs, comparison pipeline, Turtle/SHACL and readable reports.
- **License:** Apache-2.0.
- **Specification target:** Case-, implementation-, and version-specific; complete language coverage not established.
- **Getting started:** Read the documented execution/assessment workflow and select reviewed test expectations.
- **Limits:** Ledger SHACL checks validate evidence structure, not SysML semantics. Described human review does not prove every case has been approved or an engine certified. Affiliation: DSG's catalog concerns OpenMBEE collaboration; this entry receives the same evidence label as external resources.
- **Source:** [Open-MBEE/sysmlv2-testing](https://github.com/Open-MBEE/sysmlv2-testing).

## OpenSysML service contract suite

- **Purpose:** Scenario fixtures and runners check expected service responses across client transports.
- **Tasks/categories:** Validate, supporting infrastructure; contract tests, regression testing, CI reports.
- **Interfaces:** RPC request/response fixtures, gRPC/Connect/Connect JSON runners, JSON and JUnit results.
- **License:** Part of the Apache-2.0 OpenSysML repository.
- **Specification target:** OpenSysML-specific service contract, not the standardized Systems Modeling REST API.
- **Getting started:** Follow the suite README and run selected scenarios against a pinned service/client pair.
- **Limits:** A passing service contract suite does not certify OMG language conformance or establish equivalence between independent engines.
- **Source:** [OpenSysML conformance suite README](https://github.com/Open-MBEE/OpenSysML/blob/develop/conformance/README.md).
