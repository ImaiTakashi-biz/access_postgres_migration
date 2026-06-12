"""移行結果レポートの生成処理。"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MigrationReport:
    """移行結果の概要。"""

    title: str
    status: str
    message: str

    def to_markdown(self) -> str:
        """Markdown形式のレポート文字列を返す。"""

        return f"# {self.title}\n\n- 状態: {self.status}\n- 内容: {self.message}\n"


def write_report(report: MigrationReport, output_path: Path) -> None:
    """移行結果レポートをUTF-8で書き出す。"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")
