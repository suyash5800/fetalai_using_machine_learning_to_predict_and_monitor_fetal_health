<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>FetalAI: Using Machine Learning to Predict and Monitor Fetal Health</h1>

<p><strong>FetalAI</strong> is a machine learning-based solution designed to predict and monitor fetal health using Cardiotocogram (CTG) data. This project aims to assist healthcare professionals by automating the classification of fetal health status, helping in the early detection of risks and promoting timely intervention, particularly in low-resource settings.</p>

<h2>Table of Contents</h2>
<ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#project-architecture">Project Architecture</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#model-evaluation">Model Evaluation</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#advantages--disadvantages">Advantages & Disadvantages</a></li>
    <li><a href="#future-scope">Future Scope</a></li>
    <li><a href="#license">License</a></li>
</ol>

<h2 id="introduction">Introduction</h2>
<p><strong>FetalAI</strong> leverages machine learning to analyze CTG data and predict fetal health status in real-time. The solution classifies the health status into three categories:</p>
<ul>
    <li><strong>Normal</strong></li>
    <li><strong>Pathological</strong></li>
    <li><strong>Suspect</strong></li>
</ul>
<p>This system assists healthcare workers by providing quick, automated assessments, crucial for preventing child and maternal mortality.</p>

<h2 id="project-overview">Project Overview</h2>
<p>Cardiotocograms (CTGs) provide valuable data about fetal health, including fetal heart rate (FHR), fetal movements, and uterine contractions. Traditional methods of interpreting CTG data can be subjective and prone to error, making automated tools highly beneficial.</p>
<p>This project aims to:</p>
<ul>
    <li>Improve fetal health monitoring accuracy using machine learning.</li>
    <li>Provide an automated, cost-effective solution for low-resource settings.</li>
    <li>Facilitate early diagnosis, reducing maternal and child mortality.</li>
</ul>

<h2 id="dataset">Dataset</h2>
<p>The dataset used in this project consists of CTG data, which contains fetal heart rate, uterine contraction, and other related features. The dataset has been preprocessed to remove missing values, outliers, and to balance the class distribution using <strong>SMOTE</strong>.</p>
<p><strong>Classes:</strong></p>
<ul>
    <li><strong>Normal</strong></li>
    <li><strong>Pathological</strong></li>
    <li><strong>Suspect</strong></li>
</ul>

<h2 id="features">Features</h2>
<h3>1. <strong>Handling Missing Values</strong></h3>
<p>No missing values were found in the dataset.</p>

<h3>2. <strong>Handling Imbalanced Data</strong></h3>
<p>We applied <strong>SMOTE</strong> (Synthetic Minority Over-sampling Technique) to balance the class distribution in the dataset.</p>

<h3>3. <strong>Exploratory Data Analysis (EDA)</strong></h3>
<p>We conducted univariate, bivariate, and multivariate analysis to understand the data structure and relationships between features.</p>

<h3>4. <strong>Feature Selection and Scaling</strong></h3>
<p>Selected relevant features and scaled them to improve model performance.</p>

<h3>5. <strong>Model Building and Evaluation</strong></h3>
<p>We built and evaluated several machine learning models:</p>
<ul>
    <li><strong>Random Forest</strong></li>
    <li><strong>Decision Tree</strong></li>
    <li><strong>K-Nearest Neighbors</strong></li>
    <li><strong>Logistic Regression</strong></li>
</ul>
<p>The <strong>Random Forest Classifier</strong> achieved the highest accuracy, with a precision of 0.9435.</p>

<h2 id="project-architecture">Project Architecture</h2>
<p>The system follows this flow:</p>
<ol>
    <li><strong>Data Collection</strong>: CTG data is collected from monitoring devices.</li>
    <li><strong>Data Preprocessing</strong>: Includes cleaning, normalizing, and handling missing values.</li>
    <li><strong>Model Prediction</strong>: The processed data is fed into a machine learning model to predict the fetal health status.</li>
    <li><strong>Output</strong>: The model’s classification result is displayed on the healthcare professional's interface for decision-making.</li>
</ol>

<h2 id="installation">Installation</h2>
<h3><strong>Prerequisites</strong></h3>
<ul>
    <li>Python 3.7 or higher</li>
    <li>TensorFlow</li>
    <li>Scikit-learn</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
</ul>

<h3><strong>Steps</strong></h3>
<ol>
    <li>Clone the repository:
    <pre><code>git clone https://github.com/dhirajrhatwal8788-cell/fetalai-using-machine-learning-to-predict-and-monitor-fetal-health.git</code></pre></li>
    <li>Navigate to the project directory:
    <pre><code>cd FetalAI-USING-MACHINE-LEARNING-TO-PREDICT-AND-MONITOR-FETAL-HEALTH</code></pre></li>
    <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre></li>
</ol>

<h2 id="usage">Usage</h2>
<ol>
    <li>Preprocess the data using the <code>preprocess.py</code> script.</li>
    <li>Train the model using the <code>train_model.py</code> script.</li>
    <li>Evaluate the model using <code>evaluate_model.py</code>.</li>
    <li>To use the GUI for predictions:
    <pre><code>python app.py</code></pre></li>
</ol>

<h2 id="model-evaluation">Model Evaluation</h2>
<p>We evaluated various models to find the best-performing one:</p>
<ul>
    <li><strong>Random Forest</strong>: Accuracy = 0.9435</li>
    <li><strong>Decision Tree</strong>: Accuracy = 0.9310</li>
    <li><strong>K-Nearest Neighbors</strong>: Accuracy = 0.9075</li>
    <li><strong>Logistic Regression</strong>: Accuracy = 0.8119</li>
</ul>

<h2 id="screenshots">Screenshots</h2>
<p><strong>Home Page</strong></p>
<img src="\4. Project Development Phase\images\homepage.png" alt="Home Page" width="500">

<p><strong>Prediction Page</strong></p>
<img src="\4. Project Development Phase\images\analyse.png" alt="Analyse" width="500">

<h2 id="advantages--disadvantages">Advantages & Disadvantages</h2>
<h3><strong>Advantages</strong></h3>
<ul>
    <li>High accuracy in predicting fetal health.</li>
    <li>Cost-effective and scalable for low-resource settings.</li>
    <li>Automated classification reduces manual errors.</li>
</ul>

<h3><strong>Disadvantages</strong></h3>
<ul>
    <li>Requires a large and diverse dataset for optimal performance.</li>
    <li>The model’s decisions still need to be validated by healthcare professionals in critical cases.</li>
</ul>

<h2 id="future-scope">Future Scope</h2>
<ul>
    <li>Integration with real-time healthcare systems.</li>
    <li>Expanding the dataset to improve accuracy and robustness.</li>
    <li>Incorporating additional prenatal features like maternal health data for enhanced predictions.</li>
</ul>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
