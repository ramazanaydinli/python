
# Named Entity Recognition will be done here
# Created by Ramazan AYDINLI

import spacy
from spacy.matcher import Matcher

nlp=spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)

pattern_yield = [{"LOWER": "s"}, {"IS_DIGIT": True}]
pattern_ultimate = [{"LOWER": "fu"}, {"IS_DIGIT": True}]
pattern_dl = [{"LOWER": "pg"}, {"IS_DIGIT": True}]
pattern_ll = [{"LOWER": "pq"}, {"IS_DIGIT": True}]


matcher.add('Yield_Str', [pattern_yield])
matcher.add('Dead_Load', [pattern_dl])
matcher.add('Live_Load', [pattern_ll])
matcher.add('Ultimate_Str', [pattern_ultimate])
ocr_reading="link ocr reading results here!!!!"
doc = nlp(ocr_reading)

matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)

