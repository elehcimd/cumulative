import pandas as pd

from cumulative import Cumulative

df = pd.DataFrame(
    {
        "base.x": [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3]],
        "base.y": [[10, 20, 30, 40, 50, 60], [5, 15, 25, 35]],
    }
)

c = Cumulative(df)
c.copy(src="base", dst="test")

print("Type: ", type(c.df))
print("--")
print(c.df)
