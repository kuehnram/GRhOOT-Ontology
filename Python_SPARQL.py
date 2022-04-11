__author__ = "Ramona Kuehn"
__license__ = "MIT"
__version__ = "1.0."
__email__ = "ramona.kuehn@uni-passau.de"

"""
This file shows exemplary how to use SPARQL queries in Python on the GRhOOT ontology,
the ontology for rhetorical figures in German.
Examples are the competency question
Q3: figures that are neither tropes not figures of speech
Q4: looking for rhetorical figures that have their defining element in a word.
Q5: looking for rhetorical figures where a letter is omitted.
"""

import rdflib

g = rdflib.Graph()
g.parse('grhoot.owl', format='application/rdf+xml')
ont = rdflib.Namespace('https://ramonakuehn.de/')
g.bind('ont', ont)


# only figure of speech and figure of thought with position beginning
competency_question_q3 = """
SELECT distinct ?figur
WHERE {
    ?figur ont:istRhetorischeGruppe ?gruppe .
    ?gruppe rdfs:label ?gruppenName .
    ?figur ont:istInPosition ?position .
    ?position rdfs:label ?posName .
    Filter (?gruppenName != "Tropenfigur" && ?gruppenName != "Konstruktionsfigur" && ?posName = "Anfang") }
"""

competency_question_q4 = """
SELECT distinct ?figur
WHERE {
    ?figur ont:liegtImBereich ?bereich .
    ?bereich rdfs:label ?nameBereich .
    Filter (?nameBereich = "Wort" ) }
"""

competency_question_q5 = """
SELECT distinct ?figur
WHERE {
    ?figur ont:wirdWeggelassen ?element .
    ?element rdfs:label ?name .
    Filter (?name = "Buchstabe" ) }
"""


print("Competency Question Q3: Neither a trope nor a figure of construction, but position at the beginning")
result = g.query(competency_question_q3)
print(f"Number of matching rhetorical figures: {len(result)}")
for row in result:
    print(row)

print("Competency Question Q4: In the area of a word")
result = g.query(competency_question_q4)
print(f"Number of matching rhetorical figures: {len(result)}")
for row in result:
    print(row)

print("\nCompetency Question Q5: Where a letter is omitted")
result = g.query(competency_question_q5)
print(f"Number of matching rhetorical figures: {len(result)}")
for row in result:
    print(row)

