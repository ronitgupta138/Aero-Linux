# KVM Dynamic Memory Ballooning & Page Hinting Specification

## 1. MicroVM Ephemeral Isolation Memory Management
Aero Linux provides lightweight ephemeral MicroVMs via KVM and QEMU. Dynamic memory ballooning ensures host RAM is reclaimed immediately when guest memory allocations subside.

## 2. Virtio-Balloon Architecture
- **Balloon Driver:** Guest OS virtio-balloon driver allocates pinned pages and transfers descriptor references to the hypervisor host.
- **Host RSS Deallocation:** The host kernel invokes `madvise(MADV_DONTNEED)` on deallocated guest page frames, reducing the MicroVM process resident set size (RSS).

## 3. Page Freeing Hints
Enabling `virtio-balloon` page reporting (`free-page-reporting=on`) provides sub-second return of unused guest memory pools directly back to the Aero Linux zRAM / host allocator.
