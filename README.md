### TASK DJANGO REST FRAMEWORK
# Description
A django application which provides API endpoints for [task tracking app](https://github.com/Clinton-dev/angular-crash).

The following are a list of endpoints:
1. Display list of all tasks: `/tasks/`
2. Task detail end point: `tasks/task/detail/<pk>/`
3. Create a task: `tasks/create/`
4. Delete a specific task: `tasks/delete/<pk>/`

### Screenshot
![](./screenshot.png)


## Getting Started

- Clone this repository to your computer. `git clone https://github.com/Clinton-dev/task_drf.git`
- Open terminal command line then navigate to the root folder `cd task_drf`
- Create virtual environment `python3 -m venv --without-pip <virtual environment name>`
- Run your virtual environment `source <virtual environment name>/bin/activate`
- Install Django in your environment `python -m pip install Django`
- Install other extensions required for the app to run `pip install -r requirements.txt`
- requirements.txt is in the root folder
- Run `python manage.py runserver`
- Open your browser and head to the following url: `http://localhost:8000/`

### Prerequisites

Django requires Python and you can install python for your specific operating system by following this documentation [Python download](https://www.python.org/downloads/)

## Deployment

Follow this resource if you want to deploy the app [deployment](https://github.com/bernie-haxx/Deployment_to_heroku_django)

## Built With

* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/) - Backend framework used
* [django-rest-framework ](https://www.django-rest-framework.org/) - Django rest framework
* [django cors headers ](https://pypi.org/project/django-cors-headers/) - Django cors headers


### Link to Live Site
[Link to live site](https://insta-clone-254.herokuapp.com/)

## Author

* **Clinton Wambugu** - [Clinton-dev](https://github.com/Clinton-dev)


## copyright & License Info
MIT Copyright (c) 2022 Clinton Wambugu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

