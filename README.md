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
- First the video is uploaded as input. Since, it is also compilation of different forms of images.So, the video is segmented into different frames of images. Each video frame image is appeded separately in each list. It is also made sure that each video though having variable lenght are having the same numbers of frame of images. This is done because we have to make consistency for training purpose. 
 
-For instance, I have taken Data sets which has 6 labels and 48 videos.Using this data sets I made equal 40 sets of images for each 48 video.

-CNN-LSTM Architecture: Then the model is passed to CNN -LSTM model for better accuracy. For now got 67% accuracy in validation sets. If the datas are added more, we will soon reach to maximum accuracy.  It can be seen in [video_imagefram converter.ipynb](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/video_imageframe%20converter.ipynb)

-To test the model prediction: [testing.ipynb](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/testing.ipynb) file can be seen.


## Requirements
All the necessary installation to be made are inlisted in [Requirement.txt](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/requirements.txt)

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

## API Reference
Developed a django web application for predicting the activity performed by the video. Before running the website makesure that you have seen the video as mentioned here It can be found in :https://human-activity.herokuapp.com/
PS: There is a small bug in web. Since i have used heroku app to deploy my website. So, it is quite slow in predicting the model. After you upload your video on website wait for atleast 20 to 30 seconds and then click the predict button. Otherwise, your  prediction will show previous video's prediction.

## Tests
Test are shown in [testing.ipynb](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/testing.ipynb)

## Credits
Datasets from:[this github repository]( https://github.com/ksuresh21/HUMAN-ACTIVITY-RECOGNITION/tree/master/DATA )
[Research paper]:(https://www.frontiersin.org/articles/10.3389/frobt.2015.00028/full#h10)
Other project help: stackoverflow

## License
MIT © [Aayushma Pant](https://github.com/Ayushma00/Human_Activity_Recognition/blob/main/LICENSE)
