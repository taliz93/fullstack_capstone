from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {
            "name": "Nissan",
            "description": "Modern SUVs and Sedans.",
            "market": "JDM"
        },
        {
            "name": "Mercedes-Benz",
            "description": "Powerful Luxury cars and SUVs",
            "market": "Euro"
        },
        {
            "name": "Audi",
            "description": "Fast and sleek automobiles",
            "market": "Euro"
        },
        {
            "name": "Ford",
            "description": "American Trucks and SUVs",
            "market": "USDM"
        },
        {
            "name": "Toyota",
            "description": "Long-standing and reliable cars and trucks",
            "market": "JDM"
        },
    ]
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'],
                                  description=data['description'],
                                  market=data['market']))
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "dealer_id": 0,
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0]
        },
        {
            "dealer_id": 0,
            "name": "Xterra",
            "type": "Truck",
            "year": 2023,
            "car_make": car_make_instances[0]
        },
        {
            "dealer_id": 0,
            "name": "280Z",
            "type": "Coupe",
            "year": 1977,
            "car_make": car_make_instances[0]
        },
        {
            "dealer_id": 0,
            "name": "S 550",
            "type": "Sedan",
            "year": 2021,
            "car_make": car_make_instances[1]
        },
        {
            "dealer_id": 0,
            "name": "CLE 450",
            "type": "Coupe",
            "year": 2025,
            "car_make": car_make_instances[1]
        },
        {
            "dealer_id": 0,
            "name": "AMG E45 4MATIC",
            "type": "Wagon",
            "year": 2024,
            "car_make": car_make_instances[1]
        },
        {
            "dealer_id": 0,
            "name": "A4",
            "type": "SUV",
            "year": 2025,
            "car_make": car_make_instances[2]
        },
        {
            "dealer_id": 0,
            "name": "A5",
            "type": "SUV",
            "year": 2019,
            "car_make": car_make_instances[2]
        },
        {
            "dealer_id": 0,
            "name": "R8",
            "type": "Coupe",
            "year": 2012,
            "car_make": car_make_instances[2]
        },
        {
            "dealer_id": 0,
            "name": "F-150",
            "type": "Truck",
            "year": 2020,
            "car_make": car_make_instances[3]
        },
        {
            "dealer_id": 0,
            "name": "Explorer",
            "type": "SUV",
            "year": 2022,
            "car_make": car_make_instances[3]
        },
        {
            "dealer_id": 0,
            "name": "Mustang",
            "type": "Coupe",
            "year": 2018,
            "car_make": car_make_instances[3]
        },
        {
            "dealer_id": 0,
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4]
        },
        {
            "dealer_id": 0,
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4]
        },
        {
            "dealer_id": 0,
            "name": "4Runner",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[4]
        },
        # Add more CarModel instances as needed
    ]
    for data in car_model_data:
        CarModel.objects.create(name=data['name'],
                                make=data['car_make'],
                                type=data['type'],
                                year=data['year'],
                                dealerid=data['dealer_id'])
