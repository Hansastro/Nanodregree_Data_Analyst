﻿# Perceptual Phenomenon Project

## Introduction
The goal of this project is to study the [Stroop Effect][1].

This effect is the effect of the disturbance of some cognitive mechanisms. The subject has to read some words written in some colors. It is composed by two test. In a test the words are the name of the colors written in another color and in the other test the words are generic and are written in the same color palette as the first test.

The goal of the study is to determine the effect on the response time, depending of the type of the test.

## Question 1: Identify variables in the experiment
The **independent** variable is the **type of the words condition**. Congruent or incongruent.

The **dependent** variable is the **time** needed to read the test.

## Question 2a: Establish hypotheses

We can establish the null hypothesis as the fact that the congruent and incongruent type does not affect the population mean time needed to perform the test.

The alternative hypothesis is: the population mean time to read the congruent words condition is significantly different than population mean time to read the words for the incongruent words condition.

## Question 2b: Establish statistical test
The two hypotheses can be written in this form:

$H_0 : \mu_c = \mu_i$

$H_a : \mu_c \neq \mu_i$

With:

- $\mu_c$ the population mean time of the congruent words tests.
- $\mu_i$ the population mean time of the incongruent words tests.

We have here no information about the whole population. We compare two samples. We also cannot presuppose in which direction the difference will be.

The two samples are done with the same population and test the same dependent variable (the time) with two variations of a test (Congruent and Incongruent words).

We will do a two-tailed dependent paired sample t-test with a confidence level of 95% ($\alpha = 0.05$).

## Question 3: Report descriptive statistic
From the data-set, we can extract some information about the data:

|				| Congruent				 | Incongruent	|
| --------- | :-----------------: | ----------: |
| Average	| 14.05					 | 22.02			|
| Standard Dev | 3.56				 | 4.80			|
| Count	  	| 24 						 | 24				|

## Question 4: Plot the data

![](./histograms.png)
\

With this plot we can see a difference between the congrurent and incongruent words condition. On the sample we have the subjects took more time to complete the Incongruent words condition.

## Question 5: Perform the statistical test and interpret the results

With an $\alpha$ of 0.05 and a degree of freedom of 23, the $t_{critical}$ limits are -2.069 and 2.069 (See the [t-table][2]). 

To test the $H_0$ hypothesis we have to use the difference between the two samples:

This can be written in this form:

$\overline{X}_c - \overline{X}_i = 0$

The difference of the two average values is:

$\overline{X}_D = \overline{X}_c - \overline{X}_i =  14.05 - 22.02 = -7.97$

The sample standard deviation of the difference is equal to:

$S_D = \sqrt{\frac{(\sum_{a=0}^{n}(x_{c(a)} - x_{i(a)}) - \overline{X}_D)^2}{n - 1}}$

$S_D = 4.865$

We can now calculate the t-statistic:

$t_{statistical} = \frac{(\overline{X}_D - 0)}{S_D / \sqrt{n}} = \frac{(-7.965 - 0)}{4.865 / \sqrt{24}} = -8.021$

$t_{statistical} < t_{critical}$'s lower limit

We can **reject** the null hypothesis.

The time to read the congruent words condition is significantly different than the incongruent words condition.
 
It is really something we could expect. The Incongruent words condition disturb the cognitive mechanism of the brain. 

## Question 6: Extending the investigation

This experience collides two cognitive processes of the brain. This makes the whole process unsure of the answer because the each answer contradicts the other.

In the brain mechanisms are not completely linked together. It is easy to disturb the normal way of working. A lobe of the brain manage better the number and the other the knowledge. It can be interesting to see if there is a difference of the answering time of a subject depending of which ear hears a question and what is the difference between simple calculus and some general knowledge questions.

## Resources
Those resources were used to complete this project:

- [https://en.wikipedia.org/wiki/Stroop_effect][1] : Stroop Effect
- [https://s3.amazonaws.com/udacity-hosted-downloads/t-table.jpg][2] : t-table
- [https://statistics.laerd.com/statistical-guides/dependent-t-test-statistical-guide.php][3] : Description of the paired t-test

[1]: https://en.wikipedia.org/wiki/Stroop_effect
[2]: https://s3.amazonaws.com/udacity-hosted-downloads/t-table.jpg
[3]: https://statistics.laerd.com/statistical-guides/dependent-t-test-statistical-guide.php
