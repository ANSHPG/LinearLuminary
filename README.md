# LinearLuminary

![surfeace_plot](https://github.com/ANSHPG/LinearLuminary/assets/132222062/c02beb53-d02f-4b1e-9c6c-652f513349de)

Greetings! I've developed a straightforward linear regression model from scratch to predict house prices in Bangalore. But before delving into coding, let me walk you through the algorithm's conceptualization. I considered various factors such as location, ocean proximity, plot size, finished state, and flat type. To streamline the model's efficiency, I narrowed down the focus to a specific location from the database and exclusively worked on flat properties.

Now, transitioning from data engineering to model engineering, our first step is to visualize the data. We'll use scatter plots to observe the relationship between house prices and square footage. Our objective is to draw a straight line through the plot, minimizing the distance between predicted and actual prices, effectively reducing errors.

In mathematical terms, the equation of a straight line is typically represented as \( y = mx + c \), but in machine learning, we'll use \( y = wx + b \). Here, \( w \) and \( b \) are our parameters to be determined.

So, how do we find these parameters? We begin by defining our cost function:

![maths_2](https://github.com/ANSHPG/LinearLuminary/assets/132222062/b0e5d437-f5be-425c-881c-011ac1e22212)

\[ J = \frac{1}{2m} \sum_{i=1}^{m} (wx^{(i)} + b - y^{(i)})^2 \]

where \( m \) is the number of training data points. Our goal is to minimize \( J \) by adjusting \( w \) and \( b \). We achieve this through gradient descent, where we iteratively update \( w \) and \( b \) using the following equations:

\[ w = w - \alpha \frac{\partial J}{\partial w} \]
\[ b = b - \alpha \frac{\partial J}{\partial b} \]

Here, \( \alpha \) controls the convergence speed, and we loop through the process multiple times to converge to the most accurate \( w \) and \( b \) values.

After these iterations, we obtain our optimized parameters \( w \) and \( b \). We can then encapsulate them in a function to predict prices based on input square footage and compare them with actual prices.

![trained](https://github.com/ANSHPG/LinearLuminary/assets/132222062/d102d498-d909-4ec2-96f2-764801667a82) ![tested](https://github.com/ANSHPG/LinearLuminary/assets/132222062/d7d0062e-f2a0-43d0-b5df-7c9bc06b3da6)


In the coding phase, we'll utilize libraries such as Pandas, NumPy, and Matplotlib. NumPy facilitates algorithm creation, while Matplotlib aids in visualizing data. Leveraging Python ensures accuracy and scalability, particularly beneficial for large datasets. By following these mathematical steps and translating formulas into corresponding code, we can efficiently work towards accurate predictions.

![cost-iteration](https://github.com/ANSHPG/LinearLuminary/assets/132222062/61bad129-82cb-4219-a61f-113299393abc)

This repository is freely accessible for public use and is curated by Anshuman Pattnaik. Happy coding! 😊

