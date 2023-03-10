# Transactional-Data-Analysis-with-Hadoop
Covering the basics of counting, and finding conditional probability on transactional data using Hadoop MapReduce using the STRIPES & PAIRS approaches

## a. Finding co-occurences of 2-items and calculating Prob(A|B) = Count(A,B)/Count(B).

### PAIR APPROACH
The co-occurrences of each pair of items, Count (A, B)= # of transactions contains both A and B, and the conditional probability Prob(B|A) = Count(A,B)/Count(A).

Mapper emits (key->value) as (A,B) -> 1
Reducer computes Conditional Probability Prob(B|A) = Count(A,B)/Count(A)
* Count (A,B) is calculated by the number of times it occurs in “sys.stdin” (output of the mapper) 

For each line item that is input to the reducer, we compute:
* Prob(B|A) = Count(A,B)/Count(A)
* Prob(A|B) = Count(A,B)/Count(B)

### STRIPES APPROACH

Mapper emits A -> {B: count(A,B), C: count(A,C),...}
Reducer calculates the total count and computes the conditional probabilities.

## b. Finding co-occurences of 2-items and calculating Prob(A|B,C) = Count(A,B,C)/Count(B,C)

The co-occurrences of each triple of items, Count (A,B,C) = # of transactions contains both A and B, and the conditional probability Prob(A|B,C) = Count(A,B,C)/Count(B,C)

Takes 2 input files:
● Transactions.txt to create combinations
● count2 .txt to get COUNT(A,B)
### PAIRS APPROACH
* Mapper emits (A,B,C) 1
* Reducer calculates Count(A,B,C) and computes the conditional probability
Prob(A|B,C) = Count(A,B,C)/Count(B,C)
### STRIPE APPROACH
* Mapper emits A: {(B,C): count, (C,D): count,..}
* Reducer calculates Count(A,B,C) and computes the conditional probability
Prob(A|B,C) = Count(A,B,C)/Count(B,C)
