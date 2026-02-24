# Docs Index｜V∞ Constitutional AIOS Bus (Reference)

Welcome. This folder contains the canonical documentation for the **V∞ Origin Compiler-Executor** reference repository.

Repository (main):  
https://github.com/liangfeng-hu/V-infinity-Origin-Compiler-Executor-Reference/tree/main

Tactical PoC repo (DistillGuard / PoAIW cut-in):  
https://github.com/liangfeng-hu/Cosmic-Seed-DistillGuard-Reference/tree/main

---

## 1) Start Here (Recommended Reading Order)

1. **Verification Report (Sealed)**  
   - `verification-report.md` — repository-level verification and sealing statement

2. **10-Page Decks (EN / ZH)**  
   - `v-infinity-10page-deck.en.md` — VC 10-page deck (English)  
   - `v-infinity-10page-deck.zh.md` — VC 10-page deck (中文)

3. **Strategic Documents**  
   - `v-infinity-aios-blueprint.md` — the V∞ AIOS bus blueprint (CTO/CISO/board-level)  
   - `vision-and-beyond.md` — trillion-dollar extensions and industrial mapping  
   - `extension-roadmap.md` — six “killer” extensions (evidence-only, no new gates)

---

## 2) Core Engineering Docs

- `integration-guide.md` — 3 integration modes (sidecar / agent needle-eye / gateway) + checklists  
- `threat-model-and-solution.md` — threat table, defense mapping, stable reason codes  
- `intent-distill-recognition.md` — reference evidence fields for extraction intent (Gate90)  
- `lse-meta-axiom.md` — LSE meta-axiom definition, BudgetOK hook, product closure  
- `gate91-spec.md` — Gate91 physical decidability interface and reason codes

---

## 3) Where the “Truth” Lives

- Constitution (canonical): `../CONSTITUTION.md`  
- Interface specs (OpenAPI): `../spec/`  
- Runnable reference demo: `../reference-impl/python/demo.py`  
- Governance boundary & disclosure: `../SECURITY.md`, `../NOTICE`, `../CONTRIBUTING.md`

---

## 4) Intended Use (Reference Boundary)

This is a **reference repository** for:
- sealed semantics (Fail-Closed, CommitUnique, AuditCard closure)
- interface shapes (OpenAPI)
- integration guidance and governance positioning

It intentionally does **NOT** ship production ZKP circuits, operational keys, real attestation chains, or a real π_seed generator.

---

## 5) 中文简要说明
本目录为 V∞ 总线参考实现的文档入口页，建议按“验收报告 → 10页Deck → 战略文件 → 工程文档”的顺序阅读。  
本仓库为语义/接口/审计闭包参考实现，不包含生产级 ZKP/真实硬件证明链/真实 π_seed 发生器。
