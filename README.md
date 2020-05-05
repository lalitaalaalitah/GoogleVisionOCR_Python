# GoogleVisionOCR_Python
 A script to use python for OCR using Google Vision API

## Steps to setup
1.  Install Python 3
2.  Install dependencies

        python3 -m pip install google-cloud-vision

        Or

        pip install --upgrade google-cloud-vision
3.  Follow instructions on this page : https://cloud.google.com/vision/docs/before-you-begin

        - Create an Google Cloud Account Or Login with your Google ID

        - Create a Cloud Project

        - Enable billing for the project

        - Enable Google Cloud Vision API

        - Set up Authentication

    **Note: You may get an offer to avail USD 300 credit for usage. Accept that. It may enable you to OCR without charges for a few thousand images.**
4.  Open the script and search for "path_to_secret_key.json" and replace it with path of your .json authentication file(which you downloaded while following instructions from 4.)
5.  Save the script.
6.  If needed copy it to system PATH, so that you can call it from anywhere.
7.  Make the script executable.

        chmod +x path_to_script

8.  Follow instructions in the terminal and provide path to (file/folder)
