# Learning ML Model Selection & Time Series Forecasting by Building a Sales Forecasting Pipeline

## Who this is for
You're new to ML but comfortable writing Python, and you want two things at once: (1) a map of the popular ML models — what they're for and when you'd actually reach for each — and (2) a real, hands-on understanding of time series forecasting specifically: stationarity, seasonality, and how to measure accuracy correctly. On top of the ML itself, you want to see what "production-grade code" actually looks like, not just a notebook full of cells.

## What you'll build
A **Sales Forecasting Pipeline** that takes raw, messy daily sales data and:
- Cleans it (missing dates, outliers, duplicate rows)
- Diagnoses it (is it stationary? does it have seasonality/trend?)
- Forecasts future sales with a real time series model
- Evaluates the forecast with the right accuracy metrics
- Is organized the way a real ML pipeline is — not one giant script

## What you'll learn
- A practical map of popular ML model families and when each one is the right tool (Step 1 — conceptual, no code yet)
- Time series specifics: **stationarity** (and the ADF test), **seasonality** vs. **trend**, and why time series data breaks the assumptions most ML models rely on
- Forecast **accuracy metrics** — MAE, RMSE, MAPE — what each one actually measures and when to prefer one over the others
- Production coding habits: separating cleaning / diagnostics / modeling / evaluation into their own functions, config instead of magic numbers, and testing the parts that matter

## Prerequisites
- Python 3.10+, comfortable with pandas basics (reading a CSV, filtering a DataFrame)
- No prior ML or statistics background assumed — every concept is explained when it's first used
- Libraries: `pandas`, `numpy`, `matplotlib`, `statsmodels`, `scikit-learn` (`pip install pandas numpy matplotlib statsmodels scikit-learn`)

## Project setup

```
sales_forecast/
├── data/
│   └── raw_sales.csv
├── cleaning.py        # turn messy raw data into a clean series
├── diagnostics.py      # stationarity + seasonality checks
├── forecasting.py       # baseline + real model
├── evaluation.py        # accuracy metrics
├── config.py            # thresholds, file paths, model settings — no magic numbers in the logic
├── main.py               # wires it all together
└── tests/
    └── test_pipeline.py
```

**Why split it this way?** In a real ML job, cleaning, diagnostics, modeling, and evaluation get changed independently and by different people over time. If they're all tangled in one notebook, changing how you clean data risks silently breaking your model code. Separating them means each piece can be tested and changed on its own — this is one of the biggest differences between "a script that worked once" and production ML code.

---

## Step 1: A practical map of popular ML models (no code yet)

Before building anything, it's worth knowing the landscape, because "which model do I use" is really "what shape is my problem":

| Model family | Examples | Use it when... | Why |
|---|---|---|---|
| Linear / Logistic Regression | Linear Regression, Logistic Regression | You need a simple, interpretable baseline; the relationship is roughly linear | Fast, explainable, and a great sanity-check before trying anything fancier |
| Tree-based models | Decision Tree, Random Forest, Gradient Boosting (XGBoost/LightGBM) | Tabular data with mixed feature types, non-linear relationships | Handle non-linearity and feature interactions without much preprocessing; usually the strongest "default" choice on tabular data |
| Distance-based models | K-Nearest Neighbors, SVM | Smaller datasets, clear geometric structure between points | Simple and effective when data isn't huge, but slow and sensitive to scaling at large scale |
| Clustering (unsupervised) | K-Means, DBSCAN | You don't have labels and want to find natural groupings | No "right answer" to check against — used for exploration/segmentation, not prediction |
| Neural networks | MLPs, CNNs, Transformers | Large datasets, unstructured data (images, text, audio), or when simpler models plateau | Powerful but data-hungry, less interpretable, and usually overkill for small tabular problems |
| **Time series models** | ARIMA/SARIMA, Exponential Smoothing, Prophet | Data ordered in time, where *when* something happened matters, not just its value | Standard ML models assume rows are independent — time series data violates that on purpose (today depends on yesterday), so it needs its own toolbox |

Your project sits in that last row. **Why not just throw a Random Forest at "predict tomorrow's sales"?** You could, but you'd be throwing away the single most useful signal in the data — its position in time — unless you manually engineer that back in (lag features, rolling averages, etc.). Real time series models are built to use that structure directly, which is exactly why the next several steps exist.

---

## Step 2: Load and look at the raw data

```python
# main.py (first pass — will expand as we go)
import pandas as pd

df = pd.read_csv("data/raw_sales.csv")
print(df.head())
print(df.info())
```

Before writing any cleaning code, actually look at what's wrong: missing dates, a stray negative sales value, duplicate rows for the same day, maybe an inconsistent date format. You can't write good cleaning logic for problems you haven't confirmed exist.

---

## Step 3: Data cleaning — production style, not ad-hoc

```python
# config.py
from dataclasses import dataclass

@dataclass(frozen=True)
class CleaningConfig:
    date_column: str = "date"
    value_column: str = "sales"
    outlier_std_threshold: float = 3.0
```

```python
# cleaning.py
import pandas as pd
from config import CleaningConfig

def parse_dates(df: pd.DataFrame, cfg: CleaningConfig) -> pd.DataFrame:
    df = df.copy()
    df[cfg.date_column] = pd.to_datetime(df[cfg.date_column], errors="coerce")
    return df.dropna(subset=[cfg.date_column])

def deduplicate_and_sort(df: pd.DataFrame, cfg: CleaningConfig) -> pd.DataFrame:
    df = df.drop_duplicates(subset=[cfg.date_column]).sort_values(cfg.date_column)
    return df.set_index(cfg.date_column)

def fill_missing_days(df: pd.DataFrame, cfg: CleaningConfig) -> pd.DataFrame:
    full_range = pd.date_range(df.index.min(), df.index.max(), freq="D")
    return df.reindex(full_range).interpolate(method="linear")

def remove_outliers(df: pd.DataFrame, cfg: CleaningConfig) -> pd.DataFrame:
    col = df[cfg.value_column]
    z_scores = (col - col.mean()) / col.std()
    df.loc[z_scores.abs() > cfg.outlier_std_threshold, cfg.value_column] = None
    return df.interpolate(method="linear")

def clean_pipeline(df: pd.DataFrame, cfg: CleaningConfig) -> pd.DataFrame:
    df = parse_dates(df, cfg)
    df = deduplicate_and_sort(df, cfg)
    df = fill_missing_days(df, cfg)
    df = remove_outliers(df, cfg)
    return df
```

**Why each piece matters for time series specifically** (this is different from cleaning tabular ML data):
- **`fill_missing_days`** — a plain ML model doesn't care if row 47 is missing. A time series model does: it needs an unbroken daily sequence to detect patterns like "every 7th day is high" (weekly seasonality). A gap silently shifts every seasonal pattern after it.
- **`remove_outliers` via z-score, not deletion** — dropping rows would create the same gap problem above. Interpolating keeps the sequence continuous while removing the distortion.
- **Config instead of hardcoded `3.0` and column names scattered through the code** — if you later decide 3.0 std is too aggressive, you change it in one place, and every function that depends on it picks it up automatically. Hardcoded "magic numbers" spread through logic are one of the fastest ways real pipelines rot over time.

**Checkpoint:** after `clean_pipeline`, `df.index` should be a continuous daily `DatetimeIndex` with no gaps and no `NaN`s in the sales column.

---

## Step 4: Is it stationary? (the ADF test)

**What stationarity means, concretely:** a stationary series has a roughly constant mean and variance over time — no trend creeping up or down. Most classical time series models (like ARIMA) assume stationarity; if your data has a trend, the model will misread "things are growing" as noise it can't explain, and forecasts will be systematically wrong.

```python
# diagnostics.py
from statsmodels.tsa.stattools import adfuller

def is_stationary(series, significance: float = 0.05) -> bool:
    result = adfuller(series.dropna())
    p_value = result[1]
    return p_value < significance
```

**How to read this:** the Augmented Dickey-Fuller (ADF) test's null hypothesis is "this series is *not* stationary." A small p-value (below your significance threshold, typically 0.05) lets you reject that — i.e., the series *is* stationary. This is a common interview/practical gotcha: a **low** p-value is the *good* sign here, which is the opposite of how p-values usually feel intuitive.

**If it's not stationary**, the standard fix is **differencing** — subtracting each value from the previous one (`series.diff()`) — which often removes a trend and makes the series stationary. You may need to difference more than once for stronger trends.

---

## Step 5: Trend and seasonality — decomposing the series

```python
from statsmodels.tsa.seasonal import seasonal_decompose

def decompose(series, period: int = 7):
    return seasonal_decompose(series, model="additive", period=period)

result = decompose(clean_df["sales"], period=7)
result.plot()
```

- **Trend** — the slow-moving underlying direction (sales generally rising quarter over quarter).
- **Seasonality** — a pattern that repeats at a fixed interval (sales spike every weekend — `period=7` for daily data captures a weekly cycle).
- **Residual** — whatever's left after removing trend and seasonality — ideally close to random noise.

Knowing *which* of these dominates tells you what to configure in your model in the next step — e.g., SARIMA needs you to tell it the seasonal period explicitly.

---

## Step 6: Baseline first — always

```python
# forecasting.py
def naive_forecast(series, horizon: int):
    last_value = series.iloc[-1]
    return [last_value] * horizon
```

**Why bother with something this simple?** Because it's your sanity floor. If your "real" model can't beat "just predict yesterday's value repeated," it's not adding value — and you'd only know that by having a baseline to compare against. Skipping the baseline is one of the most common mistakes beginners make: jumping straight to a complex model with nothing to prove it's actually better than doing nothing clever at all.

---

## Step 7: The real forecasting model — SARIMA

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

def fit_sarima(series, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7)):
    model = SARIMAX(series, order=order, seasonal_order=seasonal_order,
                     enforce_stationarity=False, enforce_invertibility=False)
    return model.fit(disp=False)

def forecast(model_fit, horizon: int):
    return model_fit.forecast(steps=horizon)
```

**What `order` and `seasonal_order` mean, briefly:**
- `order=(p, d, q)` — `p` = how many past values it looks at (autoregression), `d` = how many times to difference the series (tying directly back to Step 4's stationarity check — if the ADF test said "not stationary," `d=1` or higher is why), `q` = how many past forecast errors it corrects for.
- `seasonal_order=(P, D, Q, s)` — the same three ideas, applied at the seasonal period `s` (here, 7 for a weekly pattern found in Step 5).

You don't need to hand-derive the "best" `p`/`d`/`q` values yet — grid-searching them is a real next step, but the point right now is understanding *what* each number represents so a `(1,1,1)` isn't just a magic incantation you copy-pasted.

---

## Step 8: Evaluate — and know which metric answers which question

```python
# evaluation.py
import numpy as np

def mae(y_true, y_pred):
    return np.mean(np.abs(np.array(y_true) - np.array(y_pred)))

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((np.array(y_true) - np.array(y_pred)) ** 2))

def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
```

**When to reach for which — this is the part interviewers and real projects both care about:**
- **MAE (Mean Absolute Error)** — average size of the error, in the same units as your data ("we're off by 12 units on average"). Easy to explain to a non-technical stakeholder.
- **RMSE (Root Mean Squared Error)** — like MAE, but squares errors before averaging, so **large errors are punished disproportionately**. Prefer RMSE when a few big misses are much worse than many small ones (e.g., stockouts matter more than being slightly off every day).
- **MAPE (Mean Absolute Percentage Error)** — expresses error as a *percentage*, which makes it comparable across products/scales ("we're off by 8%" means something on both a $10 item and a $10,000 item). Falls apart when actual values can be zero or near-zero — the percentage explodes or divides by zero.

Run all three against both the naive baseline and the SARIMA forecast — the comparison itself is the point, not any single number in isolation.

---

## Step 9: Wire it into a production-style pipeline

```python
# main.py
from config import CleaningConfig
from cleaning import clean_pipeline
from diagnostics import is_stationary
from forecasting import naive_forecast, fit_sarima, forecast
from evaluation import mae, rmse, mape
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def run_pipeline(raw_path: str, horizon: int = 14):
    cfg = CleaningConfig()
    df = pd.read_csv(raw_path)
    clean_df = clean_pipeline(df, cfg)
    log.info("Stationary: %s", is_stationary(clean_df[cfg.value_column]))

    train, test = clean_df[:-horizon], clean_df[-horizon:]

    baseline_preds = naive_forecast(train[cfg.value_column], horizon)
    model_fit = fit_sarima(train[cfg.value_column])
    model_preds = forecast(model_fit, horizon)

    for name, preds in [("baseline", baseline_preds), ("sarima", model_preds)]:
        log.info("%s -> MAE: %.2f RMSE: %.2f MAPE: %.2f%%",
                  name, mae(test[cfg.value_column], preds),
                  rmse(test[cfg.value_column], preds),
                  mape(test[cfg.value_column], preds))

if __name__ == "__main__":
    run_pipeline("data/raw_sales.csv")
```

**Why `logging` instead of `print`, and why a train/test split held out at the *end* of the series (not randomly shuffled)?** Random shuffling would let the model "see the future" during training — a classic time series mistake, since order is the whole point of the data. `logging` over `print` matters because in a real pipeline you need to control verbosity, redirect output to files, and filter by severity — none of which `print` supports.

## Testing it

```python
# tests/test_pipeline.py
import pandas as pd
from cleaning import fill_missing_days, remove_outliers
from evaluation import mae, mape
from config import CleaningConfig

def test_fill_missing_days_creates_continuous_index():
    cfg = CleaningConfig()
    idx = pd.to_datetime(["2024-01-01", "2024-01-03"])
    df = pd.DataFrame({cfg.value_column: [10, 12]}, index=idx)
    filled = fill_missing_days(df, cfg)
    assert len(filled) == 3  # Jan 1, 2, 3 — the missing day is filled in

def test_mae_is_zero_for_perfect_prediction():
    assert mae([1, 2, 3], [1, 2, 3]) == 0

def test_mape_matches_known_percentage_error():
    assert round(mape([100], [110]), 1) == 10.0
```

These tests target exactly the things most likely to silently break: does gap-filling actually produce a continuous sequence (the whole reason Step 3 exists), and do the metrics compute what you think they compute. Testing that "the pipeline runs" tells you almost nothing; testing these specific behaviors does.

## What makes this production-grade (recap)
- Cleaning, diagnostics, modeling, and evaluation live in separate modules, each independently testable
- Config values (thresholds, column names, model orders) live in one place instead of scattered magic numbers
- A train/test split that respects time order, not a random shuffle
- A baseline model exists specifically so the "real" model's value can be proven, not assumed
- `logging` instead of `print`, and tests that check *behavior*, not just "it runs without crashing"

## Where to go next
- Try grid-searching `(p,d,q)` and `(P,D,Q,s)` combinations and picking the set that minimizes RMSE on a validation split
- Swap SARIMA for Facebook Prophet and compare — Prophet handles multiple seasonalities and holidays more easily, at the cost of being a bit more of a "black box"
- Add rolling-window cross-validation instead of a single train/test split, which is the standard way real forecasting pipelines validate over time
- Once comfortable here, revisit the Step 1 model table and try the same forecasting problem reframed as a supervised regression problem using lag features (yesterday's sales, last week's sales) as inputs to a Random Forest — and compare its accuracy against SARIMA
