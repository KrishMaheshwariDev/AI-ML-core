1\. What a Vector is in ML and Why representation Matters



In ML vectors act as building blocks to represent data as arrays of numerical values. they convert text, images, or sensor data into numerical data which an algorithm can process



The representation of vectors enchance both the efficiency and accuracy of the algorithms for example, in a image if a color of a pixel is more than normal green then put it in array as 1 bit else 0 bit





2\. Dot product - geometric + numerical meaning



geometrically, dot product of 2 vectors is defined as the product of there magnitude and cosine of the angle between them. it also shows how much those 2 vectors are aligned



numerically, dot product is the sum of the products of the corresponding componenets of the two vectors



these 2 definations are equivalent when using cartesian coordinate system. and dot product determines the angles between vectors





3\. One edge case where dot product is misleading



in floating point calculations, dot product can have errors and those are dependent on the input magnitude of the vecotrs. further if the actual dot product is very small but computed result has a non zero error, the relative error becomes too large leading to bad interpretation of the relation between vectors





4\. How dot product connects to similarity in ML



dot products is used to calculate weighted sum of inputs in neural networks. output neuron is dependent on the input dot product followed by an activation function





A vector is not just an array of numbers. in ML a vector is a point in a high dimensional space, where each dimension represents a measurable attribute of the data

