from __future__ import annotations

from typing import TYPE_CHECKING

import polars as pl
from polars.utils.udfs import _get_shared_lib_location

from polars_ole.utils import parse_into_expr

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

lib = _get_shared_lib_location(__file__)

def cum_sum_bounded(values: IntoExpr, lower: IntoExpr, upper: IntoExpr) -> pl.Expr:
    expr = parse_into_expr(values)
    return expr._register_plugin(
        lib=lib,
        symbol="cum_sum_bounded",
        is_elementwise=False,
        args=[lower, upper]
    )

