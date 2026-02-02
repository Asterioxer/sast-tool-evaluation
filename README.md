# SAST Tool Evaluation

This repository is designed to evaluate and compare Static Application Security Testing (SAST) tools suitable for a containerized, Nomad-based infrastructure. It includes configurations and workflows for **Semgrep**, **SonarQube**, and **Trivy**, aimed at identifying vulnerabilities in code and infrastructure.

## Project Structure

- **`docs/`**: Documentation, including the detailed [SAST Comparison Matrix](docs/sast-comparison.md).
- **`security/`**: Configuration files for the evaluated tools.
    - `security/sast/configs/semgrep/`: Semgrep rules and configuration.
    - `security/sast/configs/sonarqube/`: SonarQube project properties.
    - `security/trivy/`: Trivy configuration.
- **`.github/workflows/`**: CI/CD pipelines demonstrating how these tools are integrated into the build process.
- **`vuln.py`**: A vulnerable Python script used as a test case for scanning.

## Tools Evaluated

### 1. Semgrep
Semgrep is a fast, open-source static analysis tool that finds bugs and enforces code standards.
- **Configuration**: `security/sast/configs/semgrep/semgrep-config.yaml`
- **Usage Strategy**: Running in CI/CD via GitHub Actions.

### 2. SonarQube
SonarQube provides comprehensive code quality and security analysis.
- **Configuration**: `security/sast/configs/sonarqube/sonar-project.properties`
- **Usage Strategy**: Requires a running SonarQube server. The workflow illustrates the client-side scan steps.

### 3. Trivy
Trivy is a comprehensive security scanner for vulnerabilities in container images, filesystems, and git repositories.
- **Configuration**: `security/trivy/trivy.yaml`
- **Usage Strategy**: Scanning the local filesystem (`fs` mode) to detect vulnerabilities in dependencies and configuration files.

## Usage

The primary execution method is through **GitHub Actions**. The workflow is defined in `.github/workflows/sast-eval.yml`.

To run the scans:
1.  Push changes to the `main` branch or open a Pull Request.
2.  The "Run SAST Checks" job will automatically trigger.
3.  **Semgrep**: Scans the codebase using the defined config.
4.  **Trivy**: Scans the filesystem for vulnerabilities.
5.  **SonarQube**: Printed instructions (placeholder) for connecting to a SonarQube server.

## Documentation

For a detailed comparison of these tools based on CI/CD integration, infrastructure footprint, and rule customization, please refer to the [SAST Tool Comparison](docs/sast-comparison.md) document.
