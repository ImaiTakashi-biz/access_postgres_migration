"""Access DB読み込み処理の入口。"""

from __future__ import annotations

from pathlib import Path


class AccessReader:
    """Access DBからテーブル情報やデータを読み込むクラス。"""

    def __init__(self, access_db_path: Path) -> None:
        self.access_db_path = access_db_path

    def validate_source_exists(self) -> bool:
        """Access DBファイルが存在するか確認する。"""

        return self.access_db_path.exists()
