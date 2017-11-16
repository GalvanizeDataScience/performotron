Performotron
========

This code is intende to duplicate the spirit of a Kaggle competition for the students.

The idea is that it will score the code on some training data, and report the score to a specified slack channel as a bot.

Installation
=====
If you have access to the repo, you should be able to do:

`pip install git+https://github.com/gschool/dsi-performotron.git`

How to make it work
========

The `Comparer` class can be instantiated with one argument--a target array--this
would represent the true values of some testing dataset.

This data is then compared against some values submitted by the user,
either to the `score` method, or to the `report_to_slack` method.

The default scoring is mean-squared-error, but the score method can be
overridden in subclasses to achieve different behavior.

A config yaml file can be specfied when `Comparer` is instantiated. This could include
information about the username ot report results as, the channel, and the slack url.
If some piece of information is missing, user input will be requested, and then saved
for subsequent runs.

Minimally, it works like this, and would prompt user for a slack url, channel, and
username.

    c = Comparer(test_targets)
    c.report_to_slack(predictions)

Slack configuration.
=====

To allow posting to the correct channel, you must have an incoming-webhooks
integration setup in slack. Each team you'd like to post to needs its own
setup add channels [here.](https://gstudents.slack.com/services/new/incoming-webhook)


You'll then need to report URL and channel to and users of the Comparer (the
students e.g.), so they can enter it when prompted.



