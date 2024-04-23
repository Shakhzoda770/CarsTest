# playwright-with-python

# setup environment
python3 -m venv venv

source venv/bin/activate

# Install required modules
 pip install -r requirement.txt


# Run tests with allure path  as an argument 
 pytest tests/test_nav.py --alluredir=./allure-results/

# See Allure report
allure serve allure-results