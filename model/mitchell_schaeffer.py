"""
Mitchell-Schaeffer model of cardiac action potential.
"""

import torch


def C(v, v_max, lambda_):
    return v * (v - lambda_) * (v_max - v)


def J_in(v, h, tau_in, v_max, lambda_):
    return h * C(v, v_max, lambda_) / tau_in


def J_out(v, tau_out):
    return -v / tau_out


def dv_dt(v, h, tau_in, tau_out, v_max, lambda_):
    return J_in(v, h, tau_in, v_max, lambda_) + J_out(v, tau_out)


def dh_dt(out, v, h, tau_open, tau_close, v_gate):
    out[:] = torch.where(v < v_gate, (1 - h) / tau_open, -h / tau_close)


DEFAULT_PARAMETERS = {
    "dh_dt": {"tau_open": 120.0, "tau_close": 189.0, "v_gate": 0.13},
    "dv_dt": {"tau_in": 0.3, "tau_out": 6.0, "v_max": 1.0, "lambda_": 0.01},
    "h0": 1,
    "v0": 0,
}
