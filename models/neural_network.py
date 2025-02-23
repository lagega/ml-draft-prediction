import keras.metrics
from keras import Sequential
from keras.src.layers import Dense
from keras.src.optimizers import Adam


def train_deepish(x_train, x_test, y_train, y_test, columns):
    network = Sequential()
    network.add(Dense(len(columns), activation='relu', input_shape=(x_train.shape[1],)))
    network.add(Dense(64, activation='relu'))
    network.add(Dense(64, activation='relu'))
    network.add(Dense(64, activation='relu'))
    network.add(Dense(1, activation='sigmoid'))
    network.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    print('Starting training...')
    network.fit(x_train, y_train, batch_size=128, epochs=50, verbose=1, validation_data=(x_test, y_test))
    print('Finished training!')

    return network


def train_deep(x_train, x_test, y_train, y_test, columns):
    network = Sequential()
    network.add(Dense(len(columns), activation='relu', input_shape=(x_train.shape[1],)))
    network.add(Dense(64, activation='relu'))
    network.add(Dense(128, activation='relu'))
    network.add(Dense(256, activation='relu'))
    network.add(Dense(256, activation='relu'))
    network.add(Dense(128, activation='relu'))
    network.add(Dense(64, activation='relu'))
    network.add(Dense(1, activation='sigmoid'))
    network.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    print('Starting training...')
    network.fit(x_train, y_train, batch_size=128, epochs=50, verbose=1, validation_data=(x_test, y_test))
    print('Finished training!')

    return network


def train_shallow(x_train, x_test, y_train, y_test, columns):
    network = Sequential()
    network.add(Dense(len(columns), activation='sigmoid', input_shape=(x_train.shape[1],)))
    network.add(Dense(8, activation='sigmoid'))
    network.add(Dense(1, activation='sigmoid'))
    network.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    print('Starting training...')
    network.fit(x_train, y_train, batch_size=128, epochs=50, verbose=1, validation_data=(x_test, y_test))
    print('Finished training!')

    return network
