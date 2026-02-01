# SAST Tool Comparison

## 1. Introduction
This document evaluates and compares SAST tools suitable for a containerized, Nomad-based infrastructure.
**Tools Evaluated:**
- Semgrep
- SonarQube
- Trivy (Optional)

## 2. Comparison Criteria
The tools are evaluated based on:

### 2.1 CI/CD Integration Complexity
- Ease of integration with GitHub Actions.
- Pipeline execution speed.

### 2.2 Infrastructure Footprint
- Resource usage (CPU/RAM).
- Operational cost (Self-hosted vs Managed).

### 2.3 Rule Customization
- Ability to write custom rules.
- False positive management.

### 2.4 Vault & Private Registry Compatibility
- Handling of secrets.
- Scanning within private registries.

## 3. Comparison Matrix (Draft)

| Feature | Semgrep | SonarQube | Trivy |
| :--- | :--- | :--- | :--- |
| **Deployment** | CI-based / SaaS | Server / Managed | CI-based / Standalone |
| **Code Coverage** | Security Focused | Broad Quality + Security | Container + Filesystem |
| **Custom Rules** | Excellent (YAML) | Moderate (Java/Plugin) | Open Policy Agent (Rego) |
| **Speed** | Very Fast | Moderate | Fast |
| **Infra Cost** | Low | High (DB + JVM) | Low |

## 4. Strengths & Weaknesses

### Semgrep
- **Pros**: Fast, highly customizable, lightweight.
- **Cons**: Deep data flow analysis can be expensive (Pro).

### SonarQube
- **Pros**: Comprehensive dashboard, quality gates, history tracking.
- **Cons**: Heavy infrastructure, complex setup.

### Trivy
- **Pros**: One tool for Container + FS + Git, simple CLI.
- **Cons**: SAST capabilities are newer, less mature than specialist tools.

## 5. Recommendation
*To be decided after practical evaluation.*
