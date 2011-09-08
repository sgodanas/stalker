#-*- coding: utf-8 -*-



import unittest
from stalker.core.models import Entity, Status






########################################################################
class StatusTest(unittest.TestCase):
    """tests the status class
    """
    
    
    
    #----------------------------------------------------------------------
    def setUp(self):
        """setup the test
        """
        
        self.kwargs = {
            "name": "Complete",
            "description": "use this when the object is complete",
            "code": "CMPLT",
            }
        
        # create an entity object with same kwargs for __eq__ and __ne__ tests
        # (it should return False for __eq__ and True for __ne__ for same
        # kwargs)
        self.entity1 = Entity(**self.kwargs)
    
    
    
    #----------------------------------------------------------------------
    def test_equality(self):
        """testing equality of two statuses
        """
        
        status1 = Status(**self.kwargs)
        status2 = Status(**self.kwargs)
        
        self.kwargs["name"] = "Work In Progress"
        self.kwargs["description"] = "use this when the object is still in \
        progress"
        self.kwargs["code"] = "WIP"
        
        status3 = Status(**self.kwargs)
        
        self.assertTrue(status1==status2)
        self.assertFalse(status1==status3)
        self.assertFalse(status1==self.entity1)
    
    
    
    #----------------------------------------------------------------------
    def test_status_and_string_equality_in_status_name(self):
        """testing a status can be compared with a string and returns True if
        the string matches the name and vice versa
        """
        
        a_status = Status(**self.kwargs)
        self.assertTrue(a_status==self.kwargs["name"])
        self.assertTrue(a_status==self.kwargs["name"].lower())
        self.assertTrue(a_status==self.kwargs["name"].upper())
        self.assertTrue(a_status==unicode(self.kwargs["name"]))
        self.assertTrue(a_status==unicode(self.kwargs["name"].lower()))
        self.assertTrue(a_status==unicode(self.kwargs["name"].upper()))
        self.assertFalse(a_status=="another name")
        self.assertFalse(a_status==u"another name")
    
    
    
    #----------------------------------------------------------------------
    def test_status_and_string_equality_in_status_code(self):
        """testing a status can be compared with a string and returns True if
        the string matches the code and vice versa
        """
        
        a_status = Status(**self.kwargs)
        self.assertTrue(a_status==self.kwargs["code"])
        self.assertTrue(a_status==self.kwargs["code"].lower())
        self.assertTrue(a_status==self.kwargs["code"].upper())
        self.assertTrue(a_status==unicode(self.kwargs["code"]))
        self.assertTrue(a_status==unicode(self.kwargs["code"].lower()))
        self.assertTrue(a_status==unicode(self.kwargs["code"].upper()))
    
    
    
    #----------------------------------------------------------------------
    def test_inequality(self):
        """testing inequality of two statuses
        """
        
        status1 = Status(**self.kwargs)
        status2 = Status(**self.kwargs)
        
        self.kwargs["name"] = "Work In Progress"
        self.kwargs["description"] = "use this when the object is still in \
        progress"
        self.kwargs["code"] = "WIP"
        
        status3 = Status(**self.kwargs)
        
        self.assertFalse(status1!=status2)
        self.assertTrue(status1!=status3)
        self.assertTrue(status1!=self.entity1)
    
    
    
    #----------------------------------------------------------------------
    def test_status_and_string_inequality_in_status_name(self):
        """testing a status can be compared with a string and returns False if
        the string matches the name and vice versa
        """
        
        a_status = Status(**self.kwargs)
        self.assertFalse(a_status!=self.kwargs["name"])
        self.assertFalse(a_status!=self.kwargs["name"].lower())
        self.assertFalse(a_status!=self.kwargs["name"].upper())
        self.assertFalse(a_status!=unicode(self.kwargs["name"]))
        self.assertFalse(a_status!=unicode(self.kwargs["name"].lower()))
        self.assertFalse(a_status!=unicode(self.kwargs["name"].upper()))
        self.assertTrue(a_status!="another name")
        self.assertTrue(a_status!=u"another name")
    
    
    
    #----------------------------------------------------------------------
    def test_status_and_string_inequality_in_status_code(self):
        """testing a status can be compared with a string and returns False if
        the string matches the code and vice versa
        """
        
        a_status = Status(**self.kwargs)
        self.assertFalse(a_status!=self.kwargs["code"])
        self.assertFalse(a_status!=self.kwargs["code"].lower())
        self.assertFalse(a_status!=self.kwargs["code"].upper())
        self.assertFalse(a_status!=unicode(self.kwargs["code"]))
        self.assertFalse(a_status!=unicode(self.kwargs["code"].lower()))
        self.assertFalse(a_status!=unicode(self.kwargs["code"].upper()))


