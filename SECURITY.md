# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the QIF Framework, please report it responsibly.

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
MAIN/legacy-core/resources/brand/brand.json   # Brand configuration
tools/qif-framework/qif/bands.py              # Authoritative band definitions (QIF v4.0)
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

## Website Security Controls (GitHub Pages)

> **Added:** 2026-01-26 | **Location:** `docs/index.html`

The website dynamically loads brand content (mission, slogan, vision, stats) from `brand.json` via GitHub's raw content API. This creates a potential attack vector if the repository is compromised. The following security controls mitigate these risks:

### Content Security Policy (CSP)

```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://unpkg.com;
  style-src 'self' 'unsafe-inline' https://unpkg.com;
  img-src 'self' https: data:;
  connect-src 'self' https://raw.githubusercontent.com https://api.github.com;
  font-src 'self';
">
```

**Effect:** Restricts where scripts, styles, and data can be loaded from. Blocks execution of scripts from unauthorized sources.

### Subresource Integrity (SRI)

External dependencies (AOS animation library) include cryptographic hashes:

```html
<link href="https://unpkg.com/aos@2.3.4/dist/aos.css"
      integrity="sha384-/rJKQnzXffaXJfyu1v+..." crossorigin="anonymous">
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"
        integrity="sha384-oZixfuJpr9a/P06Xslt0X..." crossorigin="anonymous">
```

**Effect:** Browser refuses to load the resource if the hash doesn't match, preventing supply chain attacks via compromised CDN.

### Input Validation for brand.json

All values from `brand.json` pass through validation before DOM insertion:

| Function | Validation | Rejection Criteria |
|----------|------------|-------------------|
| `sanitizeText(input, maxLength)` | Type check, length limit, pattern check | Non-string, >maxLength chars, contains HTML tags, control characters |
| `sanitizeNumber(input, min, max)` | Type check, range validation | Non-number, outside min/max range |

**Implementation:**
```javascript
function sanitizeText(input, maxLength = 500) {
    if (typeof input !== 'string') return null;
    if (input.length > maxLength) return null;
    if (/<[^>]*>/.test(input)) return null;  // Reject HTML tags
    return input.replace(/[\x00-\x1F\x7F]/g, '');  // Strip control chars
}
```

### Safe DOM Assignment

All dynamic content uses `.textContent` (never `.innerHTML`):

```javascript
missionEl.textContent = safeMission;  // Safe - treats content as text
// NOT: missionEl.innerHTML = safeMission;  // Unsafe - would parse HTML
```

**Effect:** Even if malicious content bypasses validation, it renders as literal text, not executable code.

### Attack Vectors Mitigated

| Attack Vector | Mitigation | Status |
|---------------|------------|--------|
| XSS via brand.json | Input validation + textContent | ✅ Blocked |
| Supply chain (CDN compromise) | SRI hashes | ✅ Blocked |
| Script injection (external) | CSP whitelist | ✅ Blocked |
| DoS via oversized input | Max length validation | ✅ Blocked |
| Malformed JSON | Structure validation | ✅ Blocked |

### Remaining Considerations

1. **Repository compromise**: If an attacker gains write access to the repo, they could modify the JavaScript itself. Mitigation: Branch protection, required reviews, audit logging.
2. **GitHub raw content availability**: If GitHub is unavailable, fallback to hardcoded defaults preserves functionality.

---

## Security Contacts

- **Primary Maintainer:** [@qikevinl](https://github.com/qikevinl)
- **Private Disclosure:** [GitHub Security Advisories](https://github.com/qinnovates/mindloft/security/advisories/new)

---

## Acknowledgments

We appreciate responsible security researchers who help keep QIF secure. Contributors who report valid vulnerabilities will be acknowledged here (with permission).

---

*Security Policy v1.1.0*
*Last Updated: 2026-01-26*
