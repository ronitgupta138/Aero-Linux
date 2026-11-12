# NVMe Autonomous Power State Transitions (APST) Specification

## 1. Overview
Aero Linux configures NVMe Autonomous Power State Transitions (APST) to minimize idle power draw while enforcing deterministic low-latency wake characteristics on NVMe storage controllers.

## 2. Power State Latency Matrix
NVMe SSD controllers define operational (PS0, PS1) and non-operational (PS3, PS4) states:
- **PS0 (Operational):** Maximum read/write bandwidth, zero entry/exit latency.
- **PS3 (Light Non-Operational):** Idle latency budget $\le 25\,\text{ms}$. Controller clocks gated, PCIe link in L1.2.
- **PS4 (Deep Non-Operational):** Idle latency budget $\le 100\,\text{ms}$. High energy savings, deep PHY power gating.

## 3. Latency Budget Configuration
Kernel command-line APST latency ceiling is clamped at:
`nvme_core.default_ps_max_latency_us=25000`

This guarantees that drives transition to deep energy-saving states during desktop idle without causing audio dropouts or compositor stutter upon sudden disk I/O requests.
