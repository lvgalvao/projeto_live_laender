import pandas as pd

from pathlib import Path

import sqlite3
from sqlite3 import Connection

from pandas import DataFrame

caminho: Path = Path("inventario.db")
con: Connection  = sqlite3.connect(caminho)

data_frame: DataFrame = pd.read_sql(sql="SELECT * FROM inventario", con=con)

print(data_frame)