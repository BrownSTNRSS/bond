import numpy as np
import pandas as pd


def annualize_return(ret_series: pd.Series, periods_per_year: int = 12) -> float:
    """年率換算超過リターン（算術平均）"""
    return ret_series.mean() * periods_per_year


def calc_tracking_error(alpha_series: pd.Series, periods_per_year: int = 12) -> float:
    """年率トラッキングエラー（超過リターンの標準偏差×√12）"""
    return alpha_series.std(ddof=1) * np.sqrt(periods_per_year)


def calc_information_ratio(alpha_series: pd.Series, periods_per_year: int = 12) -> float:
    """インフォメーションレシオ = 年率超過リターン / 年率TE"""
    ann_ret = annualize_return(alpha_series, periods_per_year)
    te = calc_tracking_error(alpha_series, periods_per_year)
    if te == 0:
        return np.nan
    return ann_ret / te


def calc_win_rate(alpha_series: pd.Series) -> float:
    """対ベンチマーク勝率（超過リターン > 0 の割合）"""
    return (alpha_series > 0).mean()


def performance_summary(
    portfolio_ret: pd.Series,
    benchmark_ret: pd.Series,
    periods_per_year: int = 12,
) -> pd.DataFrame:
    """
    ポートフォリオとベンチマークのパフォーマンスサマリーを返す。

    Returns
    -------
    pd.DataFrame: 各ポートフォリオの年率リターン・超過リターン・TE・IR・勝率
    """
    alpha = portfolio_ret - benchmark_ret
    return pd.DataFrame(
        {
            "年率リターン (%)": annualize_return(portfolio_ret, periods_per_year) * 100,
            "超過リターン (%)": annualize_return(alpha, periods_per_year) * 100,
            "TE (%)": calc_tracking_error(alpha, periods_per_year) * 100,
            "IR": calc_information_ratio(alpha, periods_per_year),
            "勝率 (%)": calc_win_rate(alpha) * 100,
        },
        index=["値"],
    ).T
