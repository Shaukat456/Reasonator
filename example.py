import numpy as np
import matplotlib.pyplot as plt

from resonator import ClassicalResonator

# --------------------------------------------------
# Example 1: Basic resonator
# --------------------------------------------------

resonator = ClassicalResonator(mass=1.0, damping=0.5, spring_constant=100.0)

print("Natural angular frequency:")
print(f"{resonator.natural_frequency:.2f} rad/s")

print("\nNatural frequency:")
print(f"{resonator.natural_frequency_hz:.2f} Hz")

print("\nDamping ratio:")
print(f"{resonator.damping_ratio:.3f}")

print("\nResonance frequency:")
print(f"{resonator.resonance_frequency():.2f} Hz")


# --------------------------------------------------
# Example 2: Frequency response
# --------------------------------------------------

frequencies = np.linspace(0.1, 5, 1000)

amplitudes = resonator.frequency_response(frequencies, force_amplitude=1.0)


plt.figure(figsize=(9, 5))

plt.plot(frequencies, amplitudes)

plt.xlabel("Driving Frequency (Hz)")
plt.ylabel("Amplitude (m)")
plt.title("Frequency Response of a Classical Resonator")

plt.grid(True)
plt.show()


# --------------------------------------------------
# Example 3: Compare different damping values
# --------------------------------------------------

damping_values = [0.1, 0.5, 2.0, 5.0]

plt.figure(figsize=(9, 5))

for damping in damping_values:

    system = ClassicalResonator(mass=1.0, damping=damping, spring_constant=100.0)

    amplitude = system.frequency_response(frequencies)

    plt.plot(frequencies, amplitude, label=f"b = {damping}")

plt.xlabel("Driving Frequency (Hz)")
plt.ylabel("Amplitude (m)")
plt.title("Effect of Damping on Resonance")

plt.legend()
plt.grid(True)
plt.show()
