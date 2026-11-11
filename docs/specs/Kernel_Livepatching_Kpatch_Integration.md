# Kernel Livepatching (Kpatch) Integration Specification

## 1. Overview
Aero Linux incorporates dynamic kernel livepatching via `kpatch` and the in-tree Linux kernel livepatch framework (`CONFIG_LIVEPATCH`). This allows critical CVE security patches and scheduler hotfixes to be applied to running production kernels with zero process interruption or reboot requirements.

## 2. In-Kernel Function Redirection
- Utilizes `ftrace` with `FTRACE_OPS_FL_IPMODIFY` to redirect entry instructions of patched kernel functions to the replacement payload.
- Enforces RCU (Read-Copy-Update) synchronization barriers to guarantee all CPU execution contexts have exited active target functions before patch commits.
