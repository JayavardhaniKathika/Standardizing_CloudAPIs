This project requires flask and postman.

To setup the environment (Linux and mac)
1. Create a project folder and venv folder within it.
   Use the following commands:
   $ mkdir myproject
   $ cd myproject
   $ python3 -m venv venv

2. Activate the environment. 
	$ . venv/bin/activate

3. Within the activated environment, use the following command to install Flask:
	$ pip install Flask

	( Learn more about flask installation or refer the link below for any further refrence:
	https://flask.palletsprojects.com/en/1.1.x/installation/#installation )

4. Make sure you have the main.py in your environment.

5. In the main.py, add the key and endpoint of your Microsoft Azure. To get the key and endpoint you need to have an Azure subscription. 
The below link has the steps to get Azure subscription and get key and endpoint in Prerequisite section.
https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio&pivots=programming-language-python

6. Run the following commands for installing Azure libraries:
pip install azure-ai-textanalytics --pre

7.To use the google APIs we require to have a service account key
To get google service account key follow the below link to set it up.
https://cloud.google.com/natural-language/docs/setup

8. Download the service account key file into your environment. Use the below code in the terminal to export the file.
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/my-key.json"

9. Use the following commands for installing google cloud libraries.
pip install google-cloud-storage
pip install --upgrade google-cloud-language

10. To avoid doing all installs
simple use the requirements.txt provided run the following commands which installs all the libraries for you.
pip install -r requirements.txt

11.Now setup the Postman. Download the Postman Desktop Agent from the below link and set it up.
https://www.postman.com/downloads/

12. After setting up the flask, Azure, google keys and postman and making sure you have the files in your folder now lets run our code using the below instructions.

13. Use the following commnads:
$ export FLASK_APP=main.py
$ flask run
When you run the above commands you can see the application running
 * Running on http://127.0.0.1:5000/

14. Now copy the "http://127.0.0.1:5000/" and use it in the postman.

15. All the API calls are post and use the endpoint you wanted to test.

16. Also pass the json in the body. 
For the APIs like '/api/entity-sentiment', '/api/syntax', '/api/classification', '/api/language_detection', '/api/pii_recognition', '/api/entity_linking', '/api/key_phrase_extraction', '/api/sentiment_analysis' the method is post and the JSON in body is similar to the following.
{
    "text": "We went to Contoso Steakhouse located at midtown NYC last week for a dinner party, and we adore the spot! They provide marvelous food and they have a great menu. The chief cook happens to be the owner (I think his name is John Doe) and he is super nice, coming out of the kitchen and greeted us all. We enjoyed very much dining in the place! The Sirloin steak I ordered was tender and juicy, and the place was impeccably clean. You can even pre-order from their online menu at www.contososteakhouse.com, call 312-555-0176 or send email to order@contososteakhouse.com! The only complaint I have is the food didn't come fast enough. Overall I highly recommend it!"
} 

17. For '/api/entities' you also have to provide the provider to get the JSON response.
{
    "text": "We went to Contoso Steakhouse located at midtown NYC last week for a dinner party, and we adore the spot! They provide marvelous food and they have a great menu. The chief cook happens to be the owner (I think his name is John Doe) and he is super nice, coming out of the kitchen and greeted us all. We enjoyed very much dining in the place! The Sirloin steak I ordered was tender and juicy, and the place was impeccably clean. You can even pre-order from their online menu at www.contososteakhouse.com, call 312-555-0176 or send email to order@contososteakhouse.com! The only complaint I have is the food didn't come fast enough. Overall I highly recommend it!",
    "provider":"GCP"
}

18. When you send the request you can see the JSON response in the postman.





