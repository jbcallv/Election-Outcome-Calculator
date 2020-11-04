""" calculates who will win the election in a state at input 
percentage (percent input must be decimal). Here's how it works:
we consider the amount of votes that are left to count
and calculate the outcome of the election if a candidate x 
receives a certain percent of those remaining votes (70, 80, or 90)"""

percent = float(input("Please enter the percentage (70, 80, or 90) of remaining votes to give to a candidate: "))
percentDone = float(input("Please enter the percent of votes that have been counted: "))
candidateName = input("Please enter the candidate name: ")
print("Calculating percent that has not been counted.")
print()

percentLeft = float(1-percentDone)
print("Percent left: " + str(percentLeft))
print()

percentVotes = float(input("Please enter the percent of votes a candidate has received: "))
print("Percent of votes: " + str(percentVotes))
print()

percentToAdd = percent * percentLeft
print("Percent to add: " + str(percentToAdd))
print()

resultCandidate = percentToAdd + percentVotes

print(candidateName + " will have: " + str(resultCandidate) + " votes if they get " + str(percent) + " of remaining votes.")

if (resultCandidate > 0.5):
    print(candidateName + " wins this state.")

