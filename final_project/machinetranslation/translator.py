'''
This module does translation from English to French and vice versa
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):
    '''
    This function translates text from English to French
    '''
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    print(json.dumps(frenchText['translations'][0]['translation'], indent=2, ensure_ascii=False)) # pylint: disable=unsubscriptable-object
    return frenchText['translations'][0]['translation'] # pylint: disable=unsubscriptable-object

def french_to_english(frenchText):
    '''
    This function translates text from French to English
    '''
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    print(json.dumps(englishText['translations'][0]['translation'], indent=2, ensure_ascii=False)) # pylint: disable=unsubscriptable-object
    return englishText['translations'][0]['translation'] # pylint: disable=unsubscriptable-object
