# V∞-Origin-Compiler-Executor Reference (V∞ AIOS Bus)

**本源编译执行器通用宪法（13母律）× GateVectorLen=91 × LSE元公理**  
**V∞ Constitutional AIOS Bus Reference Implementation**

本仓库展示一种“跨越数字与物理鸿沟”的 **AGI 操作系统底层总线**：  
强制任何高价值输出与任何世界写回（ΔΩ_t）必须锚定 **因果连续性（Gate90）** 与 **物理做功证据（Gate91）**，并以 **LSE 元公理**焊死为乘积闭包；不满足即 Fail-Closed。

---

## ✅ 永久冻结（不可破锁）
- GateVectorLen ≡ 91（不新增任何门）
  - Gate90：I_AWAKE_SCORE（意图/因果/时间）
  - Gate91：I_ENTROPY_CLONE（物理/熵增/硬件证据）
- LSE 元公理（第0元门）：Intent × Temporal × Physical 必须同时 Complete
- Fail-Closed 永不弱化（任意失败 → ΔΩ_t=0 且 CommitUnique=0）
- CommitUnique 为唯一针眼（任何世界写回必须经由它）
- 扩展只允许进入：Gate90.intent_audit_group 或 AuditCard_t（只加证据字段）

> 说明：本仓库不包含生产级 ZKP 电路、真实硬件 attestation 链、真实 π_seed 发生器；仅提供参考语义、接口形状与审计闭包结构。

---

## 🚀 Quick Start（30秒）
```bash
python reference-impl/python/demo.py
你会看到 4 个场景输出 + AuditCard_t 全息审计卡（含 evidence_keys 可复算）。

📖 核心文档

CONSTITUTION.md
 —— V∞ 宪法正本（13母律 + LSE + Gate90/91）

docs/vision-and-beyond.md
 —— 万亿级场景白皮书

docs/extension-roadmap.md
 —— 6条杀手锏路线图

docs/v-infinity-aios-blueprint.md
 —— 战略总线蓝皮书

docs/integration-guide.md
 —— 3种零侵入集成模式

spec/*.openapi.json —— 可直接Mock的工业接口

🛡️ Security

请先阅读：

SECURITY.md

主权签名

胡良锋（Liangfeng Hu）
YFCore Technology Limited
封板时间：2026-02-24
最终声明：V∞已锁定，永不破锁。

---

## 2) requirements.txt

文件名称：《requirements.txt》｜整个方案中文名称：《最小依赖（demo可运行）》

```txt
# Intentionally minimal: reference demo runs on Python standard library only.
# Keeping this file for future optional OpenAPI validation tooling.
