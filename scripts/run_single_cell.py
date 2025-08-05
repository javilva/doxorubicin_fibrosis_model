import torch
import matplotlib.pyplot as plt
from model.mitchell_schaeffer import dv_dt, dh_dt
from params.default_params import default_parameters

# Params
dt = 0.02  # ms
t_max = 1000  # ms
steps = int(t_max / dt)

v = torch.tensor([default_parameters["v0"]], dtype=torch.float32)
h = torch.tensor([default_parameters["h0"]], dtype=torch.float32)
v_trace = []

# Simulator
for _ in range(steps):
    dv = dv_dt(v, h, **default_parameters["dv_dt"])
    dh_dt(h, v, h, **default_parameters["dh_dt"])
    v = v + dv * dt
    v_trace.append(v.item())

# Plot
plt.plot([i * dt for i in range(steps)], v_trace)
plt.xlabel("Time (ms)")
plt.ylabel("Membrane potential (a.u.)")
plt.title("Mitchell-Schaeffer Action Potential")
plt.grid()
plt.show()
