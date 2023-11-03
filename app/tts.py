#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Speech synthesis samples for the Microsoft Cognitive Services Speech SDK
"""

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-text-to-speech-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)


# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "westus").
# Set up the subscription info for the Speech Service:
key11 = "3d9f3eab783e4e979181e13cf3078bd3"
key1 = "17c13d7933294b8888c2a5eb7db14926"
key2 = "42dc205fa66d47d3a6a09328603059a9"

resgion1 = "norwayeast"
resgion = "southafricanorth"
# speech_key, service_region = "7e951d4b4398403c8ca9341c4f032f88", "japaneast"
speech_key, service_region = "17c13d7933294b8888c2a5eb7db14926", "southafricanorth"
male_voice = "so-SO-MuuseNeural"
female_voice = "so-SO-UbaxNeural"

class SpeakMyWords:
    male_voice = "so-SO-MuuseNeural"
    female_voice = "so-SO-UbaxNeural"
    def __init__(self, subscription=speech_key, region=service_region):
        self.voice_female = False
        self.voice_male = False
        self.subscription = subscription
        self.region = region

    def cong_words(self, cong_words, voice_male=False, voice_female=False) -> None:
        self.voice_male = voice_male
        self.voice_female = voice_female
        """performs speech synthesis to the default speaker"""
        # Creates an instance of a speech config with specified subscription key and service region.
        speech_config = speechsdk.SpeechConfig(subscription=self.subscription, region=self.region)
        # Creates a speech synthesizer using the default speaker as audio output.
        # The default spoken language is "en-us".
        # The language of the voice that speaks.

        if voice_male:
            speech_config.speech_synthesis_voice_name = male_voice
        else:
            speech_config.speech_synthesis_voice_name = female_voice
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        # Receives a text from console input and synthesizes it to speaker.
        text = cong_words
        result = speech_synthesizer.speak_text_async(text).get()
        # Check result
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized to speaker for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

    def speech_synthesis_to_speaker(self, text) -> None:
        """performs speech synthesis to the default speaker"""
        # Creates an instance of a speech config with specified subscription key and service region.
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        # Creates a speech synthesizer using the default speaker as audio output.
        # The default spoken language is "en-us".
        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name='so-SO-UbaxNeural'
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        # Receives a text from console input and synthesizes it to speaker.
        text = text
        result = speech_synthesizer.speak_text_async(text).get()
        # Check result
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized to speaker for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

    def say(self, sentence, voice) -> None:

        """performs speech synthesis to the default speaker"""
        # Creates an instance of a speech config with specified subscription key and service region.
        speech_config = speechsdk.SpeechConfig(subscription=self.subscription, region=self.region)
        # Creates a speech synthesizer using the default speaker as audio output.
        # The default spoken language is "en-us".
        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name = voice
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        # Receives a text from console input and synthesizes it to speaker.
        text = sentence
        result = speech_synthesizer.speak_text_async(text).get()
        # Check result
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized to speaker for text [{}]".format(text))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

if __name__ == '__main__':
    speak = SpeakMyWords()
    print("Fadlan sug...")
    # speak.speech_synthesis_to_speaker("Sidee baad tahay?")
    speak.cong_words("Muumin saaxiib wax haka baqin waxaas dhan waan isla hagaajinaynaa haddii Eebbe yiraahdo ee adigan lle cayow imoow saaxiib..",
                     voice_female=False)
