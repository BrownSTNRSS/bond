# Bond Strategy: Simple Trend Cash

This repository contains the notebook and data for the Simple Trend Cash U.S. Treasury strategy research.

## Contents

- `notebook/06_simple_trend_cash_comparison.ipynb`
  - Self-contained backtest notebook for Miyazaki-style relative-value signals, Simple Trend Cash, BEI variants, and `MZ_TREND_CASH_ADVANCED_V2`.
- `data/us_treasury_yields_2004_2026.xlsx`
  - Monthly U.S. Treasury yield curve data used by the notebook.
- `data/us_macro_rates_2004_2026.xlsx`
  - Monthly macro/rate data, including 3M, 2Y, 10Y, BEI, and related series.
- `data/backtest_simple_trend_cash_comparison.xlsx`
  - Output workbook from the executed notebook.
- `report/Simple Trend Cash戦略.pdf`
  - PDF report explaining the strategy, formulas, results, and interpretation.

## Main Strategy

The main proposal remains `MZ_SIMPLE_TREND_CASH`.

It starts from the Miyazaki-style signal, converted to monthly comparison by `signal / 6`, and subtracts a transparent duration-loss penalty based on recent 2Y and 10Y yield momentum. Cash is included directly in the same optimization problem.

`MZ_TREND_CASH_ADVANCED_V2` is included as an improvement candidate. It adds a policy-inflation defense condition and a 2s10 inversion cash hurdle, aiming to preserve more return in low-inflation rally/range markets while still defending against 2022-style tightening shocks.

## Reproduce

```bash
uv run jupyter nbconvert --to notebook --execute --inplace notebook/06_simple_trend_cash_comparison.ipynb
```

The notebook writes:

```text
data/backtest_simple_trend_cash_comparison.xlsx
```

## Notes

- No API keys or `.private/` files are included.
- The notebook uses only information available at or before each signal date when computing portfolio weights.
