from performotron import Comparer
from sklearn import datasets, cross_validation, linear_model
from nose.tools import assert_equal

def get_comparer():
    boston = datasets.load_boston()
    data = boston['data']
    target = boston['target']
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, target,
                                                            test_size=.2)


    #OLS = linear_model.LinearRegression()
    #OLS.fit(X_train, y_train)

    url = 'https://hooks.slack.com/services/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'
    
    c = Comparer(y_test)
    return c, X_test, y_test


def test_score():
    c, _, y_test = get_comparer()
    #assert c.score(y_test)
    #Score is zero cause we're scoring test data.
    assert c.score(y_test) == 0


#def test_slack():
 #   c, _, y_test = get_comparer()

    #resp = c.report_to_slack(y_test)
    #assert_equal(resp.status_code, 200)
    

