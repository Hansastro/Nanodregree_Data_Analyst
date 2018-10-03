# Perceptual Phenomenon Project

## Introduction
The goal of this project is to study the [Stroop Effect][1]

## Question 1: Indentify variables in the experiment
The independent variable is the type of the words condition. Congruent or incongruent
The dependent variable is the time needed to read the test.

## Question 2a: Establish hypotheses
We can establish the null hypothesis as the fact that the congruent and incongruent type does not effect the time to read the test.

The hypothesis one is the time to read the congruent words condition is significantly less than the incongruent words condition.

## Question 2b: Establish statistical test
The two hyphotesis can be written in this form:

$H_0 : \mu_c = \mu_i$

$H_a : \mu_c \neq \mu_i$

With:

- $\mu_c$ the mean of the congruent words tests results
- $\mu_i$ the mean of the incongruent words tests results

We have here no information about the whole population. We compare two samples.
We will do a two tailed t-test with a confidence level of 95% ($\alpha = 0.05$).

## Question 3: Report descriptive statistic
From the dataset, we can extract some information about the data:

|				| Congruent				 | Incongruent	|
| --------- | :-----------------: | ----------: |
| Average	| 14.05					 | 22.02			|
| Standard Dev | 3.56				 | 4.80			|

## Question 4: Plot the data

![](./histograms.png)
\


## Question 5: Perform the statistical test and interpret the results

See the [t-table][2]

## Question 6: Extending the investigation

Mathematical and Words brain side

## Ressources
Those ressources were used to complete this project:

- [https://en.wikipedia.org/wiki/Stroop_effect][1] : Stroop Effect
- [https://s3.amazonaws.com/udacity-hosted-downloads/t-table.jpg][2] : t-table

[1]: https://en.wikipedia.org/wiki/Stroop_effect
[2]: https://s3.amazonaws.com/udacity-hosted-downloads/t-table.jpg