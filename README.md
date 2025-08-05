# Doxorubicin Fibrosis Model – Open Science Repository

This repository contains the cardiac cell model and MRI-based anatomical data used in the simulations described in our paper:

**In Silico Predictions of Action Potential Propagation in Doxorubicin-induced Cardiotoxicity: a Parametric Study using Preclinical 3D MRI-based Fibrotic LV Models**

## Contents

- `model/`: Mitchell-Schaeffer cell model in PyTorch
- `params/`: Parameters used in simulations
- `data/`: Sample `.mha` anatomical input files
- `scripts/`: Code to run and visualize the action potential

## How to run

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/doxorubicin_fibrosis_model.git
cd doxorubicin_fibrosis_model
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the single-cell simulation:
```bash
python scripts/run_single_cell.py
```


