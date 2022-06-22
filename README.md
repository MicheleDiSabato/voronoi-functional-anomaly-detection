### This repository has been developed by:
* [Federica Botta](https://www.linkedin.com/in/federica-botta-8629391b3/)
* [Simone Colombara](https://www.linkedin.com/in/simone-colombara-a4a430167/)
* [Michele Di Sabato](https://www.linkedin.com/in/michele-di-sabato/)

# voronoi-functional-anomaly-detection

# Theoretical framework:

![sample](readme_images/sample.png)

# Exploratory data analysis:

# Assumptions:
We don't know what makes a point an anomaly, hence we followed two trains of thought:

1. Anomalies are grouped together (e.g. anomalies are due to measurament errors).
2. Anomalis are isolated points (e.g. anomalies are due to  the presence of scar tissue).

Clearly, methods which are coherent with assumtpion 1 will not be well suited with assumtpion 2. For esample, an algoithm which is methodologically similar to k-NN will of course be coherent with assumption 2: if anomalies were grouped together, then it would be impossible to classify a signal as such, just by looking at its neighbors (which will be almost surely anomalies).

# Voronoi tessellation:
We used [Voronoi tessellation](https://en.wikipedia.org/wiki/Voronoi_diagram) as a way of taking into account spatial correlation among signals.

**Def:** a Voronoi tessellation is a collection of non overlapping patches which describe the geometry of the heart. We select **n** nuclei (i.e. randomly sampled points), the remaining points are assigned to the closest nucleus in a process which resembles the assigning of a point to one of the centroids in the k-means algorithm. 

Since the choice of the **n** nuclei is random, whenever a Voronoi tessellation is involved we need to proceed in a bootstrap-like manner. 

**Remark on shifting:** whenever the temporal difference among signals odes not need to be taken into account, we used the algined signals (see [`alignment.py`](alignment.py)). For example:

| original signal | aligned signal
:----------:|:--------:
![](readme_images/peak_right.png) | ![](readme_images/peak_right_align.png)
![](readme_images/peak_left.png) | ![](readme_images/peak_left_align.png)

# Methods:

## :one: Voronoi - FPCA (with aligned signals)
Based on [this](https://www.sciencedirect.com/science/article/pii/S0303243412000505) paper.

![](readme_images/b_step.PNG)

![](readme_images/a_step.PNG)

## :two: Voronoi - dimesionality reduction algorithm (with original signals)
Additions with repect to :one::
1. don't work directly on signals, but on some statistics of the dataset based on our [Exploratory Data Analysis](README.md#exploratory-data-analysis);
2. less robust, hence more specific (with :one: we are saying that, for example, if the representative of 100 signals in a specific patch is clustered as anomaly, all those 100 points will be classifed as anomalies as well);
3. don't use FPCA and k-means (which might be a bottleneck);

![](readme_images/mdr.PNG)

## :three: Voronoi - dictionary learning algorithm (with original signals)
Based on [this](https://ieeexplore.ieee.org/document/7790862) paper. This algorithm has been designed for anomaly detection in *images*, but can be straightforwardly generalized to vectors, thanks to the fact that one step of the algorithm is to unroll some pathces of the image, thus obtaining vectors. **In our case, a vector is not obtained unrolling an image, but it componsed of the values of a signal in different time stamps: i.e. the i-th component of the vector is the evaluation of a specific signal in the i-th time stamp.** 

The dataset used to train the dictionary needs to be composed of only normal points: hence this algorithm works under the assumption of isolated anomalies. Indeed, a point is an anomaly if:
1. the coeficients which represent its "projection" onto the dictionary are not as sparse as the ones of the training set (which is composed by normal points only);
2. the dictionary representation of that point using the learned dictionary and weights is far away (in terms of L2 distance) from the true value of the point;

![](readme_images/dl.PNG)

## :four: Voronoi - weighted H<sup>1</sup> distance (with aligned signals)
The underlying idea for this algorithm was taken from graph teory, in particular regarding the centrality measure.

The weighted $H^1$ norm used in the algorithm is: 
$$dist(f_1, f_2) = \|\|f_1 - f_2\|\|^2_{L^2} + \theta \|\|\partial_t f_1 - \partial_t f_2\|\|^2_{L^2}$$

Note that now the nuclei coincide with the representatives.

![](readme_images/H1.PNG)


# Numerical reults, advantages and disadvantages:





