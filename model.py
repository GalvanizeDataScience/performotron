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
    def __init__(self, model, X, y,
                 config_file='config.yaml'):
        """model: a fit sklearn-type model with a predict
                  method. That returns a vector of targets.
        X: Test features
        y: Test target.        
        """
        self.model = model
        self.data = X
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

    @property
    def prediction(self):
        return self.model.predict(self.data)
        
    def score(self):
        """This scores the data and reports the result to the user.
        """
        return self.model.score(self.data, self.target)

    def get_config(self, keys):
        if not self.config:
            self.config = {}
        for k in keys:
            if k not in self.config:
                self.config[k] = raw_input("What %s should I use report results?" %k)
                yield self.config[k]

        with open(self.config_file, 'w') as outfile:
            outfile.write(yaml.dump(self.config))
        return

    def report_to_slack(self):
        """Report the score on slack.
        """
        channel, username = self.get_config()
        
        data = {"channel":channel,
                "username":username,
                "text":"Got a model score of: %s" % self.score()
        }
        return requests.post(self.get_config('slack_url'),
                     data=json.dumps(data))
