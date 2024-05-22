## Deployment notes
These notes are for use later when I need to write part of the deployment section for pp4

1. Log in to Heroku and navigate to your dashboard.
2. Click on the 'New' button in the upper right and select 'Create new app.'
3. Pick a unique name for your App, select the appropriate region, and click 'Create app.'
4. Click on the 'Settings' tab, scroll down to the 'Config Vars' section, and click 'Reveal Config Vars.'
5. Add a key-value pair with key `DISABLE_COLLECTSTATIC` and value `1`.

(should this be a different deployment section)

6. Install a production ready web-server by entering `pip3 install gunicorn~=20.1` into the terminal.
7. Add this to the requirements.txt file with the terminal command `pip3 freeze --local > requirements.txt`.
8. Create a file (without any extension) named 'Procfile' in the root directory of the repository.
9. Add the line `web: gunicorn my_project.wsgi` to this file and save it. Heroku will use this to run our web app.

(should this be a different deployment section)

10. In the `settings.py` file located in the `my_project` directory, change `DEBUG=True` to `DEBUG=False`.
11. While in `settings.py`, append `, '.herokuapp.com'` to the end of the `ALLOWED_HOSTS` list (if there are no other hosts listed, simply add `'.herokuapp.com'`). (it says to remember the comma, but this is only relevant if there are other hosts, right?)

(is this even a deployment step?)

12. Save the above using `git add .`, `git commit -m "set up app for deployment"`, and `git push`. 