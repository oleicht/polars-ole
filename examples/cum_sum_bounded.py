import polars as pl
import polars.testing
from polars_ole import cum_sum_bounded

df = pl.DataFrame(
    {
        "product": ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
        "values": [1.0, -1, 2, 3, -2, -2, 3, 0],
        "upper": [1.0, 2, 2, 2, 2, 2, 2, 1],
        "lower": [-1.0, -1, -1, -2, -2, -1, -1, -1],
    }
)

df_new = df.with_columns(bounded_cumulative_sum=cum_sum_bounded(values="values", lower="lower", upper="upper").over("product"))
df_ref = df.with_columns(bounded_cumulative_sum=pl.Series([1.0, 0.0, 2.0, 2.0, -2.0, -1.0, 2.0, 1.0]))

polars.testing.assert_frame_equal(df_new, df_ref)
