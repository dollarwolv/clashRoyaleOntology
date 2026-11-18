from owlready2 import sync_reasoner
from base import onto
import data

with onto:
    sync_reasoner()

onto.save(file="clash.owl", format="rdfxml")
