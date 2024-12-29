from deep_translator import GoogleTranslator
import os
import random


times=int(input('Enter the number of times you want to translate: '))

with open('original.txt','r') as file:
    temp=file.read()

languages = [
    "af", "sq", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca",
    "zh-CN", "zh-TW", "hr", "cs", "da", "nl", "en", "et", "fi", "fr",
    "gl", "ka", "de", "el", "gu", "he", "hi", "hu", "is", "id", "ga",
    "it", "ja", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv",
    "lt", "lb", "mk", "ms", "ml", "mt", "mr", "mn", "me", "ne", "no",
    "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr",
    "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv",
    "tg", "ta", "tt", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy",
    "yi", "yo", "zu"
]


for i in range(times):
    random.shuffle(languages)
    transltor=GoogleTranslator(source='auto', target=languages[0])
    temp=transltor.translate(temp)
    print(f"translated {i+1}")
    if i==times-1:
        temp=GoogleTranslator(source='auto', target='en').translate(temp)
        with open('resault.txt','w') as file:
            file.write(temp)
        print('Done')
        break