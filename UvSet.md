## 📝 Python 3.10, Conda, and uv Environment Setup — Summary

### 1. Which Python version to use
	•	Python 3.10 is the best, most stable version for 2025 — especially for:
	•	TensorFlow
	•	PyTorch
	•	ONNX
	•	YOLO
	•	Hailo tools
	•	Django
	•	Python 3.11 is good but may have minor compatibility gaps.
	•	Avoid 3.12 and 3.13 for ML-heavy workflows.

### 2. Installing Python 3.10 with Homebrew
brew install python@3.10
brew link python@3.10 --force --overwrite

### If other Pythons are installed:
brew unlink python@3.13
brew unlink python@3.12
brew unlink python@3.11
brew unlink python@3.9

### 3. Fixing PATH so Python 3.10 is used by default
Add to ~/.zshrc:
export PATH="/opt/homebrew/opt/python@3.10/bin:$PATH"
Reload:
source ~/.zshrc
hash -r

### 4. Disabling Conda auto-activation (important!)

Conda’s base environment was overriding your Python.

Disable it:
conda config --set auto_activate_base false

Now new shells won’t activate base, which means Homebrew Python wins unless you manually run conda activate.

### 5. uv vs Conda — When to use which

Use uv for:
	•	Normal Python development
	•	School projects (Django, DS/ML work, scripts)
	•	Anything CPU-based
	•	Clean, lightweight environments
	•	Fast installs & modern packaging

Use Conda only for:
	•	GPU environments (PyTorch-CUDA, TensorFlow-GPU)
	•	Installing heavy scientific dependencies that pip struggles with (GDAL, proj, etc.)
	•	Research labs requiring environment.yml

### 6. Creating a uv venv with Python 3.10

Because you have multiple Python versions installed, specify the exact binary:

uv venv --python /opt/homebrew/opt/python@3.10/bin/python3.10

.venv/
  bin/python
  bin/pip
  ...

### 7. Using an alias to simplify venv creation
Add this to ~/.zshrc:

alias uvvenv="uv venv --python /opt/homebrew/opt/python@3.10/bin/python3.10"
Reload:
source ~/.zshrc
Now you can run:
uvvenv
source .venv/bin/activate

## ✔️ Final Workflow Checklist (Recommended)

1. Create project
cd myproject
uvvenv
source .venv/bin/activate

2. Install packages
uv add numpy pandas matplotlib django


### 🔥 How to use uv inside conda (the correct way)

Step 1 — Create a conda environment

Example for GPU PyTorch (just an example):

conda create -n mlgpu python=3.10 pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia
conda activate mlgpu

Or CPU-only:

conda create -n myenv python=3.10
conda activate myenv


Step 3 — Use uv to install packages inside your conda env

After activating the conda env:

uv pip install numpy pandas matplotlib

$CONDA_PREFIX/lib/python3.10/site-packages


### 🧼 Important Rule

❗ NEVER create a uv venv inside a conda env.

That creates a “venv inside a conda env” → confusing & unnecessary.

Correct:
Use conda env → install packages with uv

Incorrect:
Activate conda env → run uv venv (don’t do this)


## 💡 How to verify uv is installing into the conda env

After activating your conda environment:

which python
which pip
which uv

You should see:
	•	python → $CONDA_PREFIX/bin/python
	•	pip → $CONDA_PREFIX/bin/pip
	•	uv → /opt/homebrew/bin/uv
Then install a package:
uv pip install requests
pip list | grep requests

### 🧠 Bonus: Using uv for lockfiles inside conda

If your project uses:
	•	pyproject.toml
	•	uv.lock

You can still do:

🧠 Bonus: Using uv for lockfiles inside conda

If your project uses:
	•	pyproject.toml
	•	uv.lock

You can still do:

uv sync

Inside the active conda environment.

uv will:
	•	Sync packages into the conda Python
	•	Respect your lockfile
	•	NOT create a separate environment

This is incredibly powerful for CUDA workflows.


## 📌 When NOT to use uv inside conda

Avoid uv if installing:
	•	GPU-enabled TensorFlow
	•	GPU-enabled PyTorch (unless conda installed it first)
	•	Packages requiring conda-forge system libs (GDAL, rasterio, geopandas)

Use conda for those.
Then use uv for everything else.

