import pickle
import matplotlib.pyplot as plt


def main():
    filename = 'dqn_MaxBoltzmann{}'
    data = pickle.load(open(filename.format('.metrics'), 'rb'))
    # loss', 'mean_absolute_error', 'mean_q']
    plt.plot(data['loss'])
    plt.show()


if __name__ == "__main__":
    main()
