# PipeWire Low-Latency Pro-Audio Quantum Specification

## 1. Real-Time Audio Graph Scheduling
Aero Linux configures PipeWire and WirePlumber to deliver deterministic, glitch-free audio processing with sub-2ms buffer latency for professional music production, DAWs, and system notification chimes.

## 2. Quantum Buffer Rules
The PipeWire audio server dynamically manages buffer quantum allocation:
- **Default Pro-Audio Buffer:** `64` samples at `48000 Hz` (1.33 ms round-trip).
- **Fallback Buffer:** `128` samples at `48000 Hz` (2.66 ms round-trip).
- **Allowed Dynamic Range:** `32` to `1024` samples.

## 3. RTKit Priority Invariants
- Audio processing threads acquire `SCHED_RR` or `SCHED_FIFO` real-time scheduling priority via RealtimeKit (`rtkit-daemon`).
- Real-time priority ceiling: `20`.
- Memory locking (`mlockall`) enforced on the audio graph context to eliminate page-fault latency spikes during high-concurrency desktop workloads.
