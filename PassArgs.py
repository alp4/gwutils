import types

def Print():
   print "PassArgs.Print()"

def Pass(Z):
   #dictionary: no duplicate keys,no order,keys/values mixed datatype
   #dictionary ADD  dict[non existent key]=value
   #Z[32]="hot"
   #Z["hot"]=32
   # dictionary MODIFY dict[existing key]=value
   # Z["key1"]="a"
 
   # dictionary DELETE  del dict[existing key] or dict.clear()
   # Z.clear()
   # del Z["key1"]

   #special dictionary operators
   # dict.keys() return list of keys,dict.values() returns list of values
   # dict.items() returns list of tuples where each tuple is key and value

   # lists allow duplicates,ordered,mixed datatypes
   # list ADD   list.append(item),list.insert(int,item).list.extend(list)
   #li2=[45,56]
   #Z.append("goodbye")
   #Z.insert(2,"insert")
   #Z.extend(li2)
   #list MODIFY:  list[existing index]=value
   Z[0]=1
 
# list DELETE  list.remove(first occurence of val) or list.pop()
   #Z.remove("insert")
   #Z.pop()

   #special list operators:
   # list slicing:  li[first index to include:last index not to include]
   #  li[-1]= li[len(li)-1]...
   # length: len(li) you can also take len(string)
   # index of first occurrence: li.index(item)
   # boolean condition if item in list: item in li
   # concatenating list: li=li1+li2 or li+=li2
   #  repeating list:  li=li2 * int
   # list mapping: [map-expression=fcn(element-list) for element-list in list if filter-expression]
   # <delimiter-string-constant>.join(list of strings) will
   # return a single string result of joining each element using delimiter <string-constant>
   # <string>.split(<delimiter-string-constant>) returns a list of strings

   #tuple t:  allow duplicates,ordered,mixed data
   # only operations: t[int],t[int:int],item in t, tuple used as key in dictionary, string formatting
   # to convert: t=tuple(li) or li=list(t)
   ##  print dir(types)
 ##  if(type(Z)== types.StringType):
   print "PassArgs.Pass()=" + str(Z)
class BaseClass():
  #1/3 ways to create class data:
  t=2 # static data member
  #overloading [] operator
  def __setitem__(self, key, item): self.data[key] = item
  def __getitem__(self, key): return self.data[key]
  def __add__(self,other):
    self.x=other.x+self.x
    self.y=other.y+self.y
  def __init__(self,a,b ):
    #1/2 ways to create instance data
    self.x=a  #instance data members
    self.y=b
    self.data={1:2,"hello":"mary"}
    self.basestr="hello"
    print "BaseClass constructor"
  def publicHelper(self):
    print "publicHelper"
   
  def showme(self):
    print "BaseClass.print"
 
class DerivedClass(BaseClass):
  def showme(self):
    BaseClass.showme(self)
    print "DerivedClass.print"
    print self.data
 
  ## this is a PRIVATE method 
  def __privateHelper(self):
    print "privateHelper()"
  def __init__(self):
    BaseClass.__init__(self,1,1)
    # the below uses the operator[] overloading in __setitem__
    self["der"]="der"
    # this is a PRIVATE data member:
    self.__derivedstr="world"
    print "DerivedClass constructor"
    self.__privateHelper()
    self.publicHelper()
    print "base class data and derived class data="+self.basestr+self.__derivedstr



