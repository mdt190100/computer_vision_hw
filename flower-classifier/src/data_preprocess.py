import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.layers import Rescaling, RandomFlip, RandomRotation
from tensorflow.keras import Sequential

def load_data(data_dir, img_size=(224, 224), batch_size=32, val_split=0.2):
    train_ds = image_dataset_from_directory(
        data_dir,
        validation_split=val_split,
        subset="training",
        seed=123,
        image_size=img_size,
        batch_size=batch_size,
    )
    val_ds = image_dataset_from_directory(
        data_dir,
        validation_split=val_split,
        subset="validation",
        seed=123,
        image_size=img_size,
        batch_size=batch_size,
    )
    class_names = train_ds.class_names
    return train_ds, val_ds, class_names

#  Khối xử lý chính
if __name__ == "__main__":
    data_dir = r"D:\computer vision\project\flower-classifier\data\flower_photos"
    train_ds, val_ds, class_names = load_data(data_dir)

    # Augmentation chỉ áp dụng cho tập train
    data_augmentation = Sequential([
        RandomFlip("horizontal"),
        RandomRotation(0.1),
        Rescaling(1./255)
    ])

    train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y))
    val_ds = val_ds.map(lambda x, y: (Rescaling(1./255)(x), y))  # Normalize validation

    print("Số lớp:", len(class_names))
    print(" Classes:", class_names)
