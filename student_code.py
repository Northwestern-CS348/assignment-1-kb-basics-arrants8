import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))


        if isinstance(fact, Fact):     
            if fact not in self.facts:  
                self.facts.append(fact)   

        
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
 
        """if fact isinstance Fact
            for loop with match function in the facts array
            (match returns bindings which is a class)
            add this returned binding(s) to list of bindings"""
        BindingList = ListOfBindings()

        
        if isinstance(fact, Fact):
                for element in self.facts:
                    binding = match(fact.statement, element.statement) #look for match in facts
                    if binding != 0: #if there is a match, add binding to bindinglist
                        BindingList.add_bindings(binding, element)

        if BindingList:
            return BindingList

        else:
            return False

         
                                
                        
            
            

        
        print("Asking {!r}".format(fact))
