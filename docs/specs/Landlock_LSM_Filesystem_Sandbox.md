# Landlock LSM Unprivileged Filesystem Sandboxing Specification

## 1. Overview
Landlock is an unprivileged Linux Security Module (LSM) that allows Aero Linux background daemons and GUI apps to restrict their own file system access without root privileges or complex SELinux profiles.

## 2. Rule Set Creation & Access Rights
```c
struct landlock_ruleset_attr ruleset_attr = {
    .handled_access_fs = LANDLOCK_ACCESS_FS_READ_FILE |
                         LANDLOCK_ACCESS_FS_WRITE_FILE |
                         LANDLOCK_ACCESS_FS_READ_DIR |
                         LANDLOCK_ACCESS_FS_MAKE_REG,
};
```

## 3. Sandboxing Invariants
1. **Volatile Directory Isolation:** Background daemons receive read-write access strictly to `~/.config/aero` and `/home/ronit138/.hermes/cache/scratch`.
2. **Immutable System Roots:** Read-only enforcement over `/usr`, `/lib`, and `/etc`.
3. **No-New-Privs:** Processes apply `prctl(PR_SET_NO_NEW_PRIVS, 1)` prior to activating the Landlock ruleset, permanently preventing privilege escalation attacks.
