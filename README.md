# CVD Restormer Dashboard & Evaluation UI

Interactive research dashboard and visualization platform for **Color Vision Deficiency (CVD)** image recolouring and restoration. This tool visualizes comparative performance metrics, ablation studies, and visual reconstructions across **Protanopia**, **Deuteranopia**, and **Tritanopia**.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fridwanoorrahmanrafi%2FCVD-Result-UI)

---

## 🚀 Features

- **Interactive Metric Exploration**: Comprehensive benchmark tables and visualizations comparing **Proposed Restormer**, **U-Net**, **Plain CNN**, and **No Recolouring Baseline**.
- **Comprehensive Quality Metrics**:
  - **PSNR** & **SSIM** / **MS-SSIM** (Structural Similarity)
  - **MAE** (Mean Absolute Error)
  - **LPIPS** (Perceptual similarity)
  - **$\Delta E_{00}$** (CIE $\Delta E_{00}$ color difference — mean and median)
- **Ablation & Complexity Analysis**: Parameter count, GMACs, latency, and throughput (FPS) across model configurations (Base Restormer, +CBAM, +RDB, +CBAM+RDB).
- **Statistical Significance**: Paired test results with effect sizes and Holm-Bonferroni corrected p-values.
- **Visual Inspection**: Side-by-side visual comparisons using sample images (Ishihara test plates and natural scenes).

---

## 🛠️ Project Structure

```text
├── app.py              # Flask backend serving API & dashboard
├── index.html          # Interactive frontend dashboard
├── results.json        # Evaluation metrics, ablation, and statistical test results
├── requirements.txt    # Python dependencies
├── run.bat             # One-click startup script for Windows
├── samples/            # Sample visual evaluation images
│   ├── fruits.jpg
│   └── ishihara.jpg
└── README.md
```

---

## 💻 Getting Started

### 1. Prerequisites
- Python 3.10+ (or Python 3.11+)

### 2. Installation

Clone the repository:
```bash
git clone https://github.com/ridwanoorrahmanrafi/CVD-Result-UI.git
cd CVD-Result-UI
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard

#### On Windows:
Double-click `run.bat` or run:
```powershell
python app.py
```

#### On Linux / macOS:
```bash
python3 app.py
```

### 4. Access the UI
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 📡 API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Serves the interactive dashboard interface |
| `/api/results` | `GET` | Returns full evaluation JSON dataset |
| `/api/health` | `GET` | Health check endpoint (`{"status": "ok"}`) |
| `/samples/<filename>` | `GET` | Serves sample comparison images |

---

## 📝 Customizing Results

To display results from your own model training or notebook evaluations:
1. Export your evaluation results matching the structure of `results.json`.
2. Overwrite `results.json` in the root directory.
3. Refresh the dashboard!
