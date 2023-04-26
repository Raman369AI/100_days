def bid():
    person={}
    person["name"]=input('Enter your name\n')
    person["amount"]=input('Enter your amount\n')
    print(person)
    direction=input('Do you want to continue? yes, no\n').lower()
    if direction=='yes':
      clear()
      bid()
    else:
      clear()
      pass


bid()
for name in bid.person:
    n_name=name