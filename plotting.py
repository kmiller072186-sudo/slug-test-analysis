import matplotlib.pyplot as plt
import numpy as np

class SlugTestPlotter:
    def __init__(self, time, head):
        self.time = time
        self.head = head

    def plot_linear(self):
        plt.figure()
        plt.plot(self.time, self.head, marker='o')
        plt.title('Linear Plot of Slug Test Data')
        plt.xlabel('Time (s)')
        plt.ylabel('Head (m)')
        plt.grid(True)
        plt.show()

    def plot_semilog(self):
        plt.figure()
        plt.semilogy(self.time, self.head, marker='o')
        plt.title('Semi-Log Plot of Slug Test Data')
        plt.xlabel('Time (s)')
        plt.ylabel('Head (m)')
        plt.grid(True)
        plt.show()

    def plot_diagnostic(self):
        plt.figure()
        # Implementing a diagnostic plot example
        plt.plot(np.log(self.time), self.head, marker='o')
        plt.title('Diagnostic Plot of Slug Test Data')
        plt.xlabel('Log(Time)')
        plt.ylabel('Head (m)')
        plt.grid(True)
        plt.show()

    def plot_fitting_window(self):
        plt.figure()
        plt.plot(self.time, self.head, marker='o')
        # Hypothetical fitting window example
        plt.axvspan(10, 20, color='gray', alpha=0.5, label='Fitting Window')
        plt.title('Fitting Window for Slug Test Data')
        plt.xlabel('Time (s)')
        plt.ylabel('Head (m)')
        plt.legend()
        plt.grid(True)
        plt.show()