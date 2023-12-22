from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('Привет мир', 'Прив')
print(a)