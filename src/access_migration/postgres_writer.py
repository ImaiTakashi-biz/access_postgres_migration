"""PostgreSQL書き込み処理の入口。"""

from __future__ import annotations


class PostgresWriter:
    """PostgreSQLへの登録処理を担当するクラス。"""

    def __init__(self, database_url: str) -> None:
        self.database_url = database_url

    def mask_database_url(self) -> str:
        """ログ表示用に接続URLのパスワード部分を伏せる。"""

        if "://" not in self.database_url or "@" not in self.database_url:
            return self.database_url

        scheme, rest = self.database_url.split("://", 1)
        credentials, host_part = rest.split("@", 1)
        user_name = credentials.split(":", 1)[0]
        return f"{scheme}://{user_name}:***@{host_part}"
