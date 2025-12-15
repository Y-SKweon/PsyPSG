# PsyPSG

This repository provides a Python-based code for visualizing PsyPSG.  
It automates the loading of CSV datasets and generates publication-ready figures for multiple psychological instruments, including PSQI, ESS, SDS, BRUMS, STAI, and subject-specific hypnograms.  
Each figure can be selectively generated using command-line options, enabling efficient and reproducible workflows for research and data analysis.

---

## Features

### Data Loading
- Reads psychological assessment datasets from CSV format.
- Extracts questionnaire scores such as PSQI, ESS, SDS, STAI, BRUMS, and more.
- Each function requires a `path` argument, which should point to the directory where the **PsyPSG** is downloaded and stored.


### Figure Generation
| Function        | Description |
|----------------|-------------|
| `fig_demo(path)`   | Histograms of participant age and BMI. |
| `fig_sq(path)`     | Sleep-quality classification pie chart and histograms for PSQI and ESS. |
| `fig_sds(path)`    | Depression severity distribution and histogram (SDS). |
| `fig_brums(path)`  | Before/After emotional state transitions for BRUMS subscales. |
| `fig_stai(path)`   | Pre/Post sleep STAI histograms and paired-line plot. |
| `fig_hyp(path, sub)` | Hypnogram visualization for individual subjects. |

All figures are automatically saved as PNG files.

### Statistical Output
- `show(path, head)` prints descriptive statistics and Shapiro–Wilk normality test results for a chosen variable.

---

## Command-Line Usage

Run specific plots via arguments:

```bash
python figure.py --demo        # Age/BMI distribution
python figure.py --sq          # PSQI/ESS visualizations
python figure.py --sds         # SDS distribution
python figure.py --brums       # BRUMS emotional change
python figure.py --stai        # STAI before/after plots
python figure.py --hyp 323     # Hypnogram for subject 323
```
Run specific statistics via arguments:

```bash
python figure.py --show CFQ    # Statistics for CFQ
python figure.py --show age    # Statistics for age
python figure.py --show PSQI   # Statistics for PSQI
```
Statistics shown below:

```bash
CFQ :  13.88 +- 9.19 (1.0-42.0) (p = 0.050)
age :  28.09 +- 2.57 (24.0-35.0) (p = 0.135)
PSQI :  5.06 +- 1.32 (2.0-8.0) (p = 0.207)
```

---
## Output Files

Figures generated include:
```bash
Fig_demo.png
Fig_sq.png
Fig_sds.png
Fig_brums.png
Fig_stai.png
Fig_hyp{sub}.png
```
All files are saved in the working directory.
