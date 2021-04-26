import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers


def build_conv_layer(inputs, n_filters):
    conv_layer = layers.Conv2D(n_filters, kernel_size=(4,4), strides=(1,1), padding='same', data_format='channels_first')
    x = conv_layer(inputs)
    batch_layer = layers.BatchNormalization(axis=1)
    x = batch_layer(x)
    relu = layers.ReLU()
    x = relu(x)

    return x

def build_residual_tower(first_layer_output, n_blocks):
    x = first_layer_output
    shortcut = x
    for _ in range(n_blocks):
        x = build_conv_layer(x, 128)
        conv_layer2 = layers.Conv2D(128, kernel_size=(4,4), strides=(1,1), padding='same', data_format='channels_first')
        x = conv_layer2(x)
        batch_layer2 = layers.BatchNormalization(axis=1)
        x = batch_layer2(x)
        x = layers.add([x, shortcut])
        relu2 = layers.ReLU()
        x = relu2(x)
        shortcut = x
    
    return x
    
        
def nn_heads(res_tower_output, n_actions):
    #Evaluation head
    x = build_conv_layer(res_tower_output, 32)
    flatten_layer = layers.Flatten(data_format='channels_first')
    x = flatten_layer(x)
    dense_layer = layers.Dense(1, activation='tanh')
    eval_output = dense_layer(x)

    #Policy Head
    y = build_conv_layer(res_tower_output, 32)
    flatten_layer = layers.Flatten(data_format='channels_first')
    y = flatten_layer(y)
    dense_layer = layers.Dense(n_actions, activation='softmax')
    policy_output = dense_layer(y)

    return eval_output, policy_output
    
def build_model(input_shape, n_actions):
    inputs = keras.Input(shape=input_shape)
    x = build_conv_layer(inputs, 128)
    x = build_residual_tower(x, 4)
    eval_head, policy_head = nn_heads(x, n_actions)

    model = keras.Model(inputs = inputs, outputs=[eval_head, policy_head])

    optimizer = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=optimizer, loss=['mse', 'categorical_crossentropy'])
    
    return model


    

model = build_model((5,6,7), 7)
print(model.summary())