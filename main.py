#this is main file. program starts here on. u can directly run from here
print('Welcome to Food Ordering app')
print('****************************')
print('Enter 0 to access as ADMIN')
print('Enter any key to access as USER')
user_input0=input('Enter here : ')
if user_input0=='0':
    import admin
else:
    import user
