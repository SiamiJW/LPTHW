#string that uses a formatter to replace the number 10
x = "there are %d types of people." % 10
# variabkle set to a string of a single word
binary = "binary"
#same as above
do_not = "don't"
#replacement w/ aforementioned variables in conjunction with a formatter 
y = "Those who know %s and those who %s." % (binary, do_not)
#printing those things
print x
print y

print"I said: %r." % x
print "I also said: '%s'." % y
#set to false until used with a formatter
hilarious = False
#%r spits out the raw form 
joke_evaluation = "Isn't that joke so funny?! %r"

#variable stands for a string - still uses formatter to replace
print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a right side."

print w + e
