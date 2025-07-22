import re
from pathlib import Path
from typing import Iterator, List, Tuple

import pandas as pd
import pdfplumber

_regexp = r"^([\d,\s]+)\s+(.+?)\s+(\d+)\s+(\d+)$"


class CuriculumParser:
    def __init__(self, table: Path) -> None:
        self._table = table

    def _extract_from_pdf(self, table: Path) -> Iterator[str]:
        with pdfplumber.open(table) as pdf:
            for page in pdf.pages:
                yield page.extract_text()

    def _handle_row(self, row: str) -> List[Tuple] | None:
        rows = []
        if row:
            for line in row.split("\n"):
                m = re.match(_regexp, line)
                if m:
                    semesters_str, name, zet, hours = m.groups()
                    semesters = re.findall(r"\d+", semesters_str)
                    for sem in semesters:
                        rows.append(
                            {
                                "semester": int(sem),
                                "discipline": name.strip(),
                                "zet": int(zet),
                                "hours": int(hours),
                            }
                        )
        return rows

    def parse_pdf(self) -> pd.DataFrame:
        total = []
        for row in self._extract_from_pdf(self._table):
            rows = self._handle_row(row)

            if not rows:
                continue
            total.extend(rows)
        return pd.DataFrame(total)
