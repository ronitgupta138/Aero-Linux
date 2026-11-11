# Direct Rendering Infrastructure (DRI3) & Hardware Acceleration Pipeline

## 1. Buffer Sharing Mechanics
- Uses DMA-BUF file descriptors for zero-copy GPU buffer sharing across Wayland clients and display servers.
- Synchronizes buffer release events via Linux sync file fences (`drm_syncobj`).

## 2. VBlank Presentation Timing
- Adheres strictly to Vulkan/OpenGL VBlank swap intervals, eliminating tearing while minimizing presentation queue lag to $< 2.5\text{ms}$.
