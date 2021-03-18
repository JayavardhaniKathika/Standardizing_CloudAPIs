from flask import Flask
from flask import request
import json
from google.cloud import language_v1
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
key = "PASTE_YOUR_SUBSCRIPTION_KEY_HERE"
endpoint = "PASTE_YOUR_ENDPOINT_HERE"

app = Flask(__name__)

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client



@app.route('/')
def hello_world():
    return {"message":"Hello, Call Machine Learning APIs and get the result from multiple clouds!!!"}

def analyze_entity_sentiment(text_content):
    """
    Analyzing Entity Sentiment in a String
    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'Grapes are good. Bananas are bad.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entity_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Loop through entitites returned from the API
    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))
        # Get the aggregate sentiment expressed for this entity in the provided document.
        sentiment = entity.sentiment
        print(u"Entity sentiment score: {}".format(sentiment.score))
        print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{} = {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
            )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    result_json = response.__class__.to_json(response)
    result_dict = json.loads(result_json)
    
    return result_dict



def analyze_entities(text_content):
    """
    Analyzing Entities in a String
    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

    # Loop through entitites returned from the API
    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))

            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
            )



    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    result_json = response.__class__.to_json(response)
    result_dict = json.loads(result_json)
    json.dumps(result_dict)

    with open('analyze_entities.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=4)
    return result_dict

def analyze_syntax(text_content):
    """
    Analyzing Syntax in a String
    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'This is a short sentence.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(request = {'document': document, 'encoding_type': encoding_type})
    # Loop through tokens returned from the API
    for token in response.tokens:
        # Get the text content of this token. Usually a word or punctuation.
        text = token.text
        print(u"Token text: {}".format(text.content))
        print(
            u"Location of this token in overall document: {}".format(text.begin_offset)
        )
        # Get the part of speech information for this token.
        # Parts of spech are as defined in:
        # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
        part_of_speech = token.part_of_speech
        # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
        print(
            u"Part of Speech tag: {}".format(
                language_v1.PartOfSpeech.Tag(part_of_speech.tag).name
            )
        )
        # Get the voice, e.g. ACTIVE or PASSIVE
        print(u"Voice: {}".format(language_v1.PartOfSpeech.Voice(part_of_speech.voice).name))
        # Get the tense, e.g. PAST, FUTURE, PRESENT, et al.
        print(u"Tense: {}".format(language_v1.PartOfSpeech.Tense(part_of_speech.tense).name))
        # See API reference for additional Part of Speech information available
        # Get the lemma of the token. Wikipedia lemma description
        # https://en.wikipedia.org/wiki/Lemma_(morphology)
        print(u"Lemma: {}".format(token.lemma))
        # Get the dependency tree parse information for this token.
        # For more information on dependency labels:
        # http://www.aclweb.org/anthology/P13-2017
        dependency_edge = token.dependency_edge
        print(u"Head token index: {}".format(dependency_edge.head_token_index))
        print(
            u"Label: {}".format(language_v1.DependencyEdge.Label(dependency_edge.label).name)
        )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    result_json = response.__class__.to_json(response)
    result_dict = json.loads(result_json)
    return result_dict

def classify_text(text_content):
    """
    Classifying Content in a String
    Args:
      text_content The text content to analyze. Must include at least 20 words.
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    response = client.classify_text(request = {'document': document})

    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(u"Category name: {}".format(category.name))
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(u"Confidence: {}".format(category.confidence))
    
    result_json = response.__class__.to_json(response)
    result_dict = json.loads(result_json)
    return result_dict

def language_detection_example(data):
    client = authenticate_client()
    try:
        documents = [data]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)
        response['primary_language'] = dict(response['primary_language'])
        return dict(response)
    except Exception as err:
        print("Encountered exception. {}".format(err))

def pii_recognition_example(text):
    client = authenticate_client()
    documents = [text]
    response = client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("Redacted Text: {}".format(doc.redacted_text))
        list_entities = []
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("\tCategory: {}".format(entity.category))
            print("\tConfidence Score: {}".format(entity.confidence_score))
            print("\tOffset: {}".format(entity.offset))
            print("\tLength: {}".format(entity.length))
            list_entities.append(dict(entity))
        #response = dict(response)
        #response['entities'] = list_entities
    response[0] = dict(response[0])
    response[0]['entities'] = list_entities
    print(response)
    return str(response)


def entity_linking_example(text):
    client = authenticate_client()
    try:
        documents = [text]
        result = client.recognize_linked_entities(documents = documents)[0]

        print("Linked Entities:\n")
        list_entities = []
        for entity in result.entities:
            print("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url,
            "\n\tData Source: ", entity.data_source)
            print("\tMatches:")
            list_matches = []
            for match in entity.matches:
                print("\t\tText:", match.text)
                print("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))
                print("\t\tOffset: {}".format(match.offset))
                print("\t\tLength: {}".format(match.length))
                list_matches.append(dict(match))
            # result[entity] = dict(result[entity])
            entity['matches'] = list_matches
            list_entities.append(dict(entity))
        #print(list_entities)
        result['entities'] = list_entities
        return dict(result)
    except Exception as err:
        print("Encountered exception. {}".format(err))


def key_phrase_extraction_example(text):
    client = authenticate_client()

    try:
        documents = [text]
        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print(response)
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)
        response = dict(response)
        return response
    except Exception as err:
        print("Encountered exception. {}".format(err)) 

def convert_microsoft_entity():
    with open('entity_recog.json') as f:
        data = json.load(f)
    general_json = []
    
    for entity in data['entities']:
        new_entity = {}
        new_entity['name'] = entity['text']
        new_entity['category'] = entity['category']
        #new_entity['confidence_score'] = entity['confidence_score']
        new_entity['length'] = entity['length']
        new_entity['offset'] = entity['offset']
        general_json.append(new_entity)
    print(general_json)
    return str(general_json)
        
def convert_google_entity():
    type_map = ['Unknown', 'Person', 'Location', 'Organization', 'Event', 'Work of Art',
                'Consumer Good', 'Other', 'Phone Number', 'Address', 'Date', 'Number', 'Price']
    with open('analyze_entities.json') as f:
        data = json.load(f)
    general_json = []
    #data = data[0]
    #print(data)
    for entity in data['entities']:
        new_entity = {}
        new_entity['name'] = entity['name']
        new_entity['category'] = type_map[int(entity['type'])]
        new_entity['length'] = len(entity['name'])
        new_entity['offset'] = entity['mentions'][0]['text']['beginOffset']
        general_json.append(new_entity)
    print(general_json)
    return str(general_json)

def entity_recognition_example(text):
    client = authenticate_client()
    try:
        documents = [text]
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        entities_list = []
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")
            entities_list.append(dict(entity))
        result['entities'] = entities_list
        print(dict(result))
        with open("entity_recog.json", "w") as outputfile:
            json.dump(dict(result), outputfile, indent=4)
        return dict(result)
    except Exception as err:
        print("Encountered exception. {}".format(err))

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(
            "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
        )

    print(
        "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    )
    return 0


#Google sentiment analysis
def analyze(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()


    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})
    # Print the results
    print_result(annotations)
    result_json = annotations.__class__.to_json(annotations)
    result_dict = json.loads(result_json)
    json.dumps(result_dict)

    with open('google.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=4)
    return result_dict

#Azure sentiment Analysis
def sentiment_analysis_example(text):

    client = authenticate_client()

    documents = [text]
    response = client.analyze_sentiment(documents=documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    response['confidence_scores'] = dict(response['confidence_scores'])
    sentences_list = []
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))
        sentence['confidence_scores'] = dict(sentence['confidence_scores'])
        sentences_list.append(dict(sentence))
    response['sentences'] = sentences_list
    with open("microsoft.json", "w") as outputfile:
        json.dump(dict(response), outputfile, indent=4)
    return dict(response)



def sentiment():
    google_file = open("google.json", "r")
    microsoft_file = open("microsoft.json", "r")
    # google_file = open("sentiment_analysis.json", "r")
    # microsoft_file = open("sentient_analysis.json", "r")
    google_json = json.loads(google_file.read())
    microsoft_json = json.loads(microsoft_file.read())
    google_microsoft_json = {}
    google_microsoft_json["sentiment"] = {}
    sentences = []
    for sentence in microsoft_json["sentiment"]["documents"][0]["sentences"]:
        sentences.append({
            "microsoft": sentence
        })
    i = 0
    offset = 0
    for sentence in google_json[0]["sentences"]:
        if (sentences[i]["microsoft"]["offset"] == offset):
            sentences[i]["google"] = sentence
        offset += len(sentence["text"]["content"]) + 1
        i += 1
    google_microsoft_json["sentiment"]["sentences"] = sentences
    print(google_microsoft_json["sentiment"])
    return dict(google_microsoft_json["sentiment"])


    


#Google
@app.route('/api/entity-sentiment',methods=['POST'])
def entitySentiment():
    # print(request.get_json())
    content=request.get_json()
    data=content["text"]
    return analyze_entity_sentiment(data)

#Google
@app.route('/api/entities_gcp',methods=['POST'])
def entities_gcp():
    # print(request.get_json())
    content=request.get_json()
    data=content["text"]
    return analyze_entities(data)

#Azure
@app.route('/api/entities_azure',methods=['POST'])
def entities_azure():
    # print(request.get_json())
    content=request.get_json()
    data=content["text"]
    return entity_recognition_example(data)


#Google
@app.route('/api/syntax',methods=['POST'])
def syntax():
    # print(request.get_json())
    content=request.get_json()
    data=content["text"]
    return analyze_syntax(data)


#Google
@app.route('/api/classification',methods=['POST'])
def classify():
    content=request.get_json()
    data=content["text"]
    return classify_text(data)

#Google
@app.route('/api/sentiment_gcp',methods=['POST'])
def sentiment_gcp():
    content=request.get_json()
    data=content["text"]
    return analyze(data)

#Azure
@app.route('/api/sentiment_azure',methods=['POST'])
def sentiment_azure():
    content=request.get_json()
    data=content["text"]
    return sentiment_analysis_example(data)

#Azure
@app.route('/api/language_detection',methods=['POST'])
def language():
    content=request.get_json()
    data=content["text"]
    return language_detection_example(data)

#Azure
@app.route('/api/pii_recognition',methods=['POST'])
def pii_recognition():
    content=request.get_json()
    data=content["text"]
    return pii_recognition_example(data)

#Azure
@app.route('/api/entity_linking',methods=['POST'])
def entity_linking():
    content=request.get_json()
    data=content["text"]
    return entity_linking_example(data)

#Azure
@app.route('/api/key_phrase_extraction',methods=['POST'])
def key_phrase_extraction():
    content=request.get_json()
    data=content["text"]
    return key_phrase_extraction_example(data)

#Entities- Google and Azure
@app.route('/api/entities',methods=['POST'])
def entities():
    content=request.get_json()
    data=content["text"]
    provider=content["provider"]
    
    if(provider=="Azure"):
        entity_recognition_example(data)
        return convert_microsoft_entity()
    else:
        analyze_entities(data)
        return convert_google_entity()

@app.route('/api/sentiment_analysis',methods=['POST'])
def sentiment_analysis():
    content=request.get_json()
    data=content["text"]      
    sentiment_analysis_example(data)
    analyze(data)
    return sentiment()

@app.route('/api/sentiment',methods=['POST'])
def sentiment_in():
    content=request.get_json()
    data=content["text"]
    provider=content["provider"]
    if(provider=="Azure"):
        return sentiment_analysis_example(data)
    else:
        return analyze(data)
        
    
   






