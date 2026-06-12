"""AccessとPostgreSQLのスキーマ対応を扱う。"""

from __future__ import annotations


ACCESS_TO_POSTGRES_TYPE_MAP = {
    "Short Text": "text",
    "Long Text": "text",
    "Number": "numeric",
    "Date/Time": "timestamp",
    "Yes/No": "boolean",
    "Currency": "numeric",
    "AutoNumber": "integer",
}


def map_access_type(access_type: str) -> str:
    """Accessの型名からPostgreSQLの型名を返す。"""

    return ACCESS_TO_POSTGRES_TYPE_MAP.get(access_type, "text")
