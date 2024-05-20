# ordinal logistic regression
# install the package 'carData'
install.packages('carData')
library(carData)
library(MASS)

data(WVS)
head(WVS)

# descriptive statistics
summary(WVS)

# fit the proportional odds logistic regression model using
# polr function from the MASS package
model_fit <- polr(poverty~religion+degree+country+age+gender, data=
                    WVS, Hess = TRUE)
summary(model_fit)

summary_table <- coef(summary(model_fit))
pval <- pnorm(abs(summary_table[, "t value"]),lower.tail=FALSE)*2
summary_table <- cbind(summary_table, "p value" = round(pval,3))
summary_table
