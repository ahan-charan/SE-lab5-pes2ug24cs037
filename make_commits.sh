#!/bin/bash
# Run inside your cloned L5_34_online_exam folder, after copying this whole folder's contents in.
set -e
git add reports/before && git commit -m "Add baseline Pylint, Bandit and Flake8 reports (before fixes)"
cp steps/1_pylint_online_exam.py online_exam.py
git add online_exam.py && git commit -m "Pylint: snake_case names, docstrings, fix mutable default arg, use enumerate, remove no-else-return, add main guard"
cp steps/2_bandit_online_exam.py online_exam.py
git add online_exam.py && git commit -m "Bandit: replace MD5 with SHA-256, os.system with validated subprocess.run, secrets.choice, password from env var"
cp steps/3_flake8_online_exam.py online_exam.py
git add online_exam.py && git commit -m "Flake8: two blank lines between functions, operator spacing, wrap long line"
git add issues.md reflection.md reports/after && git commit -m "Add issues.md, reflection.md and after-fix reports"
git push origin main
