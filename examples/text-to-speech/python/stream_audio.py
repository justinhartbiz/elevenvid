from elevenlabs.client import ElevenLabs
from elevenlabs import stream, PronunciationDictionaryVersionLocator
from dotenv import load_dotenv

import os

def main():
    API_KEY = os.getenv("ELEVEN_API_KEY")

    if API_KEY is None:
        print("Missing API KEY")
        return
    
    DICTIONARY_ID = "<replace with result from create_dictionary.py>"
    DICTIONARY_VERSION_ID = "<replace with result from create_dictionary.py>"
    
    client = ElevenLabs(
        api_key=API_KEY
    )

    # stream
    audio_stream = client.generate(
        text="Siobhan. Aoife.",
        voice="Rachel",
        model="eleven_turbo_v2",
        stream=True,
        pronunciation_dictionary_locators=[
            PronunciationDictionaryVersionLocator(
                pronunciation_dictionary_id=DICTIONARY_ID,
                version_id=DICTIONARY_VERSION_ID,
            )
        ],
    )

    stream(audio_stream)

if __name__ == "__main__":

    load_dotenv()
    main()