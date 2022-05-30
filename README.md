# Django app with Docker, PostgreSQL, REDIS

#Usage
Uses docker + redis.

1- Build the images and run the containers:

      $ docker-compose up -d --build
To apply changes, the image must be re-built.

# API Functionality
### 1. Create,Add,Delete,Update,Filter Province
1.1. New Province. POST Methods

        http://127.0.0.1:8000/api/province/

        {   
          "name":"Ankara",
        }
        
1.2.Province List . GET Methods

    http://127.0.0.1:8000/api/province/

    {   
      "id" : 1,
      "name":"Ankara",
      "create_at" : "29.05.2022",
      "update_at" : "29.05.2022"
    }
   
1.3.Province Detail . GET Methods

    http://127.0.0.1:8000/api/province/id

    {   
      "name":"Ankara"
    }
    
    
1.4.Province Update . PATCH Methods

    http://127.0.0.1:8000/api/province/id

    {   
      "name":"İstanbul"
    }
    

    
1.5.Province Delete . Delete Methods

    http://127.0.0.1:8000/api/province/<int:id>
       
        
### 2.Create,Add,Delete,Update,Filter Town 

2.1. New Town. POST Methods

        http://127.0.0.1:8000/api/town/

        {   
          "name":"Mamak",
          "province" : 1
        }
        
        
        
2.2.Town List . GET Methods

        http://127.0.0.1:8000/api/town/

        {   
          "id" : 1,
          "name":"Mamak",
          "create_at" : "29.05.2022",
          "update_at" : "29.05.2022",
          "province" : 1
        }
   
   
2.3.Town Detail  . GET Methods

        http://127.0.0.1:8000/api/town/id

        {   
          "name":"Mamak",
          "province" : 1
        }
        
        
2.4.Town Update . PATCH Methods

        http://127.0.0.1:8000/api/town/id

        {   
          "name":"Mamak",
          "province" : 1
        }
        
        
2.5.Town Delete . Delete Methods

    http://127.0.0.1:8000/api/town/<int:id>
        
        
###  3.Create,Add,Delete,Update,Filter Weather 

3.1. New Weather. POST Methods

        http://127.0.0.1:8000/api/weather/

        {   
          "weather_forecast":"Yagmurlu",
          "degree" : 19.5,
          "province": 1,
          "town": 2
        }
        
        
        
3.2.Weather List . GET Methods

        http://127.0.0.1:8000/api/weather/

        {   
            "town": "Mamak",
            "weather_forecast": "Yagmurlu",
            "degree": 19.0,
            "province": 3
        }
        
        
3.3.Weather Detail  . GET Methods

        http://127.0.0.1:8000/api/weather/id

        {
            "town": "Mamak",
            "weather_forecast": "Yagmurlu",
            "degree": 12.0,
            "province": 1
        }
        
        
3.4.Weather Update . PATCH Methods

        http://127.0.0.1:8000/api/weather/id

        {   
          "weather_forecast":"Güneşli",
          "degree" : 20.3
        }
        
        
3.5.Weather Delete . Delete Methods

    http://127.0.0.1:8000/api/weather/<int:id>
        
        
        
### 4.All Province and Town List

    http://127.0.0.1:8000/api/weatherforecast
    [
    {
        "name": "Ankara",
        "degree": 12.0,
        "province_weather": [
            {
                "town": "Mamak",
                "weather_forecast": "Yagmurlu",
                "degree": 12.0,
                "province": 1
            },
            {
                "town": null,
                "weather_forecast": "Yer yer yagmurlu",
                "degree": 12.0,
                "province": 1
            }
        ]
    },
    {
        "name": "İstanbul",
        "degree": 25.3,
        "province_weather": [
            {
                "town": "Kadıköy",
                "weather_forecast": "Güneşli",
                "degree": 30.2,
                "province": 2
            }
        ]
    },
    {
        "name": "Amasya",
        "degree": 25.3,
        "province_weather": [
            {
                "town": "Göynücek",
                "weather_forecast": "Yagmurlu",
                "degree": 19.0,
                "province": 3
            }
        ]
    }
]

### 5.Detail of the districts of the provinces Filter

    http://127.0.0.1:8000/api/weatherforecast?province=Amasya
    
    [
    {
        "name": "Amasya",
        "degree": 25.3,
        "province_weather": [
            {
                "town": "Göynücek",
                "weather_forecast": "Yagmurlu",
                "degree": 19.0,
                "province": 3
            }
        ]
    }
]