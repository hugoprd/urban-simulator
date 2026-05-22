import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.widgets import Slider
import numpy as np
import pandas as pd


class Simulation:
    def __init__(self, model):
        self.model = model
        self.city_len = 15
        self.grid_density = np.random.uniform(1000, 5000, (self.city_len, self.city_len))

        self.fig, self.ax = plt.subplots(figsize=(8, 9))

        self.fig.subplots_adjust(bottom=0.35)

        self.inicial_val_unemployment = 8.0
        self.inicial_val_evasion = 5.0

        self.colors = ["#2ecc71", "#f1c40f", "#e74c3c"]
        self.cmap_risk = LinearSegmentedColormap.from_list("RiscoUrbano", self.colors)

        self.grid_inicial = self.predict_risk(
            self.inicial_val_unemployment, self.inicial_val_evasion
        )

        self.map_img = self.ax.imshow(
            self.grid_inicial, cmap=self.cmap_risk, interpolation="nearest", vmin=0, vmax=150
        )

        self.ax_unemployment = self.fig.add_axes([0.15, 0.20, 0.65, 0.03])
        self.ax_evasion = self.fig.add_axes([0.15, 0.10, 0.65, 0.03])

        self.unemployment_slider = Slider(
            ax=self.ax_unemployment,
            label="Desemprego (%)",
            valmin=0.0,
            valmax=25.0,
            valinit=self.inicial_val_unemployment,
            color="#3498db",
        )

        self.evasion_slider = Slider(
            ax=self.ax_evasion,
            label="Evasão Escolar (%)",
            valmin=0.0,
            valmax=15.0,
            valinit=self.inicial_val_evasion,
            color="#9b59b6",
        )

    def predict_risk(self, unemployment, evasion):
        dados_predicao = pd.DataFrame(
            {
                "desemprego": np.full(self.city_len**2, unemployment),
                "evasao_escolar": np.full(self.city_len**2, evasion),
                "densidade_populacional": self.grid_density.flatten(),
            }
        )

        return self.model.predict(dados_predicao).reshape((self.city_len, self.city_len))

    def update(self, val):
        new_unemployment = self.unemployment_slider.val
        new_evasion = self.evasion_slider.val

        new_grid = self.predict_risk(new_unemployment, new_evasion)

        self.map_img.set_data(new_grid)
        self.fig.canvas.draw_idle()

    def plot_sim_city(self):
        """
        Create the interactable interface with Sliders to change the variables in real time.
        """
        self.fig.colorbar(self.map_img, ax=self.ax, label="Índice Preditivo de Criminalidade")

        self.ax.set_title(
            "Simulação Visual - Cidade Fictícia\nAjuste os controles abaixo",
            fontsize=14,
            pad=20,
        )
        self.ax.axis("off")

        self.ax.set_xticks(np.arange(-0.5, self.city_len, 1), minor=True)
        self.ax.set_yticks(np.arange(-0.5, self.city_len, 1), minor=True)
        self.ax.grid(which="minor", color="w", linestyle="-", linewidth=2)

        self.unemployment_slider.on_changed(self.update)
        self.evasion_slider.on_changed(self.update)

        plt.show()
