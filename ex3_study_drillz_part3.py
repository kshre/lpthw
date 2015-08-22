''' 
Multiline commenting hasn't been introduced yet but meh;

Okay so in here we solve a conditional probability problem:
	You want to get tested for a rare disease.

	Prevalence of the disease is one person out of every ten thousand.
	The test for detecting this disease is accurate 99% of the time.

	Find the probability that you have the disease given that the test results come out positive.

'''

# Modeling of the problem:
#	P(D) := Probability of having the disease
#	P(D) = 1 / 10000
P_D = 1.0/10000.0
print "----------------------------------------------------------------------"
print "----------------------------------------------------------------------"
print "Probability of having the disease"
print "P(D) =", P_D
print

#	P(ND) := Probability of NOT having the disease
#	P(ND) = 1 - P(D) = 9999 / 10000
P_ND = 1.0 - P_D
print "Probability of NOT having the disease"
print "P(ND) =", P_ND
print "----------------------------------------------------------------------"

#	P(P|D) := Probability of testing POSTIVE given the subject HAS disease
P_PgD = 99.0 / 100.0
print "Probability of testing POSTIVE given the subject HAS disease"
print "P(P|D) =", P_PgD
print	

#	P(P|ND) := Probability of testing POSTIVE given the subject DOES NOT have disease
P_PgND = 1.0 / 100.0
print "Probability of testing POSTIVE given the subject DOES NOT have disease" 
print "P(P|ND) =", P_PgND
print "----------------------------------------------------------------------"
	
#	P(P) := Probability of positive test result
#	P(P) = P(P|D) * P(D) + P(P|ND) * P(ND)
P_P = P_PgD * P_D + P_PgND * P_ND
print "Cumulative probability of testing positive"
print "P(P) =", P_P
print "----------------------------------------------------------------------"

#	Applying Baye's Theorem:
#	Probability of HAVING disease given POSITIVE test result:
#	P(D|P) = P(P|D) * P(D) / P(P)
P_DgP = P_PgD * P_D / P_P
print "Applying Baye's Theorem"
print "Probability that the subject HAS disease given POSITIVE test result:"
print "P(D|P) =", round(P_DgP, 5) * 100 , "%"
print "       ~", round(P_DgP, 2) * 100 , "% (WHAT?? HOLY MOLEY!@)"
print "----------------------------------------------------------------------"





