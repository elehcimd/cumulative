import numpy as np
import pandas as pd

from cumulative import Cumulative

df = pd.DataFrame(
    {
        "base.x": [np.array([0, 1, 2, 3, 4, 5]), np.array([0, 1, 2, 3])],
        "base.y": [np.array([10, 20, 30, 40, 50, 60]), np.array([5, 15, 25, 35])],
        "base.category": ["A", "B"],
    }
)


c = Cumulative(df)
print(c.df)
