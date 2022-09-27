# FusionLayers

<p align="justify">
In this work, we address the problem of speech enhancement in the context of binaural hearing. We propose deep learning models which are connected by "fusion layers" that perform Hadamard products between specific generated latent representations. Fusion layers are inspired by multi-task learning approaches that combine and/or share weights between models that tackle related tasks. We first present a general fusion model and show that this approach is able to fit synthetic data better than independent linear models, equalize activation variance between learning modules, and exploit input data redundancy to improve the training error. We then apply the concept of fusion layers to enhance speech in binaural listening conditions. Our results show that the proposed approach improves speech enhancement performance on unseen data with respect to the independent models. However, we observe a trade-off between speech enhancement performance and predicted speech intelligibility based on a short-time objective binaural speech intelligibility index, potentially due to distortions introduced by fully fused models.
Results also suggest that fusion layers should share parameterized latent representations in order to properly exploit the information contained in each listening side. In general, this work shows that sharing information between speech enhancement modules may be promising to improve binaural speech enhancement while keeping the number of trainable parameters constant and improving generalization. 


# Requirements
See [Requirements.txt](requirements.txt)

# References
<p align="justify">
[1] Martín Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen, Craig Citro, Greg S. Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Ian Goodfellow, Andrew Harp, Geoffrey Irving, Michael Isard, Rafal Jozefowicz, Yangqing Jia, Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg, Dan Mané, Mike Schuster, Rajat Monga, Sherry Moore, Derek Murray, Chris Olah, Jonathon Shlens, Benoit Steiner, Ilya Sutskever, Kunal Talwar, Paul Tucker, Vincent Vanhoucke, Vijay Vasudevan, Fernanda Viégas, Oriol Vinyals, Pete Warden, Martin Wattenberg, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. TensorFlow: Large-scale machine learning on heterogeneous systems, 2015. Software available from tensorflow.org.

[2] Y. Luo and N. Mesgarani, “Conv-TasNet: Surpassing ideal time–frequency magnitude masking for speech separation,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 27, pp. 1256–1266, 2019.
