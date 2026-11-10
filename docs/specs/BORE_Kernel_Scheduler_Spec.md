# BORE (Burst-Oriented Response Enhancer) Scheduler Integration Specification

## 1. Overview
Aero Linux integrates the BORE scheduler modification on the standard CFS/EEVDF Linux kernel scheduler. BORE dynamically tracks the burstiness of tasks and optimizes interactive desktop responsiveness without sacrificing throughput for batch compute workloads.

## 2. Mathematical Formulation & Scoring
- **Burst Scale Metric:**
  $$\text{Burst Score} = \max\left(0, \log_2\left(\frac{\text{burst_runtime}}{\text{average_runtime}}\right)\right)$$
- Tasks exhibiting high burst ratios (e.g. video rendering, compilation swarms) receive proportional dynamic yield penalties.
- Interactive tasks (e.g. GUI compositor, editor input handling, audio subsystems) maintain low burstiness scores and gain scheduling priority during frame rendering deadlines.

## 3. Kernel Sysctl Configuration
- `/proc/sys/kernel/sched_bore`: Enabled (1) by default.
- Tuning parameters for desktop response latency vs server throughput benchmarks.
