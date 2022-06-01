
# Since turkish language is not supported the obtained text will be translated here
# Created by Ramazan AYDINLI

from googletrans import Translator

sentence = "provide sentence which needed to be translated here"

translator = Translator()

result = translator.translate(sentence)

main_text = result.text

print(main_text)


