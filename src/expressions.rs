#![allow(clippy::unused_unit)]
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

#[polars_expr(output_type=Float64)]
fn cum_sum_bounded(inputs: &[Series]) -> PolarsResult<Series> {
    let values = inputs[0].f64()?;
    let lower = inputs[1].f64()?;
    let upper = inputs[2].f64()?;

    let res: ChunkedArray<Float64Type> = values
        .into_iter()
        .zip(lower.into_iter())
        .zip(upper.into_iter())
        .scan(0.0, |state, ((v, l), u)| {
            if let Some(value) = v {
                *state = (*state + value).max(l.unwrap()).min(u.unwrap());
                Some(Some(*state))
            } else {
                Some(None)
            }
        })
        .collect();
        
    Ok(res.into_series())
}
