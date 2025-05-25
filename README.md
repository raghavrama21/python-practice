# Conda Environment Management Guide

This document provides a concise reference for creating, locating, customizing, exporting, renaming, and removing Conda virtual environments on macOS (and other platforms). Use it as a cheat sheet in your projects.

---

## 1. Conda Basics

- **Conda** is a cross-platform package and environment manager.
- Installs packages (Python and non-Python) and manages isolated environments under a central `conda` installation.

---

## 2. Creating Environments

### 2.1 By Name

```bash
# Create a new env called "myenv" with Python 3.10
conda create -n myenv python=3.10
```

### 2.1 At a Custom Path (Prefix)

```bash
conda create --prefix /path/to/envs/myenv python=3.10
```

- Use full path for activation: conda activate /path/to/envs/myenv

- In a YAML manifest, replace name: with:

```bash
prefix: /path/to/envs/myenv
```

## 3. Locating Your Environments

### 3.1 Show base directory

```bash
conda info --base
```

### 3.2 List all envs with full paths

```bash
conda env list
```

or

```bash
conda info --envs
```

## 4. Exporting & Recreating Environments

### 4.1 Export to YAML

```bash
# Minimal (explicit installs only)
conda env export --from-history > environment.yml

# Full (all dependencies)
conda env export > environment.yml
```

### 4.2 YAML format

```bash
name: myenv         # or 'prefix: /path/to/env'
channels:
  - defaults
dependencies:
  - python=3.10
  - numpy
  - pandas
  - pip
  - pip:
    - package-only-on-pip==1.2.3
```

## 5. Removing Environments

### 5.1 Conda Envs
```bash
### Conda Envs
conda env remove -n myenv
# or
conda remove --name myenv --all

# By path
conda env remove --prefix /full/path/to/env
```
### 5.2 Python venv or virtualenv

```bash
# If active, first deactivate
deactivate
# Then delete the directory
rm -rf /path/to/env_dir
```
