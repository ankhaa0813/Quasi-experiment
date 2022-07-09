### Instrumental Variable 
Here,  I tried to show how to implement the Instrumental variable approach, specifically 2SLS, the approach using Python programming language.

The instrumental variable is a very common approach to identifying a causal relationship among economic variables when dealing with endogenous explanatory variable. 

Example from the  Introductory econometrics by Jeffrey Wooldridge (2018) chapter is used here for coding. Card (1995) estimated return to education using instrumental variable. For this case, education is the endogenous explanatory variable. Instrumental variable is whether someone grew up near a four year college. As following exclusion restriction, growing up in near a four year college can only affect return to education which is measured as salary through education. I am sure that you have some questions and counterarguments about methodology in this case I will recommend you to look for original paper that is included in the reference below, and the book.

Detailed explanations of the code will be found in the python file as comment.

If you are interested in example, I would advise you to read Chapter 15 of the same book, specifically page 507- 508. Although, Wooldridge, part 3 of the book,  is able to give you good understanding about methodology, Causal inference: The mixtape would be very good complementary. Particularly, provided Stata, R, and python code incorporated within last book would be very helpful for programming skills as well as theoretical knowledge. 



## References

[1] 	J. M. Wooldridge, Introductory econometrics: A modern approach, Cengage learning, 2018. 

[2] 	[S. Cunningham, Causal Inference, Yale University Press, 2021.](https://mixtape.scunning.com/)
[3] 	D. Card, "Using geographic variation in college proximity to estimate the return to schooling,
" National Bureau of Economic Research Cambridge, Mass., USA, 1993. 


