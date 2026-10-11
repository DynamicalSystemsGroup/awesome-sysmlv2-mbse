# Contributing and maintaining resources

Help developers and systems engineers choose tools for building, analyzing, and validating models. Keep entries short, useful, and grounded in the project's own sources.

## Inclusion

Include a resource when it has a concrete SysML v2 or related MBSE workflow, a public source or documentation link, and enough information to explain its purpose. Open-source tools are the initial focus. Clearly identify commercial, mixed-license, archived, experimental, and proposed resources. Include non-SysML tools only when their MBSE integration is explained.

Do not rank by stars or repeat marketing claims as verified findings. Apply the same criteria to affiliated and external projects; disclose relevant affiliations when recommending or evaluating tools. Link to other curated lists for discovery, but check claims against primary sources.

## Add or update an entry

1. Check existing entries to avoid duplicate records.
2. Use [the resource template](docs/resource-template.md) for a canonical record in `docs/resources.md`; longer evaluations may live in separate Markdown notes.
3. Add or update the appropriate README category links. A tool can serve several tasks while having one canonical record.
4. Cite sources for capabilities, license, supported versions, limitations, and lifecycle status. Write `unknown` or `not assessed` when evidence is missing.
5. Record the date and scope of the review. Preserve any older test evidence and its exact version; a documentation update does not refresh a test result.
6. Review the rendered Markdown, local links/anchors, and changed external links before proposing the change.

## Evidence levels

| Label | Meaning |
| --- | --- |
| Discovered | Candidate link; capability details have not been reviewed |
| Documentation reviewed | Primary sources inspected; capabilities remain upstream claims |
| Locally tested | A specific operation reproduced with pinned inputs, tool/library versions, environment, commands, and retained results |

Evidence levels apply to specific claims. A tested parser does not make all runtime capabilities tested. Keep upstream self-reported results, our observations, and reviewer conclusions separate. Never claim certification from a comparison or a passing example.

Track maintenance separately using sourced descriptions such as `archived upstream`, `deprecated upstream`, or `not assessed`. Dates of commits/releases can be recorded as observations without declaring overall project health.

## Update routine

Suggested manual cadence: review entries monthly, and sooner after a relevant release, deprecation, broken-link report, or reported limitation. This is a proposed maintenance practice; no scheduled automation or owner is configured.

During a review:

- Check canonical URLs, archive/deprecation notices, release notes, licenses, specification targets, and setup documentation.
- Update changed claims and record the sources and review date. Leave unreviewed entries' dates unchanged.
- Mark unavailable links or uncertain claims explicitly; retain a migration/replacement link when upstream provides one.
- Revisit categories with few resources and confirm that listed tools still fit their tasks.

Link availability is only one check. Automated link checks, if added later, must not label functionality, compatibility, or maintenance as verified.

## Coverage backlog

Use [coverage and open questions](docs/coverage.md) to identify where the current collection has direct tools, examples, integration components, or only partial evidence. Prioritize semantic diff/merge, verified editable diagram interchange, native simulation/traceability connectors, domain rules, and complete CI workflows. Sparse catalog coverage is not proof of an ecosystem gap.

Before public release, choose a catalog license and maintenance owner. Do not copy third-party descriptions verbatim; summarize and cite them. Upstream software and model licenses remain separate from the catalog's license.
