# Wayland Compositor Direct Scanout & Latency Bounds

## 1. Zero-Copy Direct Scanout
When a fullscreen application or terminal editor occupies the complete output viewport, the compositor bypasses composition buffers and programs the application DRM framebuffer directly into the hardware display plane.

## 2. Input Latency Budget
- Hardware interrupt to libinput event dispatch: $< 1.2\text{ms}$.
- Wayland protocol message dispatch to client surface: $< 0.8\text{ms}$.
- Total end-to-end input latency: $< 8.0\text{ms}$ at 144Hz refresh rates.
