# Reflection Questions

**1. Which issues were the easiest to fix and which were the hardest?**
Style issues (naming, blank lines, docstrings, operator spacing) were easiest because the tools tell you the exact line and fix. The hardest were the security issues, especially `os.system`: removing it required deciding how to validate the hostname, how to call `ssh` safely with `subprocess.run`, and handling the follow-up Bandit warnings (B404, B603, B607) without simply silencing them.

**2. Did the static analysis tools report any false positives?**
Mostly no, but some are context-dependent. B105 (hard-coded password) and B311 (`random`) are low severity: the bonus question is not security sensitive, and the proctor password is only a demo value. They are still good practice to fix. After fixing the shell call, Bandit still reports B404/B603 on `subprocess`; these are generic warnings that I suppressed with targeted `# nosec` comments, because the call uses a fixed argument list, no shell and a validated hostname.

**3. How would you integrate static analysis tools into a real development workflow?**
Run Flake8, Pylint and Bandit locally through pre-commit hooks so problems are caught before a commit, and again in a CI pipeline (e.g. GitHub Actions) on every push and pull request, failing the build on high-severity Bandit findings or a Pylint score below an agreed threshold. Store the configuration in the repo (`.pylintrc`, `setup.cfg`/`.flake8`) so everyone uses the same rules.

**4. What tangible improvements did you see in code quality, readability and security after the fixes?**
The Pylint score rose from 5.65/10 to 10.00/10, Bandit went from 2 High + 2 Low issues to none, and Flake8 went from 11 warnings to zero. The code is now PEP 8 compliant with documentation, no shared mutable state bug, no command-injection risk, a stronger hash and no secret in source. The program output is unchanged (apart from the randomly chosen bonus question).
