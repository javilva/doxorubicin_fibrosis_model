default_parameters = {
    "dh_dt": {"tau_open": 120.0, "tau_close": 189.0, "v_gate": 0.13},
    "dv_dt": {"tau_in": 0.3, "tau_out": 6.0, "v_max": 1.0, "lambda_": 0.01},
    "h0": 1.0,
    "v0": 0.0,
}

simulations = [
    {"group": "control", "region": "healthy", "lambda_": 0.01, "sigma": 0.5, "tau_close": 193},
    {"group": "control", "region": "healthy", "lambda_": 0.1, "sigma": 1.0, "tau_close": 220},
    {"group": "dox1", "region": "healthy", "lambda_": 0.01, "sigma": 0.1, "tau_close": 115},
    {"group": "dox1", "region": "healthy", "lambda_": 0.1, "sigma": 0.3, "tau_close": 135},
    {"group": "dox1", "region": "fib",     "lambda_": 0.1, "sigma": 0.2, "tau_close": 55},
    {"group": "dox2", "region": "healthy", "lambda_": 0.01, "sigma": 0.15, "tau_close": 160},
    {"group": "dox2", "region": "healthy", "lambda_": 0.1, "sigma": 0.4, "tau_close": 185},
    {"group": "dox2", "region": "fib",     "lambda_": 0.1, "sigma": 0.4, "tau_close": 195}
]
