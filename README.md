# user_activity

user_activity is an Django application with UserTask and ActivityPeriod models, 
Also have a custom management command which is used to populate the database with dummy data.

Command to populate db : 
`python manage.py create_usertask (no)`



This API serves the data in json format.

```
{
    "ok": true,
    "members": [
    {
            "id": 11,
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "2020-07-08T19:40:04Z",
                    "end_time": "2020-07-08T19:40:06Z"
                }
            ]
        },
        {
            "id": 12,
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "2020-07-08T19:40:23Z",
                    "end_time": "2020-07-08T19:40:24Z"
                }
            ]
        }
    ]
}
```

Application is live with heroku : https://tranquil-ridge-38738.herokuapp.com/usertask/




