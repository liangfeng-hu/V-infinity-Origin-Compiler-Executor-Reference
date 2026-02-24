# Integration Guide｜V∞ Constitutional AIOS Bus 接入指南（V∞.1）

**《本源编译执行器通用宪法（13母律）× GateVectorLen=91 × LSE元公理》**  
**AIOS底层总线集成指南（不加门，只加证据字段）**

（目标）  
将 V∞ 总线作为 Pre-Commit / Sidecar / Agent Runtime 的**物理根信任针眼**，实现“任何世界写回必须锚定物理因果”。  
原则：不新增门；只加证据字段；Fail-Closed 永不弱化；CommitUnique 唯一针眼；所有结果可审计可复算。

---

## 1. 推荐部署形态（3种零侵入模式）

### 1.1 Pre-Commit Sidecar（最推荐）
推理服务 → **V∞ Sidecar（LSE×Gate90×Gate91）** → Verdict → Output Router  
- 只传证据字段：`intent_audit_group` + `seed_continuity` + `physical_proof`
- 默认不传 raw prompt / raw completion（母律9：最小泄漏律）
- Sidecar 永远输出：`payload` + `AuditCard_t`

适用：已有推理服务、想最快获得 Fail-Closed 与全息审计闭包。

### 1.2 Agent Runtime 内置针眼（控制世界写回的标准做法）
任何 Agent 的外部 API 调用（转账/控制服务器/下发工单/采购）前，必须先调用 V∞ Bus：
- 通过：CommitUnique=1 才允许执行动作（ΔΩ_t≠0）
- 失败：进入 SafeHold（只记录 Evidence，不执行动作）

适用：Agent 存在真实世界写回风险，需要“物理级停机阀”。

### 1.3 API Gateway Filter（最低摩擦入口）
在 Nginx/Envoy/Traefik 前增加 V∞ Filter 微服务：
- 高价值路由必须 I_FLOW=0 才放行
- 失败即 Fail-Closed，可返回 ShadowOnly 或直接拒绝

适用：大厂安全团队两分钟验证语义；快速 PoC 与分层上线。

---

## 2. 数据最小化原则（母律9：最小泄漏律）
- 仅提交 hashes / canonicalized telemetry / `intent_audit_group`
- 默认不提交 raw prompt / raw completion
- 所有证据写入：`Ledger_t` + `AuditCard_t`
- 审计数据分级访问（业务不可见的字段必须可封存但可复算）

---

## 3. 集成检查清单（生产前必验）
- [ ] GateVectorLen == 91（硬校验）
- [ ] Fail-Closed 永不弱化（任一失败 → ΔΩ_t=0）
- [ ] CommitUnique 为唯一针眼（任何世界写回必须经由它）
- [ ] AuditCard_t 100% 可回放复算判决
- [ ] LSE 三层（Intent/Temporal/Physical）同时 Complete 才允许放行
- [ ] ShadowOnly 输出策略仅用于 Fail-Closed（可选反制，不影响主闭环）
- [ ] 旁路路径定义为违宪并 Fail-Closed（母律6：不可旁路律）

---

## 4. 最小接入字段（不破锁最小闭包）

### 4.1 Gate90：intent_audit_group（允许扩展字段）
必须存在：
- `distillation_risk_score`（或一般化 `intent_risk_score`）
- `extraction_pattern_flags`（可扩展：`cross_model_probe` / `federated_aggregation`）
- `base_tau`（阈值基础值）

建议扩展（仍属于证据字段）：
- `device_chain_hash`（跨设备连续性）
- `tenant_id` / `model_fingerprint`（多租户隔离证据）
- `zk_low_intent_proof`（低意图证明占位）

### 4.2 SeedContinuity（时间与设备连续性证据）
- `seed_continuity_ok`（PoC 可 mock；生产需安全时钟/nonce/设备链）
- （可选）`pi_seed_t` / `session_binding` / `device_chain_hash`

### 4.3 Gate91：physical_proof（物理做功证据，占位接口允许 mock）
- `thermo_proof_ok`
- `attestation_ok`
- `entropy_clone_risk_code`

### 4.4 AuditCard_t（必须生成）
必须包含：
- `i_90`、`i_91`、`lse_budget_ok`、`i_flow`
- `commit_unique`、`world_writeback`
- `out_level`、`reason_code`
- `evidence_keys`（至少：req_hash / gate90_hash / gate91_hash / ledger_head_hash）

---

## 5. Fail-Closed 输出策略（OutLevel）
OutLevel 仅是 Fail-Closed 时的输出分级，不是新门：
- `Normal`：仅在通过时使用
- `ShadowOnly`：失败时返回低风险输出或 decoy，并写入审计指纹
- `SafeHold`：涉及世界写回的场景必须使用：只写 Evidence，不执行动作

建议：
- 纯文本生成失败：可使用 ShadowOnly
- 动作执行失败：必须 SafeHold

---

## 6. 六条杀手锏如何落到接口（只加字段版）
1) 自适应阈值：写入 `intent_audit_group.tau_effective`（由历史风险计算），审计卡记录。  
2) ShadowOnly 毒饵：失败时生成 `decoy_payload` + `poison_tag`，写入 AuditCard_t。  
3) 跨设备连续：`device_chain_hash` 与 SeedContinuity 绑定。  
4) 多租户隔离：`cross_model_probe` + `tenant_id` + `model_fingerprint` 作为证据字段。  
5) 审计导出：AuditCard_t schema 固化 + evidence_keys 可复算。  
6) 低意图证明：`zk_low_intent_proof` 占位字段 + `zk_verify_result` 写入审计卡。

注意：以上全部属于证据字段扩展，不新增门。GateVectorLen 仍然=91。

---

## 7. 生产部署注意事项（参考实现边界）
- 本仓库 demo 仅为 mock 参考，用于语义与接口演示
- 生产时替换 Gate90/Gate91 的 mock 判决为真实 ZKP/TEE/安全时钟与防重放机制
- 所有扩展仅允许进入 intent_audit_group 或 AuditCard_t

详见 CONSTITUTION.md 中 Gate90 “允许的扩展范围”。

---

（封板签名）  
胡良锋（Liangfeng Hu）｜YFCore Technology Limited
