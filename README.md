## Deployment notes
These notes are for use later when I need to write part of the deployment section for pp4

1. Log in to Heroku and navigate to your dashboard.
2. Click on the 'New' button in the upper right and select 'Create new app.'
3. Pick a unique name for your App, select the appropriate region, and click 'Create app.'
4. Click on the 'Settings' tab, scroll down to the 'Config Vars' section, and click 'Reveal Config Vars.'
5. Add a key-value pair with key `DISABLE_COLLECTSTATIC` and value `1`.
6. Add a key-value pair with key `DATABASE_URL`and value the database url provided. (If you no longer have access to this, please contact me.)

(should this be a different deployment section)

6. Install a production ready web-server by entering `pip3 install gunicorn~=20.1` into the terminal.
7. Add this to the requirements.txt file with the terminal command `pip3 freeze --local > requirements.txt`.
8. Create a file (without any extension) named 'Procfile' in the root directory of the repository.
9. Add the line `web: gunicorn my_project.wsgi` to this file and save it. Heroku will use this to run our web app.

(should this be a different deployment section)

10. In the `settings.py` file located in the `my_project` directory, change `DEBUG=True` to `DEBUG=False`.
11. While in `settings.py`, append `, '.herokuapp.com'` to the end of the `ALLOWED_HOSTS` list (if there are no other hosts listed, simply add `'.herokuapp.com'`). (it says to remember the comma, but this is only relevant if there are other hosts, right?)

(is this even a deployment step? I guess so since we will deploy from github and need the procfile)

12. Push these changes to GitHub.
13. Navigate to the 'Deploy' tab of your app on Heroku and enable 'Connect to GitHub' in the 'Deployment method' section.
14. Enter the name of the repository for the project in the search box and click 'Search.'
15. Select the repository from the list of search results.
16. Click 'Deploy Branch' to begin a manual deployment of the relevant branch.

(is this a different deployment section?)

17. Scroll up and open the 'Resources' tab.
there are steps about adding eco dynos and making sure there is no db installed yet. The first isn't entirely relevant to this but will be, not sure about the second. The steps are saved in logseq.

Environment variables
18. Create a file called env.py in the root directory. Add
`import os

os.environ.setdefault(
    "DATABASE_URL", >database_url<)`
where you replace `>database_url<` with the database url provided.
(If you no longer have access to this, please contact me.)
