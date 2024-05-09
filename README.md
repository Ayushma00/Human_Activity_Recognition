
# Human Activity Recognition Application

Human Activity Recognition is an AI-based project designed to identify and classify human activities for the given input video sources. At its current stage, it can accurately classify up to six activities: Walking, Standing, Talking on the Phone, Squatting, Yoga, and Waving Hands.

## Video Demo

Check out our demo video [here](https://youtu.be/8oalsSVb4eA).

## Tech/Framework Used

- **Operating System:** Ubuntu 20.0 (for training model)
- **Development Environment:** Jupyter Notebook
- **Libraries/Frameworks:**
  - Keras/TensorFlow
- **Web Development:**
  - Built with Atom and Django

## How It Works

1. **Data Preprocessing:** Uploaded videos are segmented into individual frames, ensuring consistency in the number of frames per video for training purposes.
   
2. **CNN-LSTM Architecture:** The model utilizes a CNN-LSTM architecture for enhanced accuracy. Currently achieving 67% accuracy on validation sets, further improvements are anticipated with additional data.

3. **Model Testing:** Model predictions can be tested using the `testing.ipynb` file.

## Requirements

Ensure all necessary installations are performed as listed in `Requirements.txt`.

## Installation

To install locally, execute the `testing.ipynb` file. Ensure all requirements are met beforehand.

## API Reference

We've developed a Django web application for predicting activities from videos. Before utilizing the website, watch the demo video provided [here](https://youtu.be/8oalsSVb4eA).

    *Note: Due to deployment on Heroku, the website may experience delays in predicting models. After uploading your video, wait for 20 to 30 seconds before clicking the predict button to avoid displaying the previous video's prediction. But running on local host will work fine.*

## Tests

Tests can be found in the `testing.ipynb` file.

## Credits

- **Datasets:** [GitHub Repository](insert_dataset_repository_link_here)
- **Research Paper:** [Link](https://www.frontiersin.org/articles/10.3389/frobt.2015.00028/full#h10)
- **Project Assistance:** Stack Overflow

## License

MIT © Aayushma Pant


