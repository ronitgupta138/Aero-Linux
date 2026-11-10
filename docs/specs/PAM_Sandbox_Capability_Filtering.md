# PAM Security Sandbox & Linux Capability Filtering Specification

## 1. Architectural Scope
Ensures development servers and unprivileged background services cannot escalate privilege or acquire administrative capabilities.

## 2. Security Primitives
- **No-New-Privileges:** Enforces `prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)` upon session initialization, preventing `setuid` binaries from elevating credentials.
- **Bounding Set Dropping:** Clears ambient and bounding capability sets (`CAP_SYS_ADMIN`, `CAP_NET_ADMIN`, `CAP_SYS_RAWIO`) for interactive developer sandboxes.
