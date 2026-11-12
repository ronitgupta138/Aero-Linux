# BPF LSM Security Instrumentation & Zero-Overhead Policy Specification

## 1. Subsystem Architecture
Aero Linux leverages BPF-based Linux Security Modules (BPF LSM) to enforce declarative security policies at native kernel speeds, replacing slow `ptrace`-based sandboxes.

## 2. Instrumented Kernel Hooks
Key LSM security entry points instrumented:
- `lsm/file_open`: Validates file descriptors against permissible workspace boundaries.
- `lsm/bprm_check_security`: Enforces executable binary signing and disallows unauthorized interpreter spawns.
- `lsm/socket_connect`: Restricts network access from sandboxed developer utility scripts.

## 3. Performance Characteristics
BPF LSM JIT-compiled bytecode executes directly within kernel context with near-zero overhead (< 15 nanoseconds per hook evaluation), enabling continuous runtime observability.
