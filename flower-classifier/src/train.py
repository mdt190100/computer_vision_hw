import tensorflow as tf
from tensorflow.keras import layers, models
from data_preprocess import load_data

def build_model(num_classes):
    model = models.Sequential([
        layers.Rescaling(1./255, input_shape=(180, 180, 3)),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(128, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    train_ds, val_ds, class_names = load_data("../data/flower_photos")
    model = build_model(len(class_names))
    model.summary()

    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=10
    )
    model.save("flower_classifier_model.h5")
