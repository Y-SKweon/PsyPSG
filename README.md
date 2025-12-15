# PsyPSG

This repository provides a Python-based code for visualizing PsyPSG.  
It automates the loading of CSV datasets and generates publication-ready figures for multiple psychological instruments, including PSQI, ESS, SDS, BRUMS, STAI, and subject-specific hypnograms.  
Each figure can be selectively generated using command-line options, enabling efficient and reproducible workflows for research and data analysis.

---

## Features

### Data Loading
- Reads psychological assessment datasets from CSV format.
- Extracts questionnaire scores such as PSQI, ESS, SDS, STAI, BRUMS, and more.

### Figure Generation
| Function        | Description |
|----------------|-------------|
| `fig_demo()`   | Histograms of participant age and BMI. |
| `fig_sq()`     | Sleep-quality classification pie chart and histograms for PSQI and ESS. |
| `fig_sds()`    | Depression severity distribution and histogram (SDS). |
| `fig_brums()`  | Before/After emotional state transitions for BRUMS subscales. |
| `fig_stai()`   | Pre/Post sleep STAI histograms and paired-line plot. |
| `fig_hyp(sub)` | Hypnogram visualization for individual subjects. |

All figures are automatically saved as PNG files.

### Statistical Output
- `show(head)` prints descriptive statistics and Shapiro–Wilk normality test results for a chosen variable.

---

## Command-Line Usage

Run specific plots or statistics via arguments:

```bash
python figure.py --demo        # Age/BMI distribution
python figure.py --sq          # PSQI/ESS visualizations
python figure.py --sds         # SDS distribution
python figure.py --brums       # BRUMS emotional change
python figure.py --stai        # STAI before/after plots
python figure.py --hyp 323     # Hypnogram for subject 323
python figure.py --show CFQ    # Statistics for CFQ
python figure.py --show age    # Statistics for age
python figure.py --show PSQI   # Statistics for PSQI
