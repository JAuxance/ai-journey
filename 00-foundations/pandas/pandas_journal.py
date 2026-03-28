import numpy as np
import pandas as pd

s = pd.Series([1, 3,5 ,np.nan, 6, 8])
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)