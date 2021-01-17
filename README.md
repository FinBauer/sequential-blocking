# sequential-blocking
A small tool to run a web application to perform sequential blocking in online (survey) experiments where participants arrive sequentially. I have used the tool with pilot experiments conducted via Qualtrics, but it can be used with any survey software that can send GET requests.

The tool follows the setup in https://github.com/diagdavenport/rpy2-heroku (also see Cavaille, Charlotte, “Implementing Blocked Randomization in Online Survey Experiments”, https://charlottecavaille.com). Main differences are:

1. This tool stores covariate-treatment profiles in Redis because Heroku has an ephemeral filesystem and past profiles may get lost if the experiment runs several days and .
2. For my purposes, exact blocking on a few discrete covariates was sufficient so I implemented my own small exact blocking function in Python. For more elaborate blocking schemes using the R blockTools package see the rpy2-heroku tool.

### Use
1. Set up Heroku account and install Python buildpack. Also set up Heroku Redis account
2. Adjust sequential_blocking.py as needed (see comments in file)
3. Push all files to Heroku

