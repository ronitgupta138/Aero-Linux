# eBPF Telemetry Subsystem Specification

## 1. Overview
The Aero Linux eBPF Telemetry Subsystem provides low-overhead, in-kernel observability into block device I/O latencies, TCP network retransmissions, scheduler runqueue latency, and system call execution profiles.

## 2. In-Kernel Architecture
- **Hook Points:**
  - `tracepoint/block/block_rq_issue` and `tracepoint/block/block_rq_complete` for sub-millisecond block device I/O service tracking.
  - `tracepoint/tcp/tcp_retransmit_skb` for detecting network packet drop anomalies and congestion window collapses.
  - `tracepoint/sched/sched_stat_runtime` and `tracepoint/sched/sched_switch` for measuring task scheduling runqueue delays.
- **Data Buffering:**
  - Uses pinned eBPF BPF_MAP_TYPE_RINGBUF instances to minimize memory copying overhead between kernel space and user space collectors.
  - Asynchronous event polling using `bpf_ring_buffer__poll` with adaptive backoff to ensure zero CPU throttling on interactive workloads.

## 3. Overhead Guarantees
- Maximum CPU consumption overhead capped at `< 0.3%` of a single CPU core under sustained 100k IOPS load.
- Strict verifier-guaranteed execution bounds on all probe handlers: zero unbounded loops, zero blocking allocations.
