### Topic analysis

I will implement simple topic analysis to estimate the public opinion about the Goettingen city in twitter using tweets about the city. I downloaded the all tweets (just 3.9K 😉) which is tweeted in last week and contained key word Goettingen through Twarc library. Below, I prepared overview of LDA, common topic analysis' technique. 


### Latent Drichilet Model
LDA is unsupervised topic modelling as well as one of the most common NLP techniques. It assumes each document as a random mixture of latent topics and clusters words
 into topics in an unsupervised way. Here, brief introduction of the model will be presented as following simple version, which is suggested by [Blei et al., 2003]. 
I will recommend he original paper for readers who interested in detailed methodology. LDA is the three evel hierarchical Bayesian model, which is shown the figure below.
![This is an image](https://github.com/ankhaa0813/Quasi-experiment/blob/main/Topic%20analysis/figure1.png)

In the figure 1, rectangles drawn with black lines indicate replicates. Outer rectangle epresents documents, while an inner rectangle represents choice of topics and words ithin a document. The model consists of corpus-level parameters, document, and word evel variables. α and β are the corpus level parameters. Document level variable, θ defines he distribution of topics for a document, which follows Dirichlet distribution with hyper arameter α. Wwhich is distributed Poisson distribution with hyperparameter of β which haracterizes the distribution of words for each topic. In particular, θ is a document level ariable while z and w are the word level variables, respectively.
Given the parameters α and β, a joint distribution of θ, w, and z is defined by

<img src="https://latex.codecogs.com/svg.image?\[p(\theta,z,w|\alpha,&space;\beta)&space;=&space;p(\theta|\alpha)&space;\prod_{n=1}^{N}p(z_n|\theta)p(w_n|z_n,&space;\beta)\]" title="https://latex.codecogs.com/svg.image?\[p(\theta,z,w|\alpha, \beta) = p(\theta|\alpha) \prod_{n=1}^{N}p(z_n|\theta)p(w_n|z_n, \beta)\]" />

The important note is that choice of distribution of words orWare open to researchers. ei et.(2003) showed the simple model in the first part of their job with Poisson distribution, hile Thorsurd assumed both repeated choice of topic z and words w are distributed
along with multinominal distribution. In principle, θ and w are estimated by maximum ikelihood method but it is computationally challenging. Therefore, Bei et al. used a ayesian method. Thorsurd used the method suggested by Griffiths and Steyvers (2004).

Intuition behind the topic model is explained well in [Bybee et al., 2021] work. Bybeer al. also used LDA topic model too to measure the state of the economy with business ews. They used Wall Street Journal and augmented the VAR model to investigate the ole of news text in formulating economic dynamics. News attention closely tracks the arious economic indicators.

Topic model, LDA, functions as a dimension reduction technique same as a principal omponent analysis(PCA). This is why sometimes it is called “generative” a model. It
reduces high dimensional textual data to relatively low dimensional topics, which consist f clusters of words. But the formations of clusters are unsupervised and defined to reserve as much of information as possible from the original corpus which is measured in variation in word usage across an article. The note is that it quantifies how much proportion of each document is dedicated to each topic. In other words, the amount of news attention allocated to each topic is defined at a document level.

### Reference

[Blei et al., 2003] Blei, D. M., Ng, A. Y., and Jordan, M. I. (2003). Latent dirichlet allocation. Journal of machine Learning research, 3(Jan):993–1022.
[Bybee et al., 2021] Bybee, L., Kelly, B. T., Manela, A., and Xiu, D. (2021). Business news and business cycles. Technical report.

