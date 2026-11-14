"""
PipeWire Pro-Audio Quantum Buffer Manager.
Validates buffer sizes and calculates audio roundtrip latencies.
"""

VALID_QUANTUMS = [32, 64, 128, 256, 512, 1024]

def is_valid_quantum(quantum: int) -> bool:
    """Check if buffer quantum size is a standard power-of-two pro-audio value."""
    return quantum in VALID_QUANTUMS

def calculate_roundtrip_latency_ms(quantum: int, sample_rate: int = 48000) -> float:
    """Calculate one-way buffer latency in milliseconds."""
    if not is_valid_quantum(quantum):
        raise ValueError(f"Invalid quantum: {quantum}. Must be one of {VALID_QUANTUMS}")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive.")
    return round((quantum / sample_rate) * 1000.0, 3)

def generate_wireplumber_config(quantum: int = 64, sample_rate: int = 48000) -> dict:
    """Generate WirePlumber configuration dictionary for pro-audio profile."""
    if not is_valid_quantum(quantum):
        raise ValueError(f"Invalid quantum: {quantum}")
    return {
        "context.properties": {
            "default.clock.rate": sample_rate,
            "default.clock.quantum": quantum,
            "default.clock.min-quantum": 32,
            "default.clock.max-quantum": 1024,
        },
        "latency_ms": calculate_roundtrip_latency_ms(quantum, sample_rate)
    }
