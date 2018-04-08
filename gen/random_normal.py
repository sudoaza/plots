import pandas as pd
import numpy as np
df = pd.DataFrame({"random": np.random.randn(10000)})
df = df * 500 + 700
print(df.to_csv(index=False))
