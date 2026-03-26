# Curriculum Vitae

This repository contains my professional CV, managed as a **Single Source of Truth** using YAML and automated via GitHub Actions.

## 🛠 The Architecture
- **Source:** `data/cv.yml` (All content resides here)
- **Web Engine:** [Hugo](https://gohugo.io/) (Generates the static site)
- **PDF Engine:** Python + [Jinja2](https://jinja.palletsprojects.com/) + LaTeX (Generates the professional PDF)
- **CI/CD:** [GitHub Actions](https://github.com/features/actions)
  - Automatically compiles the LaTeX PDF on every push.
  - Generates a unique **Calendar Versioning (CalVer)** tag.
  - Deploys the web version to GitHub Pages.
  - Attaches the latest PDF to a GitHub Release.

## 📄 View My CV
- **Web Version:** [filippogurioli.github.io/curriculum-vitae/](https://filippogurioli.github.io/curriculum-vitae/)
- **PDF Version:** [Download Latest Release](https://github.com/FilippoGurioli/curriculum-viate/releases/latest)

## 🏗 Setup & Local Development
1. **Python Setup:** `pip install Jinja2 PyYAML`
2. **Generate TeX:** `python generate_latex_cv.py`
3. **Compile PDF:** `pdflatex cv.tex`
4. **Run Web Dev:** `hugo server -D`
