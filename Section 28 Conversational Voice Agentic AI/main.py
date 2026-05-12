import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
import wave
import pyaudio

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

# 1. Initialize the player once (The "Inbuilt" Speaker connection)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=24000, # Gemini TTS default rate
    output=True
)

#Client for S2T, because Gemini compatible with the OpenAI Chat Completions endpoint
client=OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#TTS_CLIENT is created here because Gemini's TTS is a native multimodal capability that requires the official google-genai SDK
tts_client = genai.Client(api_key=GEMINI_API_KEY)



def tts(speech_data):

    print("\nGenerating Voice........")

    response = tts_client.models.generate_content(
        model="gemini-3.1-flash-tts-preview",
        contents=f"Speak like a JARVIS from IronMan: {speech_data}",
        config=types.GenerateContentConfig(
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Charon' 
                    )
                )
            )
        )
    )
    audio_data = response.candidates[0].content.parts[0].inline_data.data
    
    print("JARVIS is speaking...")
    stream.write(audio_data)

def main():
    #recoginizer : speech to text
    r=sr.Recognizer()

    #Temp file audio because work is getting done on Codespace
    # audio_file = "output_file.wav"
    #Get access for users microphone as the source
    with sr.Microphone() as source:  # when on VS Code , use sr.Microphone()
        #ambient noise for noise cancellation
        r.adjust_for_ambient_noise(source)

        #When to start recognition, if user pauses for 2 secs , start the recognition
        r.pause_threshold=2

        SYSTEM_PROMPT="""
            You are an expert voice agent, you are given a transcript of what user has said using voice.
            You need to output as if you are a voice agent and whatever you speak will be converted back to audio using AI and play it back to user.Your voice should sound like JARVIS from Ironman
    """
        messages=[
                {"role":"system","content":SYSTEM_PROMPT},
        ]
        
        while True:
            print("Speak Something......")
            #Take audio from the source
            audio=r.listen(source)

            print("Process Audio.....")

            s2t=r.recognize_google(audio)
            print("\nYou said:\n",s2t)

            messages.append({"role":"user","content":s2t})

           
            print("\n Starting LLM...")
            response=client.chat.completions.create(
                model="gemini-3.1-flash-lite",
                messages=messages
            )

            print("\n🤖 >\n", response.choices[0].message.content)
            tts(response.choices[0].message.content)
        

main()