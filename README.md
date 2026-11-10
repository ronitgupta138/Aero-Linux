<div align="center">

```text
 █████╗ ███████╗██████╗  ██████╗     ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
███████║█████╗  ██████╔╝██║   ██║    ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ 
██╔══██║██╔══╝  ██╔══██╗██║   ██║    ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ 
██║  ██║███████╗██║  ██║╚██████╔╝    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
```

### **The Ultra-Lean AI & High-Performance Developer Operating System**

[![GitHub Stars](https://img.shields.io/github/stars/ronitgupta138/Aero-Linux?style=flat-square&logo=github&color=0891b2)](https://github.com/ronitgupta138/Aero-Linux/stargazers)
[![Web Portal](https://img.shields.io/badge/Web_Portal-Live_Portal-0891b2.svg?style=flat-square)](https://ronitgupta138.github.io/aero-linux/)
[![Release](https://img.shields.io/badge/Release-v1.5.0--Pulsar-0284c7.svg?style=flat-square)](https://github.com/ronitgupta138/aero-linux/releases)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub_Sponsors-ea4aaa.svg?style=flat-square&logo=githubsponsors)](https://github.com/sponsors/ronitgupta138)
[![AlternativeTo](https://img.shields.io/badge/AlternativeTo-Listed-2563eb.svg?style=flat-square&logo=linux)](https://alternativeto.net/software/aero-linux/about/?utm_source=badge&utm_medium=referral)
[![CI](https://github.com/aero-linux/aero-linux/actions/workflows/ci.yml/badge.svg)](https://github.com/aero-linux/aero-linux/actions/workflows/ci.yml)
[![CI / Test Suite](https://img.shields.io/badge/Test_Suite-138%20Passed-059669.svg?style=flat-square)](https://github.com/aero-linux/aero-linux)
[![Idle Memory](https://img.shields.io/badge/Idle_RAM-312MB-059669.svg?style=flat-square)]()
[![zRAM](https://img.shields.io/badge/zRAM_ZSTD-Default_Enabled-7c3aed.svg?style=flat-square)]()
[![Works with GitHub](https://img.shields.io/badge/Works_with-GitHub-238636.svg?style=flat-square&logo=github)](https://github.com/developer-program)
[![License: MIT](https://img.shields.io/badge/License-MIT-4f46e5.svg?style=flat-square)](LICENSE)
[![Architecture](https://img.shields.io/badge/Architecture-x86__64-d97706.svg?style=flat-square)]()

<p align="center" style="margin-top: 12px; margin-bottom: 12px;">
  <a href="https://alternativeto.net/software/aero-linux/about/?utm_source=badge&utm_medium=referral" target="_blank">
    <img src="https://alternativeto.net/static/badges/badge-wide-dark.svg" alt="Aero Linux | AlternativeTo" width="300" height="56" style="max-width: 100%; height: auto;" />
  </a>
</p>

*Engineered for systems programmers, backend engineers, and local AI builders. Sub-350MB idle footprint, dynamic in-memory zRAM ZSTD compression, 1-click local LLM inference, 59 native GTK3 applications, and zero background bloat.*

</div>

---

## 📥 1-Command Instant Download & Install

Install the global `aero` CLI and GTK3 Control Center directly into your Linux environment:

```bash
curl -fsSL https://raw.githubusercontent.com/ronitgupta138/aero-linux/main/install.sh | bash
```

*Or install from local clone:*
```bash
git clone https://github.com/ronitgupta138/aero-linux.git
cd aero-linux && ./install.sh
```

---

## 📊 Real Hardware Performance Benchmark

Tested on identical physical hardware (**AMD Ryzen 5 5600H, 12 Cores, 15GB RAM, NVMe SSD**):

| Operating System | Idle RAM Usage | Local LLM Free RAM (16GB RAM) | Disk Swap Latency | Battery Health Cap |
| :--- | :---: | :---: | :---: | :---: |
| **Windows 11** | ~3,850 MB | ~11.5 GB | High (SSD Swapping) | ❌ Third-party app |
| **Ubuntu 24.04 (GNOME)** | ~1,420 MB | ~14.0 GB | High (SSD Swapping) | ❌ Manual script |
| **⚡ Aero Linux (1.5-Pulsar)** | **312 MB** | **~15.1 GB** | **Nanoseconds (zRAM ZSTD)** | **✅ Built-in (`aero power`)** |

---

## 🚀 Core Architectural Pillars

### 1. 🪟 Dual Desktop Experience (Windows Migrants + Tiling Purists)
* **Windows-Friendly Mode (`aero layout windows`):** Familiar bottom taskbar with **⚡ Start Menu**, pinned quick-launch apps, floating windows, and standard shortcuts (`Win+E` for File Explorer, `Ctrl+Shift+Esc` for Task Manager, `Alt+Tab` for window cycling, `Win+L` for screen lock).
* **Hacker Tiling Mode (`aero layout tiling`):** Cyber Dark Sway auto-tiling with customizable gaps and floating translucent Waybar status pills.

### 2. 🧠 Zero-Disk-Swap Memory Engine (zRAM ZSTD)
Eliminates SSD swap thrashing. Memory pages are compressed dynamically in-RAM using multi-threaded **ZSTD** (~2.8:1 compression ratio), effectively expanding 16GB of physical RAM to ~25GB+ of usable workspace headroom.

### 3. 🤖 Native Local AI Stack (`aero ai`)
1-click local model serving with Ollama and Docker. Running `aero ai run deepseek-r1:8b` serves local reasoning models instantly with automated NVIDIA CUDA and AMD ROCm kernel configuration (`aero gpu setup`).

### 4. 🔋 Hardware Battery Preservation & Power P-States
Direct ACPI hardware charge threshold control (`aero power --threshold 80`) to protect lithium health during desk sessions, paired with adaptive fan profiles (`battery`, `balanced`, `boost`, `gaming`).

---

## 🛠️ The Aero Command Suite (`aero-cli`)

Aero Linux includes an integrated management CLI covering the entire developer lifecycle:

```bash
# 🖥️ Diagnostics & Hardware Sensors
aero doctor                     # Full hardware, kernel, memory, and AI stack audit
aero temp                       # Live CPU, GPU, and NVMe hardware temperatures
aero battery                    # Lithium health, design vs usable Wh, and charge cycles
aero benchmark                  # Multi-core CPU, RAM bandwidth, and NVMe write speed test
aero monitor                    # Live interactive terminal dashboard with per-core clocks
aero logs error                 # Intelligent journalctl system error & panic parser

# ⚡ Power & Performance
aero power [battery|balanced|boost|gaming]  # Switch CPU frequency governor
aero power --threshold 80       # Cap hardware battery charge at 80%
aero gamemode run <executable>  # Low-latency Wine/Proton game launcher

# 🧠 Memory & Storage Management
aero memory --optimize          # Compact zRAM pages and drop filesystem caches
aero pkg clean                  # Prune orphaned packages and clean APT/Flatpak caches
aero disk top                   # Find large files (>100MB) consuming storage
aero disk clean-node-modules    # Recursively remove nested node_modules

# 🤖 Local AI & Deep Learning
aero ai init                    # 1-click Ollama daemon installation
aero ai pull deepseek-r1:8b     # Download local LLM model weights
aero ai run deepseek-r1:8b      # Launch interactive local AI prompt
aero ai calc --params 8 --quant q4_k_m # Calculate weights, KV cache, and RAM fit
aero ai bench deepseek-r1:8b    # Measure TTFT and tokens/sec throughput
aero agent "explain epoll"      # Local AI coding & terminal assistant
aero agent -s "kill port 8080"  # Generate exact shell commands
aero gpu setup                  # Auto-configure CUDA / ROCm GPU drivers

# 🛠️ Developer Sandboxes & Local Databases
aero store [list|install <app>] # 1-Click App Center (VS Code, Brave, Docker, Postman)
aero dev run [node|python|rust|go|c]  # Isolated containerized workspaces
aero db start [postgres|redis|mysql|mongo|clickhouse]  # 1-command local DBs
aero db ui [postgres|redis|sqlite] # Browser-based database management studio
aero tunnel <port>              # Instant public HTTPS tunnel (Cloudflare / SSH)
aero turbo [mount|status]       # 10GB/s tmpfs RAM-disk compilation accelerator
aero json [format|minify|get]   # Zero-dependency JSON formatter & path query engine
aero uuid / aero token          # Cryptographic UUIDv4 & random token generator
aero hash [sha256|md5] <target> # Cryptographic file/string hash calculator
aero base64 [enc|dec] <str>     # Base64 encoder/decoder
aero jwt <token>                # Local JWT payload & expiration claims inspector
aero http <url>                 # High-speed HTTP client with latency breakdown
aero dig <domain> / aero ping <host> # DNS records & TCP latency profiler
aero color <hex>                # Terminal HEX/RGB color inspector & ANSI swatch
aero time "<command>"           # High-precision sub-millisecond execution stopwatch
aero fan [status|set <profile>] # Hardware cooling curve manager (silent/turbo)
aero regex <pattern> <text>     # Terminal regex debugger and capture group parser
aero diff <file1> <file2>       # Colorized terminal side-by-side diff inspector
aero qr [encode|wifi]           # Instant terminal QR codes for mobile sync & Wi-Fi
aero snippet [list|search <q>]  # Developer one-liner cheatsheet & vault
aero mock serve --port 4000     # Instant local mock REST API & JSON server
aero cert generate [domain]     # 1-command trusted local SSL/TLS generator
aero clean [--dry-run]          # Deep system cache de-bloater (npm/pip/apt/docker)
aero dotfiles [export|import]   # Backup & sync developer shell & desktop configs
aero flash [drives|write]       # Safe USB live ISO media flasher
aero trace ping github.com      # Socket connect, TLS handshake & DNS tracer
aero health                     # Hardware S.M.A.R.T. NVMe & CPU throttle audit
aero firewall status            # Developer UFW firewall & port manager
aero prompt bash                # Ultra-fast sub-millisecond shell prompt engine
aero sandbox run --offline ./script.sh # Micro-jail Linux namespace sandbox
aero vault [set|get|list|export] # Encrypted local secret & .env keyring
aero live --port 8080           # Real-time web telemetry streaming dashboard
aero notify <title> [msg]       # Desktop toast notification & sound alert
aero perf [cpu|io]              # Low-level CPU context-switch & NVMe profiler
aero port list                  # Active listening developer port inspector
aero port kill 3000             # Terminate process listening on specific port
aero env check                  # Audit installed SDKs (Node, Python, C, Rust, Go, Java)
aero api bench http://localhost:3000  # Concurrent HTTP load tester (req/sec, p99)

# 🎨 Desktop, Git & Networking
aero layout [windows|tiling]    # 1-click layout switcher
aero kernel [audit|profile]     # Low-latency vs throughput kernel scheduler
aero wallpaper [set|generate]   # Procedural vector cyber wallpapers
aero git [status|scan|clean|graph|churn] # Workspace status, multi-repo scanner & branch graph
aero theme auto                 # Auto-sync theme with day/night solar cycle & battery
aero theme set [cyber-cyan|tokyo-night|nord|gruvbox] # Desktop palette switcher
aero font install jetbrains-mono # 1-click Nerd Font installation
aero net bbr                    # Enable Google BBR TCP congestion control
aero net dns cloudflare         # Switch to encrypted DNS-over-TLS (1.1.1.1)
aero security [audit|harden]    # UFW firewall & kernel security hardening
aero snapshot create            # Zero-latency system restore point
aero share .                    # Instant local network HTTP file sharing server
aero ssh [status|gen|copy|test] # Ed25519 SSH key management
```

---

## 🎛️ Complete Zero-Terminal Graphical Application Suite

Aero Linux includes **59 dedicated native GTK3 graphical management tools**, ensuring developers and users never need a terminal for common workflows:

| Application | Command / Shortcut | Description |
| :--- | :--- | :--- |
| **Aero Spotlight** | `Alt + Space` / `aero-spotlight` | Floating Raycast-style command palette, inline math evaluator & app launcher |
| **Aero Control Center** | `aero-welcome` | 6-tab central hardware, developer suite, maintenance, power, theme, and store hub |
| **Aero Local AI Studio**| `aero-ai-gui` | Offline Ollama LLM model manager, VRAM estimator & local AI prompt playground |
| **Aero Markdown Studio**| `aero-markdown-gui` | Real-time split Markdown editor, live structure parser & 1-click HTML exporter |
| **Aero HTTPS Tunnel** | `aero-tunnel-gui` | Expose localhost dev servers to instant public HTTPS URLs |
| **Aero Code Sandbox** | `aero-sandbox-gui` | Live multi-language code scratchpad (Python, Node, Bash, C) with microsecond profiler |
| **Aero GPU Studio** | `aero-gpu-gui` | GPU load, VRAM allocation, temperature sensors & 1-click hybrid graphics switcher |
| **Aero Git Graph** | `aero-gitgraph-gui` | Visual commit graph tree, stage/unstage file selector & conventional commit generator |
| **Aero Archive Studio** | `aero-archive-gui` | Inspect archive trees without extracting; create ZIP, TAR.GZ & TAR.XZ packages |
| **Aero QR Code Studio** | `aero-qr-gui` | Vector QR code generator for URLs, staging servers & 1-tap phone Wi-Fi pairing |
| **Aero Screen Recorder**| `aero-recorder-gui` | Instant MP4/GIF desktop capture, PipeWire audio toggle & recordings gallery |
| **Aero Visual Diff** | `aero-diff-gui` | Side-by-side code diffing, additions/deletions visualizer & patch generator |
| **Aero Benchmarks** | `aero-benchmark-gui` | Multi-core CPU compute, RAM memory bandwidth & NVMe disk I/O benchmark suite |
| **Aero Package Studio** | `aero-deps-gui` | System package inspector, shared library analyzer (`ldd`) & orphan cleaner |
| **Aero Mock Server** | `aero-mock-gui` | Local mock REST API server, response simulator & live webhook inspector |
| **Aero Crypto & JWT** | `aero-crypto-gui` | Visual JWT token decoder, cryptographic hash calculator (SHA256/512) & UUID generator |
| **Aero Cron Scheduler** | `aero-cron-gui` | Visual scheduled tasks manager, human-readable cron builder & test runner |
| **Aero SQL & Database** | `aero-db-gui` | SQLite database explorer, table viewer & interactive SQL console |
| **Aero Regex Studio** | `aero-regex-gui` | Regular expression pattern evaluator, live capture group matcher & preset library |
| **Aero Project .env** | `aero-env-gui` | Environment variables studio, masked secrets editor & `.env.example` sync |
| **Aero Native API** | `aero-api-gui` | High-speed REST/HTTP client (GET/POST/PUT/DELETE) with JSON body editor |
| **Aero Docker Studio** | `aero-docker-gui` | Docker container cards, live resource telemetry, streaming logs & 1-click prune |
| **Aero Snapshots** | `aero-snapshots-gui` | 1-Click TimeMachine system restore points creator & instant config rollback |
| **Aero Workspaces** | `aero-workspaces-gui` | Multi-monitor virtual workspace switcher, window organizer & tagger |
| **Aero SSL & Dev Certs**| `aero-ssl-gui` | Local HTTPS SSL/TLS cert generator with Node.js, FastAPI & Nginx snippets |
| **Aero SSH & Servers** | `aero-ssh-gui` | Ed25519 keypair generator, `~/.ssh/config` bookmarks & 1-click connect |
| **Aero Firewall Shield**| `aero-firewall-gui` | UFW network firewall controller, 1-click port allow rules & security shield |
| **Aero Git Repos** | `aero-git-gui` | Multi-repository workspace status monitor, branch tracker & 1-click fetch/pull |
| **Aero Speed & Latency**| `aero-speed-gui` | High-precision latency profiler, DNS speed benchmark & CDN throughput tester |
| **Aero Disk Visualizer**| `aero-disk-gui` | Storage analyzer & 1-click `node_modules`, `target`, `.venv` bloat cleaner |
| **Aero Dotfiles Sync** | `aero-sync-gui` | 1-Click backup, export, and restore for developer dotfiles and configs |
| **Aero Startup Apps** | `aero-startup-gui` | Manage login autostart programs, add custom commands & optimize boot speeds |
| **Aero Service Manager**| `aero-services-gui` | Background systemd daemons (Docker, SSH, DBs) controller |
| **Aero Safe USB Flasher**| `aero-flasher-gui` | Safe live USB creator with automatic internal NVMe write protection |
| **Aero System Logs** | `aero-logs-gui` | Live systemd journald and dmesg hardware log viewer with 1-click export |
| **Aero Action Center** | `aero-quick-settings` | Frosted-glass quick tiles, sliders & system toggles |
| **Aero Task Manager** | `Ctrl + Shift + Esc` / `aero-monitor` | Live Cairo vector CPU waveform graph & memory gauges |
| **Aero Update Manager** | `aero-updater` | Asynchronous system & security patch installer |
| **Aero Wi-Fi Center** | `aero-wifi` | Spectrum scanner, signal strength monitor & 1-click connect |
| **Aero Bluetooth Center**| `aero-bluetooth` | Audio device & peripheral pairing and battery indicator |
| **Aero Audio Center** | `aero-audio` | 1-Click PipeWire audio sink switcher (Speakers, Headphones, BT, HDMI) |
| **Aero Displays** | `aero-displays` | Screen resolution, 240Hz refresh rate & HiDPI fractional scaling |
| **Aero Game Hub** | `aero-gamehub` | 1-Click GameMode, MangoHud FPS overlay & FSR upscaling launcher |
| **Aero Phone Link** | `aero-connect-gui` | Wireless phone link & drag-and-drop file drop target |
| **Aero Battery Studio** | `aero-power-gui` | 80% battery protection cap & acoustic cooling fan curves |
| **Aero Night Light** | `aero-nightlight-gui` | 3000K-6500K color temperature & eye-strain scheduler |
| **Aero Theme Studio** | `aero-theme-gui` | Accent glow color palette studio & procedural wallpaper generator |
| **Aero System Cleaner** | `aero-cleaner-gui` | 1-Click package cache, pip, npm & journal log de-bloater |
| **Aero Vault** | `aero-vault-gui` | Local encrypted developer secrets, API tokens & `.env` exporter |
| **Aero Snipping Tool** | `Win + Shift + S` / `aero-screenshot-gui` | Screen capture with instant crop and clipboard export |
| **Aero Font Studio** | `aero-font-gui` | Developer Nerd Font catalog and previewer |
| **Aero Port Inspector** | `aero-ports-gui` | Active listening dev ports, process viewer and kill tool |
| **Aero Self-Repair** | `aero-repair-gui` | 1-Click automated DNS, package, and service repair |
| **Aero About System** | `aero-about-gui` | Hardware specifications, kernel info, and Aero build badge |
| **Aero eBPF & Sockets**| `aero-ebpf-gui` | Kernel TraceFS diagnostics, real-time socket lifecycles & process monitor |

---

## 📖 In-Depth Documentation

* 📐 [**System Architecture Specification**](docs/ARCHITECTURE.md) — Kernel parameters, memory layout, and daemon specs.
* 🗺️ [**Strategic Engineering Roadmap**](docs/ROADMAP.md) — Future release progression (v1.5-Pulsar to v2.0-Singularity).
* 🛠️ [**Complete CLI Reference Manual**](docs/COMMANDS.md) — Detailed reference for all 25+ `aero` subcommands.
* 🪟 [**Windows Dual-Boot & Partition Safety Guide**](docs/DUAL_BOOT_GUIDE.md) — Safe dual-booting with Windows 10/11 and BitLocker.

---

## 🏗️ Building the Live ISO Locally

```bash
# Clone the repository
git clone https://github.com/ronitgupta138/aero-linux.git
cd aero-linux

# Run the automated live-build script (requires root)
sudo ./build/build.sh
```

---

## 🌐 Project Structure

```text
aero-linux/
├── build/                      # Live ISO builder, Debian packager, sysctl & completions
│   ├── build_iso.sh            # Automated Live bootable ISO generator
│   ├── package_deb.sh          # Debian (.deb) package compiler
│   └── completions/            # Fish, Bash, and Zsh shell completions
├── desktop/                    # Desktop configs, window manager & themes
│   ├── configs/                # Sway, Waybar, Nemo Actions, Fish, Alacritty
│   │   ├── nemo-actions/       # Zero-terminal right-click developer actions
│   │   └── waybar/             # Taskbar JSON & live telemetry scripts (ports, zRAM)
│   ├── icons/                  # High-contrast developer icon assets
│   └── themes/                 # Plymouth boot splash, Tokyo Night, Cyber Cyan
├── dist/                       # Release packages (.deb), checksums (SHA256SUMS)
├── docs/                       # Architecture, Commands, Roadmap & manpages
│   ├── ARCHITECTURE.md         # System design, memory hierarchy & kernel specs
│   ├── COMMANDS.md             # Complete CLI reference manual (25+ subcommands)
│   ├── DUAL_BOOT_GUIDE.md      # Windows 10/11 & EFI partition safety manual
│   ├── ROADMAP.md              # Engineering timeline & specs (v1.5 to v2.0)
│   └── man/                    # System manpage manuals (aero.1)
├── installer/                  # Calamares dual-boot safe installer configs & branding
├── packages/                   # Core Python & GTK3 developer applications
│   ├── aero-cli/               # 59 native GTK3 apps, CLI subcommands & 138 unit tests
│   └── aero-welcome/           # 6-tab GTK3 Control Center & Quick Setup GUI
└── web/                        # Web portal, 59-app catalog, zRAM calc & hotkey guide
```

---

## 👥 Contributors & Maintainers

* **[Ronit Gupta](https://github.com/ronitgupta138)** — *Lead Architect & Creator*
* **Open Source Community Contributors**

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for full project acknowledgments.

---

## 💖 Sponsoring & Infrastructure Support

Aero Linux is 100% free and open-source software (FOSS). Your sponsorship directly funds dedicated multi-arch CI runners, package mirror hosting, and bare-metal testing infrastructure:

* **☕ Supporter ($5/mo):** Sponsor badge on your GitHub profile and listed as a backer on the project README.
* **🚀 Active Backer ($10/mo):** Named credit in official Aero Linux release notes and priority issue triage.
* **⚡ Power Contributor ($25/mo):** Direct influence on roadmap RFCs and early access to pre-release ISO builds.
* **🏢 Organization Sponsor ($100/mo):** Company or individual logo and link on the official Aero Linux portal & README.

👉 **[Sponsor Aero Linux on GitHub Sponsors](https://github.com/sponsors/ronitgupta138)**

---

## 📜 License

Distributed under the **MIT License**. Created by [Ronit Gupta](https://github.com/ronitgupta138) and Contributors.
## Latest Updates

- Sub-350MB idle RAM achievement verified
- Dynamic zRAM (ZSTD) performance tuned
- 45 GTK3 apps running lean
