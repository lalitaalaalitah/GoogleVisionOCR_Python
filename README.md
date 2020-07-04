# GoogleVisionOCR_Python
 A script to use python for OCR using Google Vision API

## Steps to setup
1.  Install Python 3
2.  Install dependencies (Check : https://cloud.google.com/python/setup for step 1 and step 2)

        python3 -m pip install google-cloud-vision

        Or

        pip install --upgrade google-cloud-vision
3.  Follow instructions on this page : https://cloud.google.com/vision/docs/before-you-begin

        - Create a Google Cloud Account Or Login with your Google ID

        - Create a Cloud Project

        - Enable billing for the project

        - Enable Google Cloud Vision API

        - Set up Authentication

    **Note: You may get an offer to avail USD 300 credit for usage. Accept that. It may enable you to OCR without charges for a few thousand images.**

4.  Download latest version of the script. Older version are kept just to learn from errors. Don't use older versions.

5.  Open the script and search for "path_to_secret_key.json" and replace it with path of your .json authentication file(which you downloaded while following instructions from 3.)

6.  Save the script.

7.  If needed copy it to system PATH, so that you can call it from anywhere.

8.  Make the script executable.

        chmod +x path_to_script
 
9.  Windows users should check whether their terminal is using utf-8 encoding or not

        chcp 65001

        set PYTHONIOENCODING=utf-8
10.  Now run the script as 

        path_to_script

11.  Follow instructions in the terminal and provide path to (file/folder)
