# Human Activity Recognition
It is an AI based project that can identify and recognize human activity from a video source and classify it based
on the activity thus performed. For now, it can classify only upto 6 classes: Walking, Standing, Talking to Phone, Squatting, Yoga , Waving Hands.

## Motivation
This project is created for the selection of ALpha AI data science internship.


## Screenshots


## Tech/framework used
<b> For Training Model </b>
- [Jupyter Notebook](https://jupyter.org/install)
- [Keras/Tensorflow](https://keras.io/)

<b> For web developyment Built with </b>
- [Atom](https://atom.io/)
- [Django](https://www.djangoproject.com/)

## How it works?
First the video is uploaded as input. Since, it is also compilation of different forms of images.So, the video is segmented into different frames of images. Each video frame image is appeded separately in each list. It is also made sure that each video though having variable lenght are having the same numbers of frame of images. This is done because we have to make consistency for training purpose. Fo instance, I have taken Data sets from https://github.com/ksuresh21/HUMAN-ACTIVITY-RECOGNITION/tree/master/DATA , using this data sets I made equal 40 sets of images for each 48 video.
CNN-LSTM Architecture: Then the model is passed to CNN -LSTM model for better accuracy. For now got 67% accuracy in validation sets. If the datas are added more, we will soon reach to maximum accuracy.  It can be seen in [video_imagefram converter.ipynb](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/video_imageframe%20converter.ipynb)
To test the model prediction: [testing.ipynb](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/testing.ipynb) file can be seen.


## Code Example
Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests
Describe and show how to run the tests with code examples.

## How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## Contribute

Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus.

## Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project. 

#### Anything else that seems useful

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Yourname]()
