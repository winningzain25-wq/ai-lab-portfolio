
# AI-101L Laboratory 4 Report
## Introduction to Scikit-learn and Traditional Machine Learning

### 1. California Housing — Linear Regression
The California Housing dataset was used to train a Linear Regression model.
The model was evaluated using the R-squared (R²) score.

### 2. Iris — Logistic Regression
The Iris dataset was used for classification with Logistic Regression.
The model achieved 1.00 accuracy on the test set, with all test samples
classified correctly.

### 3. Feature Scaling
A StandardScaler and Linear Regression pipeline was evaluated.
The R² score was approximately 0.576.

### 4. Model Persistence
The trained housing model was saved as `linear_model.pkl` and loaded
again to verify that the saved model could be reused.

### 5. Actual vs Predicted Plot
The graph was saved at `figures/actual_vs_predicted.png`.

### 6. Home Assignment — Article Sentiment Classification
The article dataset contained 20 articles. Sentiment polarity was divided
into two classes using the corpus median of approximately 0.17673.

Class 0: At or below median polarity.
Class 1: Above median polarity.

A Pipeline containing TfidfVectorizer and LogisticRegression was trained
using 16 articles and evaluated using 4 test articles.

Accuracy: 0.75

Confusion Matrix:
[[1, 1],
 [0, 2]]

The sentiment pipeline was saved as `sentiment_pipeline.pkl`.
It was reloaded and tested on raw article text without manual
text preprocessing.

### Conclusion
The lab demonstrated data loading, train-test splitting, regression,
classification, feature scaling, evaluation metrics, visualization,
pipelines, and model persistence using scikit-learn.

Note: The sentiment evaluation used only four test articles, so its
accuracy is a limited estimate of generalization performance.
