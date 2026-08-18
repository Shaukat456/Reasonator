import numpy as np


class ClassicalResonator:
    # """
    # Classical damped, driven harmonic oscillator.

    #     Physical system:

    #         m*x'' + b*x' + k*x = F0*cos(omega*t)

    #     where:
    #         m     = mass
    #         b     = damping coefficient
    #         k     = spring constant
    #         F0    = driving force amplitude
    #         omega = driving angular frequency
    #         x     = displacement
    #     """

    def __init__(self, mass, damping, spring_constant):
        self.m = mass
        self.b = damping
        self.k = spring_constant

    @property
    def natural_frequency(self):
        """
        Natural angular frequency:

            omega_0 = sqrt(k/m)

        Returns rad/s.
        """
        return np.sqrt(self.k / self.m)

    @property
    def natural_frequency_hz(self):
        """
        Natural frequency in Hz:

            f_0 = omega_0 / (2*pi)
        """
        return self.natural_frequency / (2 * np.pi)

    @property
    def damping_ratio(self):
        """
        Damping ratio:

            zeta = b / (2*sqrt(m*k))
        """
        return self.b / (2 * np.sqrt(self.m * self.k))

    def amplitude(self, driving_frequency, force_amplitude=1.0):
        """
        Calculate steady-state displacement amplitude.

        For:

            F(t) = F0*cos(omega*t)

        the amplitude is:

            A = F0 /
                sqrt((k - m*omega^2)^2 + (b*omega)^2)
        """

        omega = 2 * np.pi * driving_frequency

        denominator = np.sqrt((self.k - self.m * omega**2) ** 2 + (self.b * omega) ** 2)

        return force_amplitude / denominator

    def frequency_response(self, frequencies, force_amplitude=1.0):
        """
        Calculate amplitude over a range of driving frequencies.
        """

        frequencies = np.asarray(frequencies)

        return np.array([self.amplitude(f, force_amplitude) for f in frequencies])

    def resonance_frequency(self):
        """
        Approximate resonance frequency for a damped oscillator.

        Angular resonance frequency:

            omega_r = sqrt(omega_0^2 - 2*gamma^2)

        where:

            gamma = b/(2m)

        For weak damping, this is approximately omega_0.
        """

        gamma = self.b / (2 * self.m)

        value = self.natural_frequency**2 - 2 * gamma**2

        if value <= 0:
            return None

        omega_r = np.sqrt(value)

        return omega_r / (2 * np.pi)
