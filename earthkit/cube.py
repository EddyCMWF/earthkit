
import coucal
import xarray as xr

from earthkit._inputs_transform.__main__ import transform_module_inputs, transform_function_inputs

KWARG_TYPES = {
    "dataarray": xr.DataArray,
    "dataset": xr.Dataset,
    # "data": np.ndarray,
}

aggregate = transform_module_inputs(coucal.aggregate, kwarg_types=KWARG_TYPES)

climate = transform_module_inputs(coucal.climate, kwarg_types=KWARG_TYPES)

# climate.climate_mean = transform_function_inputs(
#     coucal.climate.climatology_mean, **coucal.climate.EARTHKIT_META_THINGS["climatology_mean"]
# )
