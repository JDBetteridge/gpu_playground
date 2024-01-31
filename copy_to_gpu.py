import matplotlib.pyplot as plt

from firedrake import *
from firedrake.pyplot import tripcolor


mesh = UnitSquareMesh(20, 20)
V = FunctionSpace(mesh, "Lagrange", 1)

u = TrialFunction(V)
v = TestFunction(V)

f = Function(V)
x, y = SpatialCoordinate(mesh)
f.interpolate(sin(4*pi*x)*sin(4*pi*y))

a = u*v*dx
l = f*v*dx

u_h = Function(V)
solve(a == l, u_h)

print(errornorm(f, u_h))

fig, ax = plt.subplots(2, 1)
fig.set_size_inches(6, 8)

cb1 = tripcolor(u_h, axes=ax[0])
fig.colorbar(cb1, ax=ax[0], vmin=-1, vmax=1)

g = Function(V).interpolate(abs(u_h - f))
cb2 = tripcolor(g, axes=ax[1])
fig.colorbar(cb2, ax=ax[1])

fig.savefig("test.png", dpi=300)
