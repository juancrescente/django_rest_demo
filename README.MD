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
    - User can query _services areas_ with a single point
    
### Development

To install this demo project you can use
```
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
#Run a dev server
python manage.py runserver
```
    
### Test with httpie
```
    http http://127.0.0.1:8000/api/servicearea/
```

### API endpoints
- List all providers

```GET /api/provider/```

- Create a provider

```PUT  /api/provider/```

- Read a provider

```GET /api/provider/<id>```

- Update a provider

```PUT /api/provider/<id>```

- List all service areas

```GET /api/servicearea/```

- Create a service area

```
PUT  /api/servicearea/

provider: 1
price: 10
poly: {"type": "Polygon", "coordinates": [[[3.55, 51.08], [4.36, 50.73], [4.84, 50.85], [4.45, 51.3], [3.55, 51.08]]]}

```

- Read a service area

```GET /api/servicearea/<id>```

- Update a service area

```PUT /api/servicearea/<id>```

- Query

```
PUT /api/servicearea/<id>

```