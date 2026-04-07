# 📊 Statistical Engineering & Simulation Engine

## 🚀 Project Overview

This project implements a **pure Python statistical engine** built from scratch without using external libraries like NumPy or Pandas. The goal is to deeply understand the **mathematical foundations of statistics** and apply them to real-world data and probabilistic simulations.

The system performs:

* Descriptive statistical analysis (mean, median, mode)
* Dispersion analysis (variance, standard deviation)
* Outlier detection
* Monte Carlo simulation to demonstrate the **Law of Large Numbers (LLN)**

---

## 🧠 Core Features

### 1. Statistical Engine (`StatEngine`)

A custom-built class that processes raw numerical data and computes:

#### ✔ Central Tendency

* **Mean**: Arithmetic average
* **Median**: Middle value after sorting
* **Mode**:

  * Supports **multimodal datasets**
  * Returns a message if no repeated values exist

#### ✔ Dispersion

* **Variance**

  * Population: divides by `n`
  * Sample: divides by `n - 1` (Bessel’s Correction)
* **Standard Deviation**

  * Square root of variance

#### ✔ Outlier Detection

* Identifies values beyond a configurable number of standard deviations from the mean
* Default threshold = `2`

---

### 2. Monte Carlo Simulation (`simulate_crashes`)

Simulates a real-world scenario:

* A server has a **4.5% daily crash probability**
* Runs simulations over different time periods (30, 100, 10,000 days)

This demonstrates how **observed probability converges to theoretical probability** as sample size increases.

---

## 📐 Mathematical Logic

### Mean

[
\text{Mean} = \frac{\sum x}{n}
]

---

### Median

* Sort the dataset
* If **odd** → middle value
* If **even** → average of two middle values

---

### Variance

#### Population Variance:

[
\sigma^2 = \frac{\sum (x - \mu)^2}{n}
]

#### Sample Variance (Bessel’s Correction):

[
s^2 = \frac{\sum (x - \bar{x})^2}{n - 1}
]

---

### Standard Deviation

[
\text{Standard Deviation} = \sqrt{\text{Variance}}
]

---

### Outliers

A data point is considered an outlier if:
[
|x - \text{mean}| > (\text{threshold} \times \text{standard deviation})
]

---

## 📁 Project Structure

```
statistical_engine/
│
├── data/
│   └── sample_salaries.json
│
├── src/
│   ├── stat_engine.py
│   └── monte_carlo.py
│
├── tests/
│   └── test_stat_engine.py
│
├── main.py
└── README.md
```

---

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone <your-repo-link>
cd statistical_engine
```

2. Run the main script:

```bash
python main.py
```

---

## 🧪 Running Tests

This project uses Python’s built-in `unittest` framework.

Run tests with:

```bash
python -m unittest
```

---

## 📊 Example Insights

Using the startup salary dataset:

* The **mean is heavily skewed** by extreme values (e.g., 500,000)
* The **median better represents a typical employee**
* **Standard deviation reveals high volatility**
* Outlier detection highlights unrealistic salary values

---

## 🎲 Law of Large Numbers (LLN)

Simulation results show:

* Small sample sizes (e.g., 30 days) produce **unstable probabilities**
* Large samples (e.g., 10,000 days) converge toward the true probability (0.045)

👉 This proves:

> The larger the dataset, the more reliable the estimate.

---

## ✅ Acceptance Criteria Checklist

* [x] Handles empty input safely
* [x] Handles non-numeric data with proper errors
* [x] Correctly computes mean, median, and mode
* [x] Supports multimodal distributions
* [x] Implements both sample and population variance
* [x] Computes standard deviation correctly
* [x] Detects outliers using statistical thresholds
* [x] Monte Carlo simulation implemented
* [x] Demonstrates Law of Large Numbers
* [x] Includes unit tests using `unittest`

---

## 🎥 Video Presentation Guide

This project supports a presentation covering:

* Code structure and design decisions
* Mathematical implementation details
* Statistical insights from the dataset
* Simulation results and probability interpretation

---

## 🏁 Final Note

This project focuses on **understanding the logic behind statistics**, not just using tools. By building everything from scratch, it strengthens both **programming skills** and **statistical intuition** — essential for any data scientist.
