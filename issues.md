# Issue Documentation

Tools: Pylint (5.65/10 before, 10.00/10 after), Bandit (4 issues before, 0 after), Flake8 (11 issues before, 0 after).

| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| Shell command built from string (B605) | Security (High) | 52 | `os.system("ssh " + labPc + " lock-screen")` passes user-controlled text to a shell, allowing command injection (e.g. `pc1; rm -rf ~`). | Validate hostname with a regex, then use `subprocess.run([ssh_path, "--", lab_pc, "lock-screen"], check=True)` with no shell. |
| Weak MD5 hash (B324) | Security (High) | 17 | `hashlib.md5` is cryptographically broken and unsuitable for hashing answers. | Replaced with `hashlib.sha256`. |
| Mutable default argument (W0102) | Bug / Pylint Warning (Medium) | 22 | `penalties={}` is created once and shared by every call, so penalties leak between calls/students. | Use `penalties=None` and create a new dict inside the function. |
| Hard-coded password (B105) | Security (Low) | 12 | `PROCTOR_PASSWORD = "proctor-demo"` stores a secret in source control. | Read from environment: `os.environ.get("PROCTOR_PASSWORD", "")`. |
| Non-secure random (B311) | Security (Low) | 20 | `random.choice` is a pseudo-random generator, not suitable for security-sensitive choices. | Use `secrets.choice`. |
| Naming convention (C0103) | Style (Low) | 16, 19, 22, 33, 42, 50 | Functions and args use camelCase (`hashAnswer`, `studentName`, `labPc`) instead of snake_case. | Renamed to `hash_answer`, `student_name`, `lab_pc`, etc., and updated all calls. |
| Missing docstrings (C0114/C0116) | Documentation (Low) | 1, 16-54 | Module and every function lack docstrings. | Added a module docstring and one-line docstrings to all functions. |
| Range/len loop (C0200) | Style (Low) | 24 | `for i in range(len(QUESTIONS))` is unidiomatic. | Use `for i, question in enumerate(QUESTIONS)`. |
| Unnecessary elif after return (R1705) | Style (Low) | 35 | `elif`/`else` after `return` adds needless nesting. | Replace with plain `if` statements and a final `return "C"`. |
| `main()` runs on import | Design (Low) | 67 | Importing the module runs the demo. | Added `if __name__ == "__main__":` guard. |
| Missing blank lines (E302/E305) | Style (Low) | 16-67 | Only 1 blank line around top-level definitions; PEP 8 requires 2. | Added the extra blank line. |
| Missing whitespace around operator (E225) | Style (Low) | 62 | `average=class_average()` | Changed to `average = class_average()`. |
| Line too long (E501) | Style (Low) | 65 | Line is 93 characters (limit 79). | Wrapped the `print` call across two lines. |
