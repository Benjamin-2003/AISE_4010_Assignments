import csv
from pathlib import Path
p=Path(r"d:\Year-4\AISE4010\Assignment-3\train_dataset.csv")
with p.open() as f:
    r=csv.reader(f)
    first=next(r)
    cols=len(first)
    rows=1+sum(1 for _ in r)
print(f"TRAIN rows={rows}, cols={cols}")
q=Path(r"d:\Year-4\AISE4010\Assignment-3\test_dataset.csv")
with q.open() as f:
    r=csv.reader(f)
    first=next(r)
    cols2=len(first)
    rows2=1+sum(1 for _ in r)
print(f"TEST rows={rows2}, cols={cols2}")
