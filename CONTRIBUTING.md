# CONTRIBUTING｜贡献指南（V∞ Reference Implementation）

**V∞-Origin-Compiler-Executor-Reference**  
**本源编译执行器通用宪法（13母律）× GateVectorLen=91 × LSE元公理**

（封板声明）  
本仓库为宪法参考实现，核心使命是展示 **Fail-Closed 语义、证据闭包与接口形状**。  
任何贡献必须严格守锁：**不新增门、不弱化硬墙、不旁路针眼，只允许在证据字段内扩展**。

---

## 1. 贡献前请先读（必读文档）
- `CONSTITUTION.md`（宪法正本与冻结条件）
- `SECURITY.md`（边界与负责任披露）
- `docs/integration-guide.md`（集成模式与最小闭包）

---

## 2. 贡献范围（Allowed Contributions）

允许的贡献类型（欢迎）：

1) 文档改进（Docs)
- 修正拼写、结构优化、术语一致性
- 增加清晰的集成说明、审计字段解释、示例用法
- 增补威胁模型说明（不包含攻击脚本与可执行细节）

2) 接口规范完善（OpenAPI / Spec）
- 对 `spec/*.openapi.json` 做字段说明完善
- 增加 schema 版本号字段、example 字段、注释说明
- 保持语义：仍然是 Gate90/Gate91/LSE 的证据闭包接口形状

3) 参考实现增强（Reference Implementation）
仅允许在以下范围内增强：
- 增加 **证据字段**（Evidence fields）  
  - 只能进入：`Gate90.intent_audit_group` 或 `AuditCard_t`
- 增加更多演示场景（demo.py）  
  - 只能展示 Fail-Closed、ShadowOnly、SafeHold、AuditCard 可复算等语义
- 改善可读性与可维护性（重构、注释、类型标注）  
  - 必须不改变冻结条件与判决语义

---

## 3. 绝对禁止（Constitutional Red Lines）

任何 PR 若触碰以下任意一条，将被直接关闭：

1) **新增任何 Gate**（GateVectorLen 必须永远=91）  
2) **削弱 Fail-Closed 语义**（失败仍允许 ΔΩ_t≠0 或 CommitUnique=1）  
3) **旁路 CommitUnique 针眼**（任何世界写回不经针眼）  
4) 引入生产级攻击/绕过实现细节（例如可直接复用的攻击脚本、可执行绕过策略）  
5) 请求/引入生产级 ZKP 电路、真实 attestation 链、真实 π_seed 发生器  
6) 让系统“更容易蒸馏”或“移除物理证明”  
7) 让历史补丁成为因果父系（违背母律1与母律8：本源重编译与因果闭包）

---

## 4. 代码贡献规则（必须满足）

1) 不新增依赖（默认仅 Python 标准库）  
2) demo.py 仍需在 iPhone 复制后可直接运行  
3) 任何新增字段必须：
- 明确放入 `intent_audit_group` 或 `AuditCard_t`
- 在输出的 `AuditCard_t` 中可见
- 可被 `evidence_keys` 哈希覆盖（可复算）

4) 不允许修改“冻结条件”的声明文本（除非修正明显笔误且不改变含义）

---

## 5. PR 提交清单（提交前自检）

- [ ] GateVectorLen 仍然=91（无新增门）  
- [ ] Fail-Closed 未被削弱（失败时 CommitUnique=0 且 ΔΩ=0）  
- [ ] CommitUnique 仍为唯一针眼  
- [ ] 新增内容只进入 intent_audit_group 或 AuditCard_t  
- [ ] demo.py 运行通过（本地或 GitHub Actions）  
- [ ] 文档更新同步（如新增字段，请更新 docs 对应说明）  
- [ ] 不包含可执行攻击脚本或绕过细节  

---

## 6. 风格与提交规范

- Commit message 建议使用：
  - `docs: ...`
  - `spec: ...`
  - `demo: ...`
  - `refactor: ...`
- 不要引入花哨依赖或复杂工程脚手架（保持“低摩擦可验证”）

---

## 7. 联系方式
如需私密披露安全问题，请按 `SECURITY.md` 的流程联系：security@yfcore.tech

（封板签名）  
胡良锋（Liangfeng Hu）｜YFCore Technology Limited
