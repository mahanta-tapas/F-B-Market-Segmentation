
/*People in younger age groups are more stressed than others.*/
ods rtf file='Age_group_Stress_ChiSquared';
proc freq data=srg_data;
tables hS3_age_group*Q1ra_is_stressed/ChiSq;
run;
ods rtf close;

/*Stressed people have different eating habits than others*/
ods rtf file='Stressed_peole_eating_out_ChiSquared';
proc freq data=srg_data;
tables Q1ra_is_stressed*type_of_restaurant/ChiSq;
run;
ods rtf close;

/*Do people who feel stressed-out also snack more?*/

ODS RTF File = 'Stressed.rtf';
PROC FREQ DATA=srg_data NLEVELS;
TABLE Q1rb_Work_too_much*Q1ra_is_stressed *S2;
RUN;
ODS RTF CLOSE;

/*Do people who feel stressed-out and work too much snack more?*/
ODS RTF File = 'Work to much.rtf';
PROC FREQ DATA=srg_data NLEVELS;
TABLE Q1rb_Work_too_much*Q1ra_is_stressed*Q25 *S2;
RUN;
ODS RTF CLOSE;


/* Snacks histogram*/

ODS RTF FILE = 'Snack Histogram.rtf';
PROC sgplot data=srg_data;
histogram numofSnacks / scale = count binstart = 0 binwidth = 1 transparency=0.5 group =Q1ra_is_stressed;
density numofSnacks / type = normal;
title '# of Snacks Eaten last 24hrs Histogram';
run;
ODS RTF CLOSE;

/* Generalized Logistic Regression for Intent Analysis*/

/*
S2 - Gender,D6 - income group S3 - age */
ods rtf file='Choice Intention Generalized Logit regression';
proc logistic data=srg_filtered_data;
class S2(ref='Female') D6(ref='Less than $15,000') Q1ra_is_stressed /param = ref;
model choice(event='Tasty_Pizza') = S2 D6 S3 Q1ra_is_stressed S3*Q1ra_is_stressed / link=glogit;
run;
ods rtf close;


ods rtf file='price_sensitivity_regression';
proc logistic data=project.data;
class Gender(ref='0') ethnicity(ref='White') Married(ref='0') Education(ref='0') Work(ref='0') D11;
logit: model Q30rbb_food_price_shopper(event='1') = Gender ethnicity Married Education Work D11;	
run;
ods rtf close;
