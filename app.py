import flask
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
import cohere
from cohere.classify import Example
co = cohere.Client('yZ5jR7RtfXXepb8RwnRsSzxTLm0W0BeSgyIaDfQZ') # This is your trial API key

@app.route('/test')
@cross_origin()
def outputcode():
    response = co.classify(
    inputs=["I have a really bad cough, runny nose, abdominal pain, and feel tired"],
    examples=[Example("I have a cough, runny nose, and some on-and-off fever. And there are mucuses feeling in my throat, which blocks my sinus.","A Cold"), Example("I have a stuffy nose. My throat and sinus hurt sometimes and it makes me wanting to cough easily. ", "A Cold"), Example("I am feeling weak and some tingling senation on one side of my body. My vision got blurred. I am having trouble walking since I am so dizzy right now.", "Stroke"), Example("I am having trouble in speaking. My head is hurting so much. I cannot control my left / right part of my body. ", "Stroke"), Example("My abdomin hurts so much. I feel so dizzy and want to vomit.  I am always wanting to go to the toilette. I am having loose and watery stool. I  can barely walk and having dried lips. ", "Diarrhea"), Example("I vomited for 5 hours already. I feel so thirsty. I am having stomach ache and the pain persist for long already. I see some blood in my stool. ", "Diarrhea"), Example("My ear hurts and had yellow liquid leaking out of my ear. My ear is clogged. I am having minor headach.", "Ear Infection"), Example("I have difficulty in hearing for 2 days already. I feel pressure inside the ear preventing me from hearing. I am having on-and-off fever. ", "Ear Infection"), Example("I urinate a lot more often in recent months. Many of my wounds are not healing. I am getting really thirsty even though I drank lots of water already. My energy is not enough for me to still up for daily activities. But my body weight drops significatly without effort in the past two months. My vision has decreased.", "Diabetes"), Example("I loss lots of weigth without performing any moderate to vigorous physical activities. I urinate frequently and get extreme thirst. My vision is getting blurred. I am having some dark skin patches all over my body.", "Diabetes"), Example("My wounds and sores takes too long to heal ", "Diabetes"), Example("I feel more thirsty than usual", "Diabetes"), Example("loss of taste or smell", "COVID-19"), Example("Abdominal pain", "COVID-19"), Example("runny nose", "COVID-19"), Example("sore throat", "COVID-19"), Example("coughing", "COVID-19"), Example("I feel weak", "COVID-19"), Example("I have a fever", "COVID-19"), Example("I have itching sensation in my anal region.", "Hemorroid"), Example("I have bleeding during bowel movements ", "Hemorroid"), Example("My anus is swollen", "Hemorroid"), Example("I have trouble breathing ", "Allergies"), Example("I am getting raised rashes all over my body", "Allergies"), Example("I got swollen eyes, lips, mouth.", "Allergies"), Example("I keep sneezing but I do not have any mucus", "Allergies"), Example("Abdominal pain", "A Cold"), Example("Runny Nose", "A Cold"), Example("Headache", "A Cold"), ])
    return "According to our calculations, you seem to be suffering from" + response.classifications[0].prediction + ". Our system has detected a" + str(round((response.classifications[0].confidence*100),2))+ "% degree of accuracy. We recommend that you seek the appropriate aid for this ailment."