# python-bdd-testing
# If you want to just run scenario(without allure report) use command like this: behave features/checkout_with_db.feature
# If you want have allure reports - install allure-behave and use command like this for run your scenario:
# behave -f allure_behave.formatter:AllureFormatter -o reports/ features
# for watching allure report in your browser use this command : allure serve reports
 
#BEFORE ALL THAT ABOVE  YOU MUST:

# 1) Install allure - for example: In a terminal, run this command:  brew install allure.
# 2) In PyCharm go to PyCharm Settings->Project Interpreter and there add allure-behave