# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the ONI Framework, please report it responsibly.

### Private Disclosure (Preferred)

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, use one of these methods:

1. **GitHub Private Vulnerability Reporting**
   ```
   https://github.com/qinnovates/mindloft/security/advisories/new
   ```

2. **Email**
   - Contact the maintainer directly (see [ABOUT.md](ABOUT.md))

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Timeline

| Action | Timeframe |
|--------|-----------|
| Acknowledgment | 48 hours |
| Initial assessment | 7 days |
| Fix or mitigation | 30 days (critical), 90 days (other) |

---

## Security Hardening Checklist

> **Status:** Update this checklist as settings are configured.

### High Priority

| Status | Setting | URL |
|--------|---------|-----|
| [ ] | Secret scanning + push protection | [Settings → Security](https://github.com/qinnovates/mindloft/settings/security_analysis) |
| [ ] | Branch protection on `main` | [Settings → Branches](https://github.com/qinnovates/mindloft/settings/branches) |
| [~] | Ruleset (no admin bypass) | [Settings → Rules](https://github.com/qinnovates/mindloft/settings/rules) |
| [ ] | Actions permissions (restrict) | [Settings → Actions](https://github.com/qinnovates/mindloft/settings/actions) |
| [x] | CODEOWNERS for critical files | [.github/CODEOWNERS](.github/CODEOWNERS) |
| [x] | Trusted Publishers (PyPI OIDC) | [.github/workflows/publish.yml](.github/workflows/publish.yml) |

> **Note — Ruleset [~] Backlogged:** Risk accepted for early development phase. No critical or sensitive data at risk. Single maintainer workflow. Ruleset with admin bypass prevention will be applied once external contributors are onboarded.

### Medium Priority

| Status | Setting | URL |
|--------|---------|-----|
| [ ] | Tag protection `v*` | [Settings → Tags](https://github.com/qinnovates/mindloft/settings/tag_protection) |
| [ ] | Private vulnerability reporting | [Settings → Security](https://github.com/qinnovates/mindloft/settings/security_analysis) |
| [ ] | Environment protection (`pypi`) | [Settings → Environments](https://github.com/qinnovates/mindloft/settings/environments) |
| [x] | SECURITY.md | This file |
| [x] | Security audit pipeline | [.github/security-audit/](.github/security-audit/) |
| [x] | Dependabot alerts | [.github/dependabot.yml](.github/dependabot.yml) |

### Low Priority

| Status | Setting | URL |
|--------|---------|-----|
| [ ] | Signed commits required | [Settings → Branches](https://github.com/qinnovates/mindloft/settings/branches) |
| [ ] | CodeQL scanning | [Settings → Security](https://github.com/qinnovates/mindloft/settings/security_analysis) |
| [ ] | Deploy keys audit | [Settings → Keys](https://github.com/qinnovates/mindloft/settings/keys) |
| [ ] | Webhooks audit | [Settings → Webhooks](https://github.com/qinnovates/mindloft/settings/hooks) |

### Account Security

| Status | Setting | URL |
|--------|---------|-----|
| [ ] | 2FA enabled (GitHub) | [GitHub Security](https://github.com/settings/security) |
| [ ] | 2FA enabled (PyPI) | [PyPI 2FA](https://pypi.org/manage/account/two-factor/) |
| [ ] | Review GitHub Apps | [Installed Apps](https://github.com/settings/installations) |
| [ ] | Review OAuth Apps | [OAuth Apps](https://github.com/settings/applications) |

### Incident Response Readiness

| Status | Item | Notes |
|--------|------|-------|
| [ ] | Credential rotation plan | Know how to rotate PyPI tokens, GitHub PATs |
| [ ] | Git history cleanup tools | Install `git-filter-repo` or BFG |
| [ ] | Backup of critical configs | CODEOWNERS, workflows, secrets list |
| [ ] | Contact list for disclosure | Security researchers, downstream users |

---

## Security Measures

### Repository Protection

This repository implements multiple layers of security:

| Protection | Purpose |
|------------|---------|
| **Rulesets** | `main` branch rules without admin bypass |
| **Branch Protection** | `main` branch requires PR approval before merge |
| **CODEOWNERS** | Critical files require maintainer approval |
| **Signed Commits** | Optional verification of commit authenticity |
| **Secret Scanning** | Automatic detection of leaked credentials |
| **Dependabot** | Automated dependency vulnerability alerts |

### Protected Files (CODEOWNERS)

The following files require explicit maintainer approval to modify:

```
.github/CODEOWNERS          # Self-protecting
.github/workflows/          # CI/CD pipelines (prevents malicious publish)
neurosecurity/legacy-core/resources/brand/brand.json   # Brand configuration
neurosecurity/legacy-core/oni-framework/ONI_LAYERS.md  # Authoritative layer definitions
```

### PyPI Publishing Security

Python packages are published using **Trusted Publishers (OIDC)**:

- No API tokens or secrets stored in repository
- Publishing is cryptographically tied to GitHub Actions
- Only workflows from this repository can publish
- Environment protection requires maintainer approval

---

## Security Audit Pipeline

This repository includes an automated security scanning system.

### What It Detects

| Category | Examples |
|----------|----------|
| **API Keys** | OpenAI, Anthropic, Google, Stripe, AWS |
| **Private Keys** | RSA, OpenSSH, PGP, EC, DSA |
| **Tokens** | GitHub, GitLab, NPM, PyPI, JWT, Bearer |
| **Credentials** | Passwords, database connection strings |
| **PII** | Email addresses, SSNs, phone numbers |
| **Sensitive Files** | `.env`, `*.pem`, `*.key`, `credentials.json` |

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  Developer writes code                                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  1. PRE-COMMIT HOOK (Local)                                  │
│     - Scans staged files before commit                       │
│     - Blocks commits containing secrets                      │
│     - Install: ./.github/security-audit/install.sh          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. PULL REQUEST SCAN (GitHub Action)                        │
│     - Scans changed files in PR                              │
│     - Posts findings as PR comment                           │
│     - Uploads SARIF to GitHub Security                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. PUSH SCAN (GitHub Action)                                │
│     - Full repository scan on push to main                   │
│     - Weekly scheduled scan (Sundays 00:00 UTC)              │
└─────────────────────────────────────────────────────────────┘
```

### Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| `critical` | Confirmed secrets, private keys | Blocks PR |
| `high` | Likely secrets, passwords | Blocks PR |
| `medium` | Possible credentials | Warning |
| `low` | Informational (IPs, emails) | Logged |

### Running Manually

```bash
# Scan staged files
python .github/security-audit/scripts/audit.py --staged

# Scan all tracked files
python .github/security-audit/scripts/audit.py --all

# Scan with verbose output
python .github/security-audit/scripts/audit.py --all --verbose
```

---

## Contributing Securely

### Pull Request Requirements

For security reasons, all pull requests must meet these requirements before merging:

1. **Create a Pull Request**
   - Fork the repository or create a feature branch
   - Make your changes
   - Open a PR against `main`

2. **Automated Checks Must Pass**
   - Security audit scan (no secrets detected)
   - All CI tests pass
   - No high/critical vulnerabilities in dependencies

3. **Code Owner Approval Required**
   - PRs modifying protected files require maintainer approval
   - This prevents unauthorized changes to critical infrastructure

4. **Review Process**
   - At least one approving review required
   - Reviewer must be different from PR author (for external contributors)
   - Maintainer reviews for security implications

### Why These Requirements?

| Requirement | Security Reason |
|-------------|-----------------|
| PR required | Prevents direct pushes; creates audit trail |
| Automated scans | Catches secrets before they enter git history |
| Code owner approval | Protects critical files from unauthorized changes |
| Review required | Second pair of eyes catches vulnerabilities |

### For Maintainers

When reviewing PRs, check for:

- [ ] No hardcoded secrets, API keys, or credentials
- [ ] No new dependencies with known vulnerabilities
- [ ] Changes to protected files are intentional and reviewed
- [ ] No modifications to CI/CD workflows without justification
- [ ] Input validation for any user-facing code

---

## Dependency Security

### Dependabot Configuration

Dependabot is configured to:

- Monitor Python dependencies for vulnerabilities
- Monitor GitHub Actions for updates
- Open PRs automatically for security updates

See: [.github/dependabot.yml](.github/dependabot.yml)

### Reviewing Dependency Updates

Before merging Dependabot PRs:

1. Check the changelog for breaking changes
2. Verify the update addresses a real vulnerability
3. Run tests to ensure compatibility

---

## Incident Response

If a security incident occurs:

1. **Contain** - Revoke compromised credentials immediately
2. **Assess** - Determine scope and impact
3. **Remediate** - Remove secrets from git history if needed
4. **Notify** - Inform affected users if applicable
5. **Document** - Record lessons learned

### Removing Secrets from Git History

If a secret is accidentally committed:

```bash
# Use git-filter-repo (preferred) or BFG Repo-Cleaner
# Then force push and rotate the compromised credential
```

**Important:** Always assume a committed secret is compromised. Rotate it immediately.

---

## Security Contacts

- **Primary Maintainer:** [@qikevinl](https://github.com/qikevinl)
- **Private Disclosure:** [GitHub Security Advisories](https://github.com/qinnovates/mindloft/security/advisories/new)

---

## Acknowledgments

We appreciate responsible security researchers who help keep ONI secure. Contributors who report valid vulnerabilities will be acknowledged here (with permission).

---

*Security Policy v1.1.0*
*Last Updated: 2026-01-26*
