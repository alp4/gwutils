import PassArgs
#changes for the Forked gwutils project
import unittest
class Harness(unittest.TestCase):
   def testSanity(self):
       print "Harness.testToRoman before assert"
       self.assertEqual(1,1)
       print "Harness.testToRoman after assert"




##import pdb
#import types

if __name__ == "__main__":
#   unittest.main()
##  pdb.set_trace()
# strings,numbers,tuples are immutable(pass by value)
# dictionary.lists,userdefined objects are mutable(pass by reference)

# strings are pass by value
 # Z='hello world'
#Numbers are pass by value
 # Z=1
#tuples are pass by value
# if we pass  Z=("a","b","c")
# and inside function  Z=("g","h"),Z will not change
# dictionary are pass by reference
#  Z={"key1":"value1"}
 # lists are pass by reference
 # Z=["hi",2]
#  print Z
#  PassArgs.Pass(Z)
#  print Z
 
  #print dir(PassArgs)
 ## print PassArgs.__builtins__
 
   b1 = PassArgs.BaseClass(1,2)
   b2 = PassArgs.BaseClass(3,4)
   print "BaseClass.x="+str(b1.x)+"BaseClass.y"+str(b1.y)+"b1.t="+str(b1.t)
 
   print "BaseClass.x="+str(b2.x)+"BaseClass.y"+str(b2.y)+"b2.t="+str(b2.t)
 
    # 2/3 ways to create class data
   PassArgs.BaseClass.t=3  # modifies static reference var(modify class data)
    # 3/3 ways to create class data
   b1.__class__.t=25 # modifies static reference var (modify class data)
    #2/2 ways to create instance data:
   b2.t=4  # creates new instance data with same name "t" !!! (create instance data)
 
    # <instance>.t below will first look to see if there is
    # instance data called "t" and if not then will look for class data called "t"
   print "BaseClass.x="+str(b1.x)+"BaseClass.y"+str(b1.y)+"b1.t="+str(b1.t)
   print "BaseClass.x="+str(b2.x)+"BaseClass.y"+str(b2.y)+"b2.t="+str(b2.t)
    # <class>.t below will always show class data called "t"
   print "PassArgs.BaseClass.t="+str(PassArgs.BaseClass.t)
 
   #overloading [] operator
   b1["hi"]="there"
   print "b1[hi]="+str(b1["hi"])
   d = PassArgs.DerivedClass()
   d.showme()
  
   
   b1+b2
   print "BaseClass.x="+str(b1.x)+"BaseClass.y"+str(b1.y)+"b1.t="+str(b1.t)
 
   print "BaseClass.x="+str(b2.x)+"BaseClass.y"+str(b2.y)+"b2.t="+str(b2.t)
  
 
 
 
 
 
