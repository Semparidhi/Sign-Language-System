# Sign-Language-To-Text-and-Speech-Conversion

## Abstract

Sign language, being one of the oldest and most natural forms of communication, is utilized by individuals with disabilities, especially the deaf and dumb. This project introduces a real-time method employing neural networks for finger-spelling-based American Sign Language recognition. A Convolutional Neural Network (CNN) is proposed to recognize hand gestures from camera images, aiming to bridge the communication gap for individuals who use sign language.

## Introduction

American Sign Language serves as a predominant form of communication for the deaf and dumb (D&M) community. Given their communication limitations, our project focuses on developing a model that recognizes finger-spelling-based hand gestures. Deaf and dumb individuals express themselves through hand gestures, a form of nonverbal communication, which our model interprets through computer vision.

![American Sign Language](https://user-images.githubusercontent.com/99630855/201489493-585ffe5c-f460-402a-b558-0d03370b4f92.jpg)


More than 70 million deaf people worldwide use sign languages for communication, allowing them to learn, work, access services, and participate in communities. Recognizing the challenges of making everyone learn sign language, our project aims to create a user-friendly Human-Computer Interface (HCI) that understands American Sign Language. This project endeavors to enhance the lives of deaf and dumb individuals by providing them with a means of communication.

## Objective

The main objective of this project is to create computer software and train a Convolutional Neural Network (CNN) model. This model takes an image of an American Sign Language hand gesture as input and outputs the recognized sign language in both text and audio formats. The goal is to make communication easier for the deaf and dumb community.

## Scope

This system benefits both deaf/dumb individuals and those unfamiliar with sign language. Users communicate through sign language gestures, and the system identifies the intended message, providing output in both text and speech formats.

## Modules

### Data Acquisition

Different approaches to acquiring data about hand gestures include using electromechanical devices and vision-based methods. We use a computer webcam as the input device, and the MediaPipe library is employed for image processing to detect hand gestures.

### Data Pre-processing and Feature Extraction

This module involves processing acquired data, detecting the region of interest (ROI), and applying various image processing techniques. The hand is detected using the MediaPipe Landmark System, addressing challenges related to background and lighting conditions.

### Gesture Classification

The Convolutional Neural Network (CNN) is used for gesture classification. This includes convolution layers, pooling layers, and fully connected layers. Hand landmarks are fed into the model, achieving high accuracy in classifying gestures.

### Text To Speech Translation

Recognized gestures are translated into words, and the system utilizes the `pyttsx3` library to convert the recognized words into speech, providing a simulated real-life dialogue.

## Project Requirements

### Hardware

- Webcam

### Software

- Operating System: Windows 8 and Above
- IDE: PyCharm
- Programming Language: Python 3.9
- Python Libraries: OpenCV, NumPy, Keras, MediaPipe, TensorFlow

## System Diagrams

### System Flowchart

![System Flowchart](https://user-images.githubusercontent.com/99630855/201490238-224f65aa-071f-473a-8c23-a9d60e0a47d8.png)

### Use-case Diagram

![Use-case Diagram](https://user-images.githubusercontent.com/99630855/201490218-85f4c194-0496-4dfb-b920-e486256bd6b7.png)

### DFD Diagram

![DFD Diagram 1](https://user-images.githubusercontent.com/99630855/201490226-966bcc44-8149-433d-ab3b-b0a23deb1c91.png)
![DFD Diagram 2](https://user-images.githubusercontent.com/99630855/201490221-f543fa6d-75ba-4db0-bc35-ee8c06e25018.png)

### Sequence Diagram

![Sequence Diagram](https://user-images.githubusercontent.com/99630855/201490230-b903c365-7a4c-4972-8268-5687060b9cd0.png)

## Conclusion

In conclusion, this project addresses the communication challenges faced by the deaf and dumb community by developing a system capable of recognizing and translating American Sign Language gestures into both text and speech. The modular approach, employing vision-based methods and Convolutional Neural Networks, contributes to the accuracy and effectiveness of the system.

---

