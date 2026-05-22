import model.model as ml_model
from frontend.simulate import Simulation


def main():
    modelo_treinado = ml_model.model()

    simulation = Simulation(modelo_treinado)

    simulation.plot_sim_city()


if __name__ == "__main__":
    main()
