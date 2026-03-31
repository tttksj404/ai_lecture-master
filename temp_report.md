

## 스크린샷 2026-03-24 094959.png
- **Visual Content**: Two presentation slides stacked vertically.
- **Main Text**:
  - Slide 1: Answer and explanation for Quiz Question 3 (from previous image). Answer is 2 (Learning cannot eliminate measurement errors).
  - Slide 2: "강의 정리" (Lecture Summary) - "오늘 공부한 내용 요약 및 정리" (Summary of today's study). Summarizes AI and ML definitions, Data components (Feature/Label), and 1D feature learning.
- **Purpose**: To conclude the first lecture by answering the final quiz question and providing a summary of the core concepts covered.

## 스크린샷 2026-03-24 095003.png
- **Visual Content**: A presentation slide showing the continuation of the lecture summary.
- **Main Text**: 
  - "강의 정리" (Lecture Summary continued).
  - Summarizes "Model and hypothesis space", "Learning" (selecting the optimal model from hypothesis space based on data and performance metrics), and "Need for model learning" (Prediction, Important feature identification, Interpretability).
- **Purpose**: To finish summarizing the key takeaways from the first lecture.

## 스크린샷 2026-03-24 095008.png
- **Visual Content**: Four presentation slides stacked vertically.
- **Main Text**:
  - Slide 1: Title slide for a new lecture: "AI & 기계학습 기초 2: 지도학습은 무엇인가?" (AI & ML Basics 2: What is Supervised Learning?).
  - Slide 2: "CONTENTS" - 1. Concept of Supervised Learning, 2. Regression, 3. Classification, 4. Purpose of Learning.
  - Slide 3: "학습 목표" (Learning Objectives) - Understanding differences between regression and classification, selecting appropriate error metrics, understanding that the goal is maximizing test performance, and understanding overfitting.
  - Slide 4: Sub-title "0. 학습 시작(Overview)".
- **Purpose**: To introduce the second lecture focusing on Supervised Learning, outlining its contents and objectives.

## 스크린샷 2026-03-24 095023.png
- **Visual Content**: A completely blank white screen.
- **Main Text**: None.
- **Purpose**: Likely a slide transition, a rendering error, or an intentional pause during the presentation.

## 스크린샷 2026-03-24 095029.png
- **Visual Content**: A presentation slide with text.
- **Main Text**: 
  - "0. 학습 시작" (Overview).
  - Defines Supervised Learning as "Making AI that solves new problems well" (처음 보는 문제도 잘 푸는 AI 만들기).
  - It learns prediction rules using inputs (features) and answers (labels).
  - Goal: Improve prediction performance not just on training data, but on unseen data.
- **Purpose**: To give a high-level definition and state the ultimate goal of supervised learning.

## 스크린샷 2026-03-24 095033.png
- **Visual Content**: A presentation slide with text and an illustration.
- **Main Text**: 
  - Continues "0. 학습 시작" (Overview).
  - Examples provided: 1) Predicting customer churn using past customer data. 2) Detecting new fraudulent transactions using past fraud data.
  - Illustration shows "Training data" going into "Supervised Learning" to produce a "Data predictive model".
- **Purpose**: To provide concrete business examples of where supervised learning is applied.

## 스크린샷 2026-03-24 095039.png
- **Visual Content**: Two presentation slides stacked vertically.
- **Main Text**:
  - Slide 1: Title slide "1. 지도학습의 개념" (Concept of Supervised Learning).
  - Slide 2: Sub-title "1-1. 지도학습(Supervised learning)이란?" (What is supervised learning?). Re-emphasizes that it's a method of learning a prediction model using training data that has correct answer labels.
- **Purpose**: To formally start the first section on the concept of supervised learning.

## 스크린샷 2026-03-24 095044.png
- **Visual Content**: A presentation slide showing an image classification process.
- **Main Text**: 
  - Explains the supervised learning process visually.
  - "Training Data (Train Set)" with labels (Cat, Dog) goes into "Learning" to create a model.
  - "Test Data (Test Set)" without labels is fed into the "Model generation and application" phase.
  - The model outputs predictions, which are then checked for "Results confirmation" (evaluating if predictions are correct).
- **Purpose**: To visually illustrate the workflow of training and testing a supervised learning model using image classification as an example.

## 스크린샷 2026-03-24 095050.png
- **Visual Content**: A presentation slide showing a table.
- **Main Text**: 
  - "1-2. 지도학습의 종류 (회귀 vs 분류)" (Types of Supervised Learning: Regression vs Classification).
  - Focuses on Regression (회귀): Used when the value you want to predict is a numerical value (숫자). Examples: Price, score, temperature.
  - Shows a table mapping "Study time" to "Test score" to illustrate predicting a continuous number.
- **Purpose**: To introduce Regression as a sub-type of supervised learning and define its characteristic numerical output.

## 스크린샷 2026-03-24 095054.png
- **Visual Content**: A presentation slide comparing two concepts visually.
- **Main Text**: 
  - Continues comparing Regression vs Classification.
  - Adds Classification (분류): Used when the value you want to predict is a categorical value (범주). Examples: Spam/normal, presence/absence of disease.
  - Shows examples of Spam/Normal email classification and Cat/Dog/Hamster image classification.
- **Purpose**: To introduce Classification as the other main sub-type of supervised learning and contrast it with Regression.

## 스크린샷 2026-03-24 095059.png
- **Visual Content**: A presentation slide with text definitions and a graph.
- **Main Text**: 
  - "1-3. 지도학습 용어" (Supervised Learning Terminology).
  - Defines Feature (x): Explanatory variable used for prediction.
  - Defines Label (y): The correct answer to be guessed.
  - Defines Predicted value (y-hat): The result output by the model.
  - Defines Error: The difference between the predicted value and the label (y-hat - y). A graph shows actual values (black dots) and predicted values (red line) to visualize the error.
- **Purpose**: To standardize the vocabulary and mathematical notation used in supervised learning.

## 스크린샷 2026-03-24 095104.png
- **Visual Content**: Two presentation slides stacked vertically.
- **Main Text**:
  - Slide 1: Title slide "2. 회귀(Regression)".
  - Slide 2: Sub-title "2-1. 회귀(Regression) 문제" (Regression Problem). Defines it as predicting a number accurately from inputs. Shows a scatter plot with a linear regression line.
- **Purpose**: To transition into the specific topic of Regression models.

## 스크린샷 2026-03-24 095109.png
- **Visual Content**: Two presentation slides stacked vertically.
- **Main Text**:
  - Slide 1: Duplicate of the previous "2-1" slide with the scatter plot.
  - Slide 2: Gives two concrete examples of regression. 1) Predicting house price (Label) based on area, rooms, age (Features). 2) Predicting sales (Label) based on TV, radio, internet ad spend (Features).
- **Purpose**: To provide practical data table examples for regression problems.

## 스크린샷 2026-03-24 095114.png
- **Visual Content**: A presentation slide with text.
- **Main Text**: 
  - "2-2. 회귀 오류: 평균제곱오차(MSE)" (Regression Error: MSE).
  - Asks "How do we know how accurate the prediction is?" States the need for an index to measure prediction accuracy numerically.
- **Purpose**: To introduce the need for a formal evaluation metric for regression models.

## 스크린샷 2026-03-24 095126.png
- **Visual Content**: A presentation slide with math formulas and a graph.
- **Main Text**: 
  - Continues "2-2. 회귀 오류: 평균제곱오차(MSE)".
  - Explains MSE (Mean Squared Error): The average of the squared differences between the correct answer and the prediction. Penalizes larger errors more due to squaring. Shows the mathematical formula.
  - Introduces RMSE (Root Mean Squared Error) as a way to return the error metric to the original data's unit scale for easier interpretation.
- **Purpose**: To mathematically define MSE and RMSE as the standard evaluation metrics for regression models.

## 스크린샷 2026-03-24 095135.png
- **Visual Content**: A presentation slide with math formulas and a graph.
- **Main Text**: 
  - "2-3. 회귀 설명력: R^2 (결정계수)" (Regression Explanatory Power: R-squared / Coefficient of Determination).
  - Defines R^2 as the proportion of variance in the Label explained by the Feature. Indicates how much better the model is at guessing the actual value compared to a simple average prediction. Ranges 0 to 1 (closer to 1 is better).
  - Shows the formula for R^2 and asks a question: "Can R^2 be negative?".
- **Purpose**: To introduce R-squared as an alternative metric that measures relative model performance rather than absolute error.

## 스크린샷 2026-03-24 095141.png
- **Visual Content**: A presentation slide identical to the previous one, but with an answer revealed.
- **Main Text**: 
  - Answers the question "Can R^2 be negative?". The answer is yes. It happens if the model's predictions are worse than just predicting the simple average of the data.
- **Purpose**: To clarify an important edge case regarding the R-squared metric.

## 스크린샷 2026-03-24 095147.png
- **Visual Content**: A presentation slide showing a comparison table.
- **Main Text**: 
  - "2-4. MSE vs R^2".
  - Compares the two metrics side-by-side. MSE ranges 0 to infinity, has data units, measures absolute error size, and is better when closer to 0. R^2 ranges 0 to 1, has no units, measures relative performance, and is better when closer to 1.
- **Purpose**: To contrast the absolute (MSE) and relative (R^2) evaluation metrics for regression.

## 스크린샷 2026-03-24 095152.png
- **Visual Content**: Three presentation slides stacked vertically.
- **Main Text**:
  - Slides 1 & 2: Explain how to interpret MSE and R^2 values in a practical scenario. For example, MSE = (10M won)^2 means the average error is about 10M won. R^2 = 0.8 means the model explains 80% of the data's variance (80% better than average prediction).
  - Slide 3: Recommends using MSE when the specific absolute size of the error is important, and using R^2 when you want an intuitive evaluation of model performance or need to compare different models. Suggests using them complementarily.
- **Purpose**: To provide practical guidance on how to interpret and choose between MSE and R-squared in real-world scenarios.

## 스크린샷 2026-03-24 095157.png
- **Visual Content**: Two presentation slides stacked vertically.
- **Main Text**:
  - Slide 1: Title slide "3. 분류(Classification)".
  - Slide 2: Sub-title "3-1. 분류(Classification) 문제" (Classification Problem). Defines it as predicting a categorical output. Gives examples of Binary/Multiclass labels. Shows data tables for Spam detection and Medical diagnosis as examples.
- **Purpose**: To transition from Regression to the second major type of supervised learning: Classification.