# WF-ML-BATCH-MILESTONE-1
This repo contains the ml model code file, flask deployment tool for the same, and profile report of the WF case study 1 dataset.

Information about the dataset statistics, shape and presence of any null values/incorrect imputation is present in Data_Profile_Report.html file. 

With regards to the specific information requested in the case study, the findings are as follows:-
1. Number of unique in each column:
ID                    5000
Age                     45
Experience              47
Income                 162
ZIP Code               467
Family                   4
CCAvg                  108
Education                3
Mortgage               347
Personal Loan            2
Securities Account       2
CD Account               2
Online                   2
CreditCard               2

2. Number of people with zero mortgage: 
3462

3. Number of people with zero credit card spending per month:
106

4. Value counts of all categorical columns:
Family:
1   0.29
2   0.26
3   0.20
4   0.24
Education:
1   0.42
2   0.28
3   0.30
Personal Loan:
0   0.90
1   0.10
Securities Account:
0   0.90
1   0.10
CD Account:
0   0.94
1   0.06
Online:
0   0.40
1   0.60
CreditCard:
0   0.71
1   0.29

Univariate and Bivariate analysis results are presented in Data_Profile_Report.html file. Nevertheless, some observations from my analysis are:
- ID is an unnecessary variable that adds no meaning to the dataset and plays no role in influencing the output. So, keeping it in the data will result in unwanted statistical role played in the output. Hence, it’s been removed.
- Age and experience have huge correlation (coefficient = 0.99). I tried centralizing the variables and computing the VIFs’, but the values were still very high. So, one of the 2 variables need to be removed. I have removed the Age variable.
-	Regarding the ZIP Code, even though it’s a numerical value, it does not have any inherent order, and hence, does not help in regression. One solution is to categorize the zip codes in terms of the broader locations (split the US map in x number of regions, etc). Another solution is to entirely remove this variable. The latter has been adopted in this analysis. 
- Besides Experience, all numerical variables including CCAvg, Mortgage and Income were positively skewed. However, the data has not been modified to see if the ML models perform well for this particular case. Also, non-normality in the input variables is not a big issue here since the sole goal is to determine the value of the output (whether the personal loan has been accepted or not).
- For the categorical variables, dummy variables were made for Family and Education. Again, skewness in CD Amount, Online and CreditCard have been left unmodified.

Results:
Results from ML Analysis are present in the ML_case_study.ipynb file in the results dataframe. The conclusion is that by computing a net score obtained as a weighted average of the recall, roc auc score, testing and training accuracies, Random Forest classifier outperformed all other algorithms. 

Ways to make the model perform better:
- Iterate over the various parameters of each classifier and optimize for the best combination based on its performance.
- Include the ZIP code variable as a categorical variable by clubbing regions in terms of states or cardinal directions. The model may not necessarily perform better, but it will give an insight on the regional preferences of the loan.
- Modify the aforementioned skewed input variables through various techniques to be represent all classes similarly can improve the model's performance in general.

Business Understanding:
- The loan is accepted by people belonging to the typical low risk fraternity - high income and well educated, with a sizeble family, considerable credit spendings and high mortgage payments. 
- The loan does not appeal to the youth, who have lower income and small/no family, low credit spendings and small/no mortgage payments, who do not have big financial responsibilities and are willing to take higher risk.
- Having a credit card or a Securities Account does not play a role in acceptance of personal loan, whereas, having a CD account does increase chances of buying a loan.

Model Deployment:
- The ML model has been deployed using the Flask python module and files are attached in this repository. 



