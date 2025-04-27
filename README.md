
## Introduction

<p> This docker environment is for querying BEA data over the web. It
builds the forms from data provided by the BEA website encoded as a json
file.</p>
<p>Some of the time, it's useful to view the BEA data configutation
to see, for example, the set of tables for a dataset, For this, one can
invoke the beahier script that, thє first time, retrieves the data
confituration from BEA and dieplays it as a set of HTML tables. On
occasion, the data confituration changes, so this script can be invoked
with 'Update' selected. It can take quite a bit of time the first time
that 'Show' is invoked because it must get the proper data from BEA,
construct the HTML and serve it. From then on, until or unless
beahier.py is invoked with 'Updata' selected, the BEA structure is
service immediately. If 'Update' is selected, it will take the same
amount of time as the first 'Show'. In addition to serving the HTML,
'Update' also refreshes the json file used to build the menues by
bea.py</p>

<p>bea.py is the main 'CGI' script. It first serves a page allowing one
to select a BEA dataset. Once a dataset is selected, a menu is served
allowing one to select the desired parameters. Last one can select the
desired respons, HTML to display the data as a plot and table or CSV to
allow one to download the data in CSV format</p>
## The Environment

<p>.env file</p>

<p>a BEA_API_KEY environmental variable for BEA<br>
You can get one at https://apps.bea.gov/api/signup/</p>

## The Dockerfile

<p>The Dockerfile starts with alpine linux, lighttpd, and python.<br>
It creates a file hierarchy with suitable permissions.<br>
It copies the shell an python scripts to their proper directories.<br>
The required python librarys are installed in a python venv environment
because of alpine python restrictions.<br>
Іt ends with a CMD directive so that one can enter the running container<br>
if neeced</p>

## Various Shell Scripts

<p>the following are convenience shell scripts
b.sh  - a convenience script to build the container<br>
ds.sh - a convenience script to stop the container<br>
e.sh  - a convenence script to create the .env file<br>
ec.sh - a convenience script to edit the lighttpd.conf file<br>
r.sh  - a convenience script to run the container in the background<br>
rb.sh - a convenience script to rebuild the containe<br>
ri.sh - a convenience script to run the container interactively<br>
rm.sh - a convenience script to remove the container image<br>
ru.sh - a convenience script to run the container interactively as root<br>
sl.sh - a script to start lighttpd with the proper environment<br>
td.sh - a script to test bea.py with varions QUERY_STRINGs<br>
v.sh  - a script to create the python venv invironment</p>

## The python 'CGI' scripts

<p>bea.py       - a web script for retrieving data<br>
beahier.py   - a web script for showing/updating the BEA structure<br>


