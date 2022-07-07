### Difference in Difference 
I will show a simple example of how to implement DinD approach using Python programming language. DinD approach compares difference between control and treatment group and before and after the treatment. A key assumption of this approach is the parallel trend assumption. 

I will use example from Introductory econometrics by Jeffrey Wooldridge (2018) chapter 13 that focus on panel data and its method. Kiel and McClain (1995) estimated the impact of a new incinerator on price of nearby house in North Andover, Massachusetts U.S. The rumor about a new garbage incinerator began around city after 1978. Construction work started in 1981, and the incinerator began its operation in 1985. 

Treatment group is the houses located within 3 miles from the incinerator, while other or far houses are categorized as a control group. Pre and pro treatment date is defined as 1978 and 1981, respectively.

DinD approach and other panel data approaches are mainly doable with simple OLS analysis by adding interaction term, fixed effects, finding difference, or making demeaning. Detailed explanation of the code will be found from python file as comment.

If you are interested in example, I would advise you to read Chapter 13 of the same book, specifically pages 432- 434. Although, the Wooldridge, part 3 of the book,  is able to give you good understanding about methodology, Causal inference: The mixtape would be very good complementary. Particularly, provided Stata, R, and python code incorporated within latter book would be very helpful for programming skill as well as theoretical knowledge. 


## References

[1] 	J. M. Wooldridge, Introductory econometrics: A modern approach, Cengage learning, 2018. 

[2] 	[S. Cunningham, Causal Inference, Yale University Press, 2021.](https://mixtape.scunning.com/)

[3] 	K. A. a. M. K. T. Kiel, "House prices during siting decision stages: The case of an incinerator from rumor through operation," 
Journal of Environmental Economics and Management, vol. 2, no. 28, pp. 241--255, 1995. 
