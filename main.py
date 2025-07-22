import re

import pandas as pd
import pdfplumber

rows = []

with pdfplumber.open("10033-abit.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            for line in text.split("\n"):
                # Шаблон: один или несколько семестров через запятую, потом название, потом 2 числа (ЗЕТ, часы)
                m = re.match(r"^([\d,\s]+)\s+(.+?)\s+(\d+)\s+(\d+)$", line)
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

df = pd.DataFrame(rows)
print(df)
