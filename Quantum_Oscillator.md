Yes. If you want **only quantum resonator examples**, I'd build them as a progression from the simplest quantum oscillator to cavity QED and open quantum systems.

I'll use **Python + NumPy + SciPy + Matplotlib**, and keep the physics attached to every example.

> Terminology: the correct term is **quantum resonator**.

---

# 1. Quantum Harmonic Oscillator — Energy Levels

The quantum harmonic oscillator has Hamiltonian

[
\hat H
======

\frac{\hat p^2}{2m}

- \frac{1}{2}m\omega^2\hat x^2.
  ]

Its energy eigenvalues are

[
\boxed{
E_n=\hbar\omega\left(n+\frac12\right)
}
]

where

[
n=0,1,2,\ldots
]

This is the most fundamental quantum resonator.

### Python

```python
import numpy as np
import matplotlib.pyplot as plt

hbar = 1.054571817e-34

# Resonator frequency
f = 1e9
omega = 2 * np.pi * f

# Quantum numbers
n = np.arange(0, 10)

# Energy levels
E = hbar * omega * (n + 0.5)

# Convert to frequency units E / h
h = 6.62607015e-34
E_Hz = E / h

plt.figure(figsize=(7, 5))

for i, energy in enumerate(E_Hz):
    plt.hlines(
        energy,
        0,
        1,
        linewidth=2
    )
    plt.text(
        1.02,
        energy,
        f"n={i}"
    )

plt.xlabel("Quantum number")
plt.ylabel("Energy / h (Hz)")
plt.title("Quantum Harmonic Oscillator")
plt.yticks([])
plt.show()
```

### Physics

Notice that the levels are equally spaced:

[
E_{n+1}-E_n=\hbar\omega.
]

This means the resonator has a characteristic frequency

[
\boxed{\omega}.
]

This is the first important connection between **frequency** and **quantized energy**.

---

# 2. Quantum Harmonic Oscillator — Wavefunctions

Now instead of only calculating energy, calculate the actual quantum states.

The wavefunction is

[
\psi_n(x)
=========

\frac{1}{\sqrt{2^n n!}}
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/4}
H_n(\xi)e^{-\xi^2/2}
]

where

[
\xi=\sqrt{\frac{m\omega}{\hbar}}x.
]

### Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite, factorial

hbar = 1.054571817e-34
m = 1e-30
omega = 2 * np.pi * 1e12

x = np.linspace(-5e-9, 5e-9, 1000)

xi = np.sqrt(m * omega / hbar) * x

plt.figure(figsize=(9, 6))

for n in range(4):

    normalization = (
        1 / np.sqrt(2**n * factorial(n))
    )

    prefactor = (
        m * omega / (np.pi * hbar)
    )**0.25

    psi = (
        normalization
        * prefactor
        * eval_hermite(n, xi)
        * np.exp(-xi**2 / 2)
    )

    plt.plot(
        x * 1e9,
        psi,
        label=f"n={n}"
    )

plt.xlabel("Position (nm)")
plt.ylabel(r"$\psi_n(x)$")
plt.title("Quantum Harmonic Oscillator Wavefunctions")
plt.legend()
plt.grid()
plt.show()
```

### Physics

The quantum resonator doesn't have a classical trajectory (x(t)).

Instead, it has a wavefunction

[
\psi(x).
]

The measurable probability density is

[
\boxed{
P(x)=|\psi(x)|^2
}
]

This is a fundamental difference between classical and quantum resonators.

---

# 3. Probability Density

Modify the previous example to plot

[
|\psi_n(x)|^2.
]

```python
probability = np.abs(psi)**2

plt.plot(x * 1e9, probability)

plt.xlabel("Position (nm)")
plt.ylabel(r"$|\psi(x)|^2$")
plt.title("Quantum Probability Density")

plt.grid()
plt.show()
```

Now you're looking at the probability of finding the oscillator around a particular position.

---

# 4. Quantum Number and Classical Limit

Calculate states:

[
n=0,1,2,10,50.
]

The interesting physics is that at large (n), the quantum probability distribution starts resembling the classical oscillator's behavior.

This is related to the **correspondence principle**.

```python
quantum_numbers = [0, 1, 2, 10, 50]
```

This is an excellent computational experiment.

---

# 5. Quantized Electromagnetic Resonator

Now we make the important transition:

[
\boxed{
\text{Quantum harmonic oscillator}
\rightarrow
\text{quantized EM mode}
}
]

A single electromagnetic cavity mode is mathematically equivalent to a quantum harmonic oscillator.

Its Hamiltonian is

[
\boxed{
\hat H
======

\hbar\omega
\left(
\hat a^\dagger\hat a

- \frac12
  \right)
  }
  ]

where:

- (\hat a) annihilates a photon
- (\hat a^\dagger) creates a photon
- (\hat n=\hat a^\dagger\hat a) is the photon-number operator.

---

# 6. Photon Number States — Fock States

A Fock state is

[
|n\rangle.
]

It has a definite photon number:

[
\hat n|n\rangle=n|n\rangle.
]

The energy is

[
E_n=
\hbar\omega
\left(n+\frac12\right).
]

### Python

```python
import numpy as np

hbar = 1.054571817e-34
f = 5e14

omega = 2 * np.pi * f

for n in range(6):

    energy = hbar * omega * (n + 0.5)

    print(
        f"|{n}> : "
        f"E = {energy:.3e} J"
    )
```

This is the simplest computational representation of a quantum optical resonator.

---

# 7. Photon Energy

Ignore the zero-point term for a moment.

One photon carries:

[
\boxed{
E_\gamma=\hbar\omega
}
]

or:

[
\boxed{
E_\gamma=hf
}
]

### Python

```python
h = 6.62607015e-34

frequency = 5e14

photon_energy = h * frequency

print("Photon energy =", photon_energy, "J")
```

Now change the frequency and observe:

[
E\propto f.
]

---

# 8. Coherent State — Laser-Like Quantum Resonator

A coherent state

[
|\alpha\rangle
]

is one of the most important states in quantum optics.

It satisfies:

[
\hat a|\alpha\rangle
====================

\alpha|\alpha\rangle.
]

Its photon-number distribution is Poissonian:

[
\boxed{
P(n)
====

e^{-|\alpha|^2}
\frac{|\alpha|^{2n}}{n!}
}
]

and:

[
\langle n\rangle=|\alpha|^2.
]

### Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

alpha = 3

n = np.arange(0, 20)

probability = (
    np.exp(-abs(alpha)**2)
    * abs(alpha)**(2*n)
    / factorial(n)
)

plt.bar(n, probability)

plt.xlabel("Photon number n")
plt.ylabel("Probability")
plt.title("Photon Statistics of a Coherent State")

plt.show()
```

### Physics

This is approximately the quantum state of an ideal laser field.

Compare this with a Fock state:

[
|n\rangle.
]

A Fock state has exactly (n) photons.

A coherent state has an uncertainty in photon number.

---

# 9. Vacuum State

The vacuum state is

[
|0\rangle.
]

The average photon number is:

[
\langle n\rangle=0.
]

But the energy is still:

[
\boxed{
E_0=\frac12\hbar\omega.
}
]

This is the **zero-point energy**.

### Python

```python
import numpy as np

hbar = 1.054571817e-34
f = 5e14

omega = 2 * np.pi * f

E_vacuum = 0.5 * hbar * omega

print("Vacuum energy =", E_vacuum, "J")
```

This leads naturally into:

- vacuum fluctuations
- quantum noise
- squeezed states
- cavity QED

---

# 10. Cavity Resonator Modes

Consider a one-dimensional optical cavity of length (L).

The allowed frequencies are approximately

[
\boxed{
\omega_n=
\frac{n\pi c}{L}
}
]

and

[
\boxed{
f_n=\frac{nc}{2L}.
}
]

### Python

```python
import numpy as np
import matplotlib.pyplot as plt

c = 3e8
L = 1e-6

n = np.arange(1, 11)

frequency = n * c / (2 * L)

plt.stem(n, frequency / 1e14)

plt.xlabel("Mode number n")
plt.ylabel("Frequency (10¹⁴ Hz)")
plt.title("Optical Cavity Resonant Modes")

plt.show()
```

These are the classical cavity modes.

When quantized, each mode becomes a quantum harmonic oscillator.

---

# 11. Atom + Quantum Resonator

Now we reach genuine quantum resonance.

Suppose an atom has two states:

[
|g\rangle
]

and:

[
|e\rangle.
]

Their energy difference is:

[
\Delta E=E_e-E_g.
]

Therefore:

[
\boxed{
\omega_a=
\frac{\Delta E}{\hbar}.
}
]

The cavity has frequency:

[
\omega_c.
]

Define detuning:

[
\boxed{
\Delta=\omega_a-\omega_c.
}
]

When:

[
\boxed{
\Delta=0
}
]

the atom and cavity are resonant.

---

# 12. Rabi Oscillations

For a resonantly driven two-level system:

[
P_e(t)
======

\sin^2
\left(
\frac{\Omega t}{2}
\right).
]

Here (\Omega) is the Rabi frequency.

### Python

```python
import numpy as np
import matplotlib.pyplot as plt

Omega = 2 * np.pi * 1e6

t = np.linspace(
    0,
    5e-6,
    1000
)

P_excited = np.sin(Omega * t / 2)**2

plt.plot(
    t * 1e6,
    P_excited
)

plt.xlabel("Time (µs)")
plt.ylabel(r"$P_e(t)$")
plt.title("Rabi Oscillations")

plt.grid()
plt.show()
```

### Physics

The atom does not simply transition once:

[
|g\rangle\rightarrow|e\rangle.
]

Under coherent driving, population can oscillate:

[
|g\rangle
\rightarrow
|e\rangle
\rightarrow
|g\rangle
\rightarrow
|e\rangle
\rightarrow\cdots
]

This is **Rabi oscillation**.

---

# 13. Detuned Quantum Resonance

Now introduce:

[
\Delta=\omega_{\text{drive}}-\omega_0.
]

The generalized Rabi frequency is:

[
\boxed{
\Omega_R=
\sqrt{\Omega^2+\Delta^2}.
}
]

The excited-state population is:

[
\boxed{
P_e(t)
======

\frac{\Omega^2}
{\Omega^2+\Delta^2}
\sin^2
\left(
\frac{\Omega_Rt}{2}
\right).
}
]

### Python

```python
import numpy as np
import matplotlib.pyplot as plt

Omega = 2 * np.pi * 1e6

detunings = [
    0,
    2 * np.pi * 0.5e6,
    2 * np.pi * 2e6
]

t = np.linspace(0, 5e-6, 1000)

plt.figure(figsize=(9, 5))

for Delta in detunings:

    Omega_R = np.sqrt(
        Omega**2 + Delta**2
    )

    P = (
        Omega**2
        / (Omega**2 + Delta**2)
        * np.sin(Omega_R * t / 2)**2
    )

    plt.plot(
        t * 1e6,
        P,
        label=f"Δ/2π = {Delta/(2*np.pi):.1e} Hz"
    )

plt.xlabel("Time (µs)")
plt.ylabel(r"$P_e$")
plt.title("Detuned Rabi Oscillations")

plt.legend()
plt.grid()
plt.show()
```

The important observation is:

[
\boxed{
\text{Increasing detuning reduces the maximum excitation probability.}
}
]

That is quantum resonance in action.

---

# 14. Jaynes–Cummings Resonator

Now combine:

- a two-level atom
- a quantized cavity mode.

The Hamiltonian is:

[
\boxed{
\hat H=
\hbar\omega_c
\hat a^\dagger\hat a

- \frac{\hbar\omega_a}{2}
  \hat\sigma_z
- \hbar g
  \left(
  \hat a^\dagger\hat\sigma\_-
- \hat a\hat\sigma\_+
  \right)
  }
  ]

where (g) is the atom-cavity coupling strength.

This is the **Jaynes–Cummings model**.

---

# 15. Simple Numerical Jaynes–Cummings Model

For a small photon-number Hilbert space, we can construct the matrices explicitly.

```python
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------

wc = 1.0
wa = 1.0
g = 0.2

N = 10


# -----------------------------
# Photon operators
# -----------------------------

a = np.zeros((N, N), dtype=complex)

for n in range(1, N):
    a[n - 1, n] = np.sqrt(n)

adag = a.conj().T

I_cavity = np.eye(N)

# -----------------------------
# Two-level atom operators
# -----------------------------

sigma_plus = np.array([
    [0, 1],
    [0, 0]
], dtype=complex)

sigma_minus = sigma_plus.conj().T

sigma_z = np.array([
    [1, 0],
    [0, -1]
], dtype=complex)

I_atom = np.eye(2)


# -----------------------------
# Tensor products
# -----------------------------

def kron(A, B):
    return np.kron(A, B)


# -----------------------------
# Hamiltonian
# -----------------------------

H_cavity = wc * kron(
    adag @ a,
    I_atom
)

H_atom = (
    wa / 2
    * kron(
        I_cavity,
        sigma_z
    )
)

H_interaction = (
    g
    * (
        kron(adag, sigma_minus)
        +
        kron(a, sigma_plus)
    )
)

H = (
    H_cavity
    + H_atom
    + H_interaction
)


# -----------------------------
# Energy eigenvalues
# -----------------------------

energies = np.linalg.eigvalsh(H)

print("Jaynes-Cummings energies:")
print(energies)
```

This is already a genuine quantum-optics simulation.

---

# 16. Why the Jaynes–Cummings Model Is a Resonator Problem

The cavity has:

[
\omega_c.
]

The atom has:

[
\omega_a.
]

When:

[
\omega_c\approx\omega_a,
]

the interaction becomes strong.

The excitation can move between:

[
\boxed{
\text{atom}
\leftrightarrow
\text{cavity photon}.
}
]

So the cavity and atom form a coupled quantum resonator system.

---

# 17. Cavity Decay

Real quantum resonators are not perfectly isolated.

Photons leak out.

A simple model is:

[
\frac{d\langle n\rangle}{dt}
============================

-\kappa\langle n\rangle.
]

The solution is:

[
\boxed{
\langle n(t)\rangle
===================

\langle n(0)\rangle
e^{-\kappa t}.
}
]

### Python

```python
import numpy as np
import matplotlib.pyplot as plt

kappa = 2e6

n0 = 10

t = np.linspace(0, 5e-6, 1000)

n = n0 * np.exp(-kappa * t)

plt.plot(
    t * 1e6,
    n
)

plt.xlabel("Time (µs)")
plt.ylabel(r"$\langle n\rangle$")
plt.title("Photon Decay from a Quantum Resonator")

plt.grid()
plt.show()
```

The physics is:

[
\boxed{
\text{photon inside cavity}
\rightarrow
\text{cavity loss}
\rightarrow
\text{photon escapes}
}
]

---

# 18. Quantum Resonator Quality Factor

For a cavity:

[
\boxed{
Q=\frac{\omega_c}{\kappa}
}
]

approximately, depending on the precise definition of (\kappa).

For example:

```python
omega_c = 2 * np.pi * 5e9
kappa = 2 * np.pi * 1e6

Q = omega_c / kappa

print("Q =", Q)
```

You can then investigate:

```text
Low Q
  ↓
large losses
  ↓
short photon lifetime

High Q
  ↓
small losses
  ↓
long photon lifetime
```

---

# 19. Photon Lifetime

If:

[
\frac{dn}{dt}=-\kappa n,
]

then the characteristic lifetime is:

[
\boxed{
\tau=\frac{1}{\kappa}.
}
]

### Python

```python
kappa = 1e6

tau = 1 / kappa

print("Photon lifetime =", tau, "seconds")
```

Now you have connected:

[
\boxed{
Q
\leftrightarrow
\kappa
\leftrightarrow
\tau
}
]

which is extremely important in real quantum resonators.

---

# 20. Quantum Resonator with Lindblad Decay

For a more advanced example, use the master equation:

[
\boxed{
\frac{d\rho}{dt}
================

-\frac{i}{\hbar}
[\hat H,\rho]

- \kappa
  \left(
  \hat a\rho\hat a^\dagger
  ***

\frac12
{\hat a^\dagger\hat a,\rho}
\right).
}
]

This is the standard Lindblad description of photon loss from a cavity.

You can implement this with **QuTiP**.

```python
import numpy as np
import matplotlib.pyplot as plt
from qutip import *

N = 20

omega = 2 * np.pi * 5e9
kappa = 1e6

a = destroy(N)

H = omega * a.dag() * a

initial_state = basis(N, 10)

times = np.linspace(
    0,
    5e-6,
    500
)

result = mesolve(
    H,
    initial_state,
    times,
    [np.sqrt(kappa) * a],
    [a.dag() * a]
)

plt.plot(
    times * 1e6,
    result.expect[0]
)

plt.xlabel("Time (µs)")
plt.ylabel(r"$\langle n\rangle$")
plt.title("Quantum Resonator with Photon Loss")

plt.grid()
plt.show()
```

Here the collapse operator

[
\boxed{
C=\sqrt{\kappa}\hat a
}
]

represents photon loss.

---

# 21. Quantum Jump Version

Now take the same cavity but simulate individual quantum trajectories.

Instead of:

[
\rho(t)
]

you simulate:

[
|\psi(t)\rangle.
]

The trajectory looks conceptually like:

```text
continuous evolution
       │
       │
       ▼
   quantum jump
       │
       ▼
photon disappears
       │
       ▼
continuous evolution
       │
       ▼
   another jump
```

After many trajectories:

[
\boxed{
\rho(t)
\approx
\frac{1}{N}
\sum_j
|\psi_j(t)\rangle
\langle\psi_j(t)|
}
]

This connects directly to **Monte Carlo Wave Function / quantum trajectory simulations**.

---

# 22. The Quantum Resonator Learning Path

For your studies, I'd implement the examples in exactly this order:

```text
01_quantum_harmonic_oscillator.py
              ↓
02_energy_levels.py
              ↓
03_wavefunctions.py
              ↓
04_probability_density.py
              ↓
05_classical_correspondence.py
              ↓
06_fock_states.py
              ↓
07_coherent_state.py
              ↓
08_vacuum_state.py
              ↓
09_thermal_state.py
              ↓
10_optical_cavity.py
              ↓
11_two_level_atom.py
              ↓
12_rabi_oscillations.py
              ↓
13_detuned_rabi.py
              ↓
14_jaynes_cummings.py
              ↓
15_cavity_decay.py
              ↓
16_lindblad_resonator.py
              ↓
17_quantum_trajectories.py
```

The really important conceptual chain is:

[
\boxed{
\text{Quantum Harmonic Oscillator}
\rightarrow
\text{Photon Mode}
\rightarrow
\text{Quantum Cavity}
\rightarrow
\text{Two-Level Atom}
\rightarrow
\text{Atom-Cavity Resonance}
\rightarrow
\text{Dissipation}
\rightarrow
\text{Quantum Trajectories}
}
]

That would give you a much stronger computational understanding of **quantum resonators** than simply plotting a resonance curve.
