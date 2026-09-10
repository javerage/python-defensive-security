# Python for Defensive Security: Fundamentals and Local Lab Tooling

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Curriculum: 40 Sessions](https://img.shields.io/badge/curriculum-40%20sessions-green.svg)](#curriculum-roadmap)
[![Security Focus: Defensive](https://img.shields.io/badge/focus-defensive%20security-crimson.svg)](#ethical-confinement--rules-of-engagement)
[![Lab Scope: Localhost Only](https://img.shields.io/badge/scope-127.0.0.1%20only-blueviolet.svg)](#ethical-confinement--rules-of-engagement)
[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-2563eb.svg)](https://javerage.github.io/python-defensive-security/)

> **Hands-on 40-session curriculum: from Python programming fundamentals to defensive security automation, log analysis, and local lab verification.**

🌐 **Live Course Portal & Workbooks:** [https://javerage.github.io/python-defensive-security/](https://javerage.github.io/python-defensive-security/)

<table>
  <tr>
    <td align="center" width="160">
      <img src="docs/qr_code.svg" width="140" height="140" alt="Quick Access QR Code" />
    </td>
    <td>
      <strong>📱 Mobile & Quick Classroom Access</strong><br>
      Scan this QR code with your phone or tablet camera to instantly open the interactive course portal and student workbooks.<br><br>
      ⭐ <em>If you find this material useful for learning or teaching, please star this repository and follow on GitHub!</em>
    </td>
  </tr>
</table>

---

## Course Overview

**Python for Defensive Security (`PyDefSec`)** is a rigorous, 40-session training program designed to take students from foundational software engineering principles to the automated construction of defensive cybersecurity utilities. 

Structured across 10 weeks (four 60-minute sessions per week), the curriculum maintains a strict 50/50 balance between programmatic rigor and applied defensive engineering:

* **Block A (Sessions 01–20): Core Python Fundamentals** — Syntax, data structures, control flow, functions, structured exception handling, modular programming, unit testing, and CLI development using Python 3.13.
* **Block B (Sessions 21–40): Defensive Security Tooling** — Threat modeling, cryptographic hashing, forensic log parsing, local mock HTTP service consumption, network socket telemetry, safe process automation with `subprocess`, and an end-to-end incident response capstone.

---

## Ethical Confinement & Rules of Engagement

> [!IMPORTANT]
> **Strict Localhost Confinement:** All exercises, socket connections, HTTP transactions, and automation routines are strictly confined to local loopback addresses (`127.0.0.1`, `::1`) and controlled laboratory fixtures.

1. **Defensive Purpose Only:** Code and tools created in this course are built solely for system auditing, vulnerability detection, log analysis, and protective monitoring.
2. **Zero External Scanning:** Probing, connecting to, or scanning external third-party networks or unauthorized hosts is strictly prohibited.
3. **No Malicious Payloads:** Creating exploit payloads, rootkits, persistent backdoors, or evasive code violates academic and legal integrity boundaries.

---

## Repository Structure

```text
python-defensive-security/
├── src/                         # Source code, starter templates & runnable scripts
│   └── modulo_01/               # Module 01: Environment and Syntax
│       └── sesion_01/
│           ├── hola.py          # Environment verification baseline script
│           ├── auditoria_local.py # Student autonomous local audit template
│           └── README.md        # Session 01 execution guide and instructions
├── docs/                        # Public student workbooks & GitHub Pages portal
│   ├── index.html               # Web portal index for interactive student access
│   ├── qr_code.svg              # Instant access QR code vector graphic
│   ├── COURSE_BRANDING_EN.md    # Canonical naming specifications and course metadata
│   └── modulo_01/               # Module 01: Environment and Syntax
│       └── sesion_01/
│           └── material_estudiante_sesion_01.html  # Self-contained A4 student workbook
├── .gitignore                   # Security exclusion rules (protects data/private/ & venvs)
└── README.md                    # Course overview and onboarding documentation
```

*Note: Teacher guides, lecture scripts, diagnostic solution keys, and internal syllabus tracking are maintained in a secure private workspace (`data/private/`) excluded from this public repository.*

---

## Laboratory Setup & Prerequisites

All student exercises are built to run directly on the host machine using Python 3.13 and lightweight virtual environments (`venv`), without requiring Docker or cloud accounts.

### 1. Verify Python Version
```bash
python --version
# Expected: Python 3.13.x
```

### 2. Create and Activate Virtual Environment

* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
  *(If script execution is disabled: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`)*

* **Linux / macOS (Bash / Zsh):**
  ```bash
  python3.13 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Verify Isolated Interpreter
```bash
# Verify the interpreter resolves inside .venv
which python      # Linux / macOS
where.exe python  # Windows PowerShell
```

---

## Running Session 01 Scripts

Once inside the activated virtual environment, navigate to the Session 01 source folder:

```bash
cd src/modulo_01/sesion_01
```

1. **Run the baseline verification script:**
   ```bash
   python hola.py
   ```

2. **Run and complete the autonomous audit challenge:**
   ```bash
   python auditoria_local.py
   ```

Refer to [`src/modulo_01/sesion_01/README.md`](src/modulo_01/sesion_01/README.md) for detailed execution instructions and expected outputs.

---

## Curriculum Roadmap

| Block | Modules | Focus & Deliverables |
| :--- | :--- | :--- |
| **Block A** | **M1–M11** (Sessions 01–20) | Environment setup, data types, logic, collections, functions, debugging, file I/O, unit testing with `unittest`/`pytest`, Pydantic runtime schema validation, and mid-term milestone. |
| **Block B** | **M12–M18** (Sessions 21–40) | Ethics & scope declaration, CLI design (`argparse`), structured log analysis, local HTTP mock auditing, TCP socket telemetry on `127.0.0.1`, safe subprocess automation, and final defensive toolkit capstone. |

---

## How to Use Student Workbooks

Student materials are accessible online via GitHub Pages or offline directly in the browser:
- **Online (Interactive Portal):** Open [https://javerage.github.io/python-defensive-security/](https://javerage.github.io/python-defensive-security/) in any modern browser.
- **Offline Capable:** No external CDN or internet connection is required. Double-click `material_estudiante_sesion_01.html` directly from disk.
- **Print / PDF Friendly:** Pre-configured with `@media print` CSS rules. Press `Ctrl + P` (or `Cmd + P`) and select **Save as PDF** on A4 paper for a clean printable workbook.

---

## Contributing & Academic Integrity

This curriculum is developed for academic institutions and self-paced defensive security learners. If you find typographical issues or wish to suggest improvements to student lab exercises, please feel free to submit an issue or pull request.

---

## License

This project is licensed under the [MIT License](LICENSE) — see the repository files for details.
