__author__ = "Ramona Kuehn"
__license__ = "MIT"
__version__ = "1.0."
__email__ = "ramona.kuehn@uni-passau.de"

"""
This file shows exemplary how to use SPARQL queries on the GRhOOT ontology,
the ontology for rhetorical figures in German.
Examples are the competency question
Q3: looking for rhetorical figures that have their defining element in a word.
Q4: looking for rhetorical figures where a letter is omitted.
"""

import rdflib

g = rdflib.Graph()
g.parse('GRhOOT_Ontology.owl', format='application/rdf+xml')
ont = rdflib.Namespace('http://webprotege.stanford.edu/')
g.bind('ont', ont)

competency_question_q3 = """
SELECT distinct ?figur
WHERE {
    ?figur ont:liegtImBereich ?bereich .
    ?bereich ont:Name ?nameBereich .
    Filter (?nameBereich = "Wort" ) }
"""

competency_question_q4 = """
SELECT distinct ?figur
WHERE {
    ?figur ont:wirdWeggelassen ?element .
    ?element ont:Name ?name .
    Filter (?name = "Buchstabe" ) }
"""

print("Competency Question Q3:")
result = g.query(competency_question_q3)
print(f"Number of matching rhetorical figures: {len(result)}")
for row in result:
    print(row)

print("\nCompetency Question Q4:")
result = g.query(competency_question_q4)
print(f"Number of matching rhetorical figures: {len(result)}")
for row in result:
    print(row)
