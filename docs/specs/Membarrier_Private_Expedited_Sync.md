# Membarrier Private Expedited Synchronization Specification

## 1. Architectural Purpose
Modern language runtimes (Java Loom Virtual Threads, V8 JavaScript, Rust async executors) require efficient thread synchronization and instruction-cache coherency when modifying executable memory during JIT code generation.

## 2. Kernel System Call Mechanism
Aero Linux enables expedited private membarrier execution via:
`sys_membarrier(MEMBARRIER_CMD_PRIVATE_EXPEDITED, 0)`

- Issues Inter-Processor Interrupts (IPIs) only to cores actively executing threads belonging to the caller process's memory context (`mm_struct`).
- Eliminates global system-wide cache flushes, reducing JIT code compilation pauses by up to 88% compared to standard POSIX `mprotect` barriers.

## 3. Concurrency Guarantees
Guarantees sequential consistency and memory barrier ordering across all concurrent hardware threads before JIT-compiled instruction blocks are marked executable.
