
## Building a Convolutional Neural Network from Scratch for Hair Type Classification

In the  _Machine Learning Zoomcamp 2024_, led by Alexey Grigorev at DataTalksClub, we participants are tasked with building a convolutional neural network (CNN) for classifying hair types. Unlike using pre-trained models, the goal here is to design a model from scratch to handle a dataset of hair images, which will be split into training and test sets. This exercise provides a deep dive into the essential principles of CNNs, including data preparation, model construction, and evaluation.

### Dataset and Model Architecture

### 

The dataset for this homework consists of approximately 1,000 images of hair, divided into training and test sets. Each image is of size  200x200x3  (200 pixels by 200 pixels with 3 color channels—RGB). The objective is to design a CNN that will learn from this dataset and predict the hair type. The model construction follows a typical CNN pipeline, beginning with input processing and progressing through various layers.

#### Key Layers in the Model

### 

1.  Input Layer: The model begins by accepting images of shape  (200, 200, 3), representing 200x200 pixel images with 3 RGB channels.
    
2.  Convolutional Layer: The first convolutional layer utilizes  32 filters  with a  (3, 3)  kernel size, applied to the input image. The  ReLU activation  function is used to introduce non-linearity, enabling the model to learn complex patterns in the images.
    
3.  Max Pooling Layer: The next step involves reducing the spatial dimensions of the feature maps produced by the convolutional layer. This is achieved using a  max pooling layer  with a pool size of  (2, 2), which helps reduce computational complexity and retains important features.
    
4.  Flatten Layer: The feature maps from the max pooling layer are flattened into a one-dimensional vector to be passed to the fully connected layers.
    
5.  Dense Layer: A fully connected  Dense layer with 64 neurons  is added. This layer is again activated using the  ReLU function, enabling the model to learn more complex relationships in the data.
    
6.  Output Layer: The final output layer consists of a single neuron with a  sigmoid activation  function. This activation is ideal for binary classification tasks, as it outputs a probability between 0 and 1, indicating whether the hair type is straight or curly.
    

### Model Parameters

### 

The model’s total number of parameters is a key indicator of its complexity. It’s important to note that the  896 parameters  in the convolutional layer represent just part of the model's total complexity. The complete model, including the dense layers, has a total of  20,073,473 parameters. This high number of parameters is indicative of the model's ability to learn intricate features from the data, though it also increases the risk of overfitting if not carefully managed.

### Training the Model

### 

The model is trained using the  Stochastic Gradient Descent (SGD)  optimizer, with a learning rate of  0.002  and momentum set to  0.8. These values help the optimizer navigate the loss surface efficiently and avoid local minima, ensuring that the model converges during training.

The model’s performance is evaluated by tracking both the accuracy and the loss over multiple epochs. The  median training accuracy  for the model across all epochs is approximately  0.72, indicating that the model is able to learn from the data reasonably well. Furthermore, the  standard deviation of the training loss  is  0.068, suggesting that the loss varies slightly across epochs but generally decreases over time.

### Enhancing Performance with Data Augmentation

### 

Data augmentation plays a crucial role in improving the model’s generalization capability. The model is trained with additional transformations applied to the training data, such as rotation, width and height shifts, zoom, and horizontal flipping. These augmentations artificially expand the dataset, preventing overfitting and allowing the model to generalize better to unseen data.

With the augmented data, the model continues training for an additional 10 epochs. The  mean test loss  for this extended training phase is found to be  0.56, showing an improvement in generalization performance. The  average test accuracy  over the last five epochs (epochs 6 through 10) reaches  0.71, demonstrating that the augmented model performs better on the test data.

### Model Evaluation and Results

### 

Upon completing the model training, the final evaluation metrics show that the model performs quite well given the complexity of the task. The test accuracy demonstrates an improvement after data augmentation, reflecting the model's ability to generalize better to new, unseen examples.

-   Total Parameters: 20,073,473
-   Median Training Accuracy: 0.72
-   Standard Deviation of Training Loss: 0.068
-   Mean Test Loss After Augmentation: 0.56
-   Average Test Accuracy (last 5 epochs): 0.71

These results demonstrate that the CNN, even when trained from scratch, can achieve reasonable performance in a complex image classification task like hair type classification.

### Conclusion

### 

Building a CNN from scratch to classify hair types offers a valuable hands-on experience in understanding the inner workings of deep learning. By following a straightforward architecture and applying techniques such as data augmentation, one can significantly enhance the model's ability to generalize to new data. The process emphasizes the importance of thoughtful model design, careful training, and ongoing evaluation to improve performance in real-world applications.

This project is a great starting point for anyone looking to deepen their understanding of CNNs and their practical applications in image classification tasks.
