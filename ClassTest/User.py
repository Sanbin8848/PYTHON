class User():
   '''定义用户类'''

   def __init__(self,first_name,last_name,user_description):
       self.first_name=first_name
       self.last_name=last_name
       self.user_description=user_description


   def describe_user(self):
        print(self.first_name.title()+' '+self.last_name.title()+':'+self.user_description)


   def greet_user(self):
        print(self.first_name.title()+' '+self.last_name+','+'You are welcome to our home!')


