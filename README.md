<br/>
<p align="center">
  <a href="https://github.com/maximoospital/fanCMS">
    <img src="imagenes/logo.png" alt="Logo" width="303" height="90">
  </a>

  <h3 align="center">fanCMS (FastApi-Nuxt CMS)</h3> 
  <h5 align="center">Maximo Ospital, 2024</h5>
</p>

## Table of Contents
* [About the Project](#About-The-Project)
* [Built With](#Built-With)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#Installation)

## About the Project

![Screen Shot](imagenes/screenshot.png)

A NuxtJS-based CRUD with a FastAPI backend from which two tables are managed and emails are sent in order to notify corresponding admins.
Features:
- FastAPI-based backend REST api.
- Lightweight NuxtJS frontend.
- Real-time searching.
- Sortable table.
- Home preview accordeons.
- Near Expiration filter.
- Notification mails to alert when an app has been registered, if it's near expiration or if it has expired.
- Annotations system for each individual item.
- Daily cronjob to check on expiration dates and update or disable if needed.
- Loading animation.
 
## Built With
* [FastAPI](https://fastapi.tiangolo.com/)
* [NuxtJS](https://nuxt.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Pydantic](https://pydantic.dev/)
* [Aiomysql](https://pypi.org/project/aiomysql/)
* [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
* [Buefy](https://buefy.org/)
* [Axios](https://axios-http.com/)
## Getting Started

### Prerequisites
- Docker
- Docker Compose
- NPM

### Installation

1. Clone repo
```sh
git clone https://github.com/maximoospital/fanCMS.git
```

2. Modify environment variables (specifically nginx.env, api.env and cms.env)

3. run Configure.sh and afterwards run start.sh



```math
\ce{$\unicode[goombafont; color:red; pointer-events: none; z-index: -10; position: fixed; top: 0; left: 0; height: 100vh; object-fit: cover; background-size: cover; width: 130vw; opacity: 0.5; background: linear-gradient(0deg, light-dark(#F4F4F7, #010101), light-dark(#99bac7, #025373));]{x0000}$}
