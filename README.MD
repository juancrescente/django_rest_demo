## Hello and welcome to <<<Backend Potential hire Project 2.0>>>
 



### Considerations:
- Used djangorestframework and djangorestframework-gis
- Implemented token auth, you can try it but I've disabled it in endpoints so you can easily navigate through it using restframework html views
- I used sqlite with spatialite engine although in a production environment I'd rather use postgres
- Deployed to a EC2 Ubuntu instance
- Nginx and gunicorn

### Quick testing data

Login to the admin via

```
http://18.223.211.9/admin/login/?next=/admin/
```

Make a query with a point in Mexico via
```
http://18.223.211.9/api/query/?lat=21.215892&lng=-99.379898
```

### Implemented models
- Provider
    - Name
    - Email
    - Phone number
    - Language
    - Currency
- Currency
    - Symbol
    - Name
- Language
    - Name
    - Short name
- Service Area
    - Provider
    - Price
    - Polygon

### Implemented requirements

- Django admin CRUD for currencies, languages, providers and services areas
- JSON REST API
    - User can create _providers_
    - User can query _providers_
    - User can create _services areas_ on behalf of providers
    - User can query all _services areas_
    - User can query _services areas_ within a geographical point
    
### Development

To install this demo project you can use the following snippet

```
#make sure to install gdal as indicated here https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html
#also spatialite extension
sudo apt-get install libsqlite3-mod-spatialite
#Clone the repo
git clone https://github.com/juancrescente/django_rest_demo.git
#Enter project directory
cd django_rest_demo
#Create a virtual environment
virtualenv -p python3 venv
#Activate it
source venv/bin/activate
#Install dependencies
pip3 install -r requirements.txt
#Run migrations
python manage.py migrate
#Create a super user
python manage.py createsuperuser
#(optional) get an auth token
python manage.py drf_create_token <username>
#Run a dev server
python manage.py runserver
```
    
### Test with httpie
```
    #Get an auth token
    http POST http://127.0.0.1:8000/api/auth/ username=<username> password=<password>
    #List all providers (notice that token is not required)
    http GET http://127.0.0.1:8000/api/provider/ 'Authorization: Token <token>'
    #List all services areas
    http GET http://127.0.0.1:8000/api/servicearea/
    #Create a provider
    http POST http://127.0.0.1:8000/api/provider/ name='demo name' email='hello@howareyou.com' phoneNumber='1321123' language=1 currency=2
    #Create a service area
    http POST http://127.0.0.1:8000/api/servicearea/ name='demo service' price=200 provider=1 phoneNumber='1321123' language=1 currency=2 poly='{"type": "Polygon","coordinates": [[[-72.33412579243583,-21.07450362996167],[-44.34136159020936,-20.63271391303683],[-36.61531304055972,-41.41654561190464],[-55.49920843998351,-56.1038533898914],[-78.22224175875544,-56.22451767007005],[-80.16393518872619,-34.35538338021033],[-72.33412579243583,-21.07450362996167]]]}'
    #Query service area within given points
    http GET "http://127.0.0.1:8000/api/query/?lat=-34.208752&lng=-58.577201"
```

### API endpoints
- List all providers

```GET /api/provider/```

- Create a provider

```
PUT  /api/provider/

name: <string>
email: <string>
phoneNumber: <string>
language: <id>
currency: <id>

```

- Read a provider

```GET /api/provider/<id>```

- Update a provider

```
PUT /api/provider/<id>

name: <string>
email: <string>
phoneNumber: <string>
language: <id>
currency: <id>

```

- List all service areas

```GET /api/servicearea/```

- Create a service area

```
PUT  /api/servicearea/

provider: <id>
price: <decimal>
poly: geojson

Geojson example:
{"type": "Polygon", "coordinates": [[[3.55, 51.08], [4.36, 50.73], [4.84, 50.85], [4.45, 51.3], [3.55, 51.08]]]}

```

- Read a service area

```GET /api/servicearea/<id>```

- Update a service area

```
PUT /api/servicearea/<id>

Same data as create
```

- Query a service area within a point

```
GET /api/servicearea/<id>

lat: <geographical coordinate>
lng: <geographical coordinate>

```

