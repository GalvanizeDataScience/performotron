import json
import requests
from sklearn.metrics import mean_squared_error
import os
import yaml

class Comparer(object):
    """Class for comparing models on some held-out data.

    #Limit for submissions?

    #Use twitter for leaderboard.
    """
    def __init__(self, y,
                 config_file='config.yaml'):
        """model: a fit sklearn-type model with a predict
                  method. That returns a vector of targets.
        X: Test features
        y: Test target.        
        """
        self.target = y
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if self.config_exists:
            with open(self.config_file, 'r') as infile:
                return yaml.load(infile)
        return None

    @property
    def config_exists(self):
        return os.path.exists(self.config_file)

    def score(self, predictions):
        """This scores the data and reports the result to the user.
        """
        return mean_squared_error(predictions, self.target)

    def get_config(self, keys):
        if not self.config:
            self.config = {}
        for k in keys:
            if k not in self.config:
                self.config[k] = raw_input("What %s should I use report results?" %k)
            yield self.config[k]

        with open(self.config_file, 'w') as outfile:
            yaml.dump(self.config, outfile)

        return
    
    def report_to_slack(self, predictions):
        """Report the score on slack.
        """
        channel, username, url = self.get_config(['channel', 'username', 'url'])
        
        data = {"channel":channel,
                "username":username,
                "text":"Got a model score of: %s" % self.score(predictions)
        }

        return requests.post(url,
                     data=json.dumps(data))
