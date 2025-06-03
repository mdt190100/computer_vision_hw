import tensorflow as tf
from tensorflow.keras import layers, models
from data_preprocess import load_data

# Thêm data augmentation và chuẩn hóa
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
    layers.Rescaling(1./255)  # Chuẩn hóa pixel
])

def build_model(num_classes):
    base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                                   include_top=False,
                                                   weights='imagenet')
    base_model.trainable = True  # ✅ Cho phép fine-tune

    inputs = layers.Input(shape=(224, 224, 3))
    x = data_augmentation(inputs)  # ✅ Áp dụng augmentation trước khi vào model
    x = base_model(x, training=True)  # Bắt buộc đặt training=True khi fine-tune
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs, outputs)

    model.compile(optimizer=tf.keras.optimizers.Adam(1e-4),  # ✅ Learning rate thấp hơn
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

if __name__ == "__main__":
    train_ds, val_ds, class_names = load_data(r"D:\computer vision\project\flower-classifier\data\flower_photos")

    # Chuẩn hóa ảnh trong validation set
    normalization_layer = tf.keras.layers.Rescaling(1./255)
    val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

    model = build_model(len(class_names))
    history = model.fit(train_ds, validation_data=val_ds, epochs=10)

    # ✅ Lưu model với định dạng mới
    model.save("../model/flower_mobilenetv2.keras")
    print("✅ Model đã được lưu tại: model/flower_mobilenetv2.keras")
