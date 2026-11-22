"""Figure 4's annotations must not read more into a test statistic than the test supports."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest
from matplotlib.figure import Figure

from cryptoforecast.plots import inference


def _table() -> pd.DataFrame:
    """Two settings Clark-West rejects, and three where DM favours the benchmark and CW < 0."""
    rows = [
        ("BTC", 1, "ridge", 0.76, 2.62),
        ("BTC", 1, "elastic_net", -0.46, 2.57),
        ("ETH", 7, "ridge", 3.15, -0.79),
        ("SOL", 7, "ridge", 3.22, -1.43),
        ("SOL", 7, "gbm", 3.32, -1.39),
    ]
    return pd.DataFrame(rows, columns=["asset", "horizon", "model", "dm_stat", "cw_stat"])


def _render(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Figure:
    captured: list[Figure] = []
    monkeypatch.setattr(
        inference, "finish", lambda fig, out_path, caption=None: captured.append(fig)
    )
    inference.plot_dm_versus_clark_west(_table(), tmp_path / "fig4.png")
    assert len(captured) == 1
    return captured[0]


@pytest.mark.unit
def test_negative_clark_west_is_described_as_a_failure_to_reject(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Clark-West is one-sided: a negative statistic does not reject, it is not evidence of
    inferiority, so the DM-favours-benchmark cluster must not be called 'worse' by both tests.
    """
    ax = _render(monkeypatch, tmp_path).axes[0]
    texts = [t.get_text() for t in ax.texts]
    cluster = [t for t in texts if t.startswith("3 settings")]
    assert cluster == ["3 settings:\nDM favours the benchmark;\nCW does not reject the null"]
    assert not any("worse" in t or "agree" in t for t in texts)


@pytest.mark.unit
def test_clark_west_axis_states_the_sign_convention_not_a_verdict(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """A positive statistic favours the model; only a significant one says the model predicts."""
    ax = _render(monkeypatch, tmp_path).axes[0]
    assert "positive favours the model" in ax.get_ylabel()
    assert "predicts" not in ax.get_ylabel()
