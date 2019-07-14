import pickle
import matplotlib.pyplot as plt


def main():
    filename = 'max_boltzmann_run/dqn_MaxBoltzmann.metrics'
    filename = 'eps_greedy_run/dqn_EpsGreedy{}.metrics'
    filtered_data = []
    for i in range(10):
        data = pickle.load(open(filename.format(i), 'rb'))['mean_absolute_error']
        batch_size = 2000
        for j in range(int(len(data) / batch_size)):
            batch = data[j * batch_size : j * batch_size + batch_size]
            filtered_data.append(sum(batch) / batch_size)
    # 'loss', 'mean_absolute_error', 'mean_q']
    plt.plot(filtered_data)
    plt.title('Epsilon Greedy Mean Absolute Error')
    plt.ylabel('Average Mean Absolute Error in Batches of 2000')
    plt.xlabel('Steps in Batches of 2000')
    plt.show()


if __name__ == "__main__":
    main()
