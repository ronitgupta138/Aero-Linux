# sched_ext Custom Extensible BPF CPU Scheduling Specification

## 1. Overview
`sched_ext` is an extensible Linux kernel CPU scheduling framework enabled in recent kernels (v6.12+) that allows scheduling policies to be defined via eBPF programs loaded dynamically from userspace.

## 2. Dispatch Queues & Core Allocation
- **User-Space Policy:** Aero Linux BPF scheduling dispatchers categorize tasks into interactive (compositor, editor) and background batch workers (compilers, linters).
- **Core Affinity:** Background compilations are pinned to efficient compute units, while interactive UI events are scheduled immediately on high-frequency boost cores.

## 3. Safe Failure Fallback
If an eBPF scheduling program aborts or encounters a kernel safety panic, the kernel seamlessly and immediately fails over back to the default CFS / EEVDF scheduler without dropping running tasks.
