# Weather API Backend

As an API user you can get the minimum, maximum, average and median temperature for a given city and period of time.

#### Expected deliverables

Create a Django application with RESTful API to provide the following

* Django's application must run locally
* API must be in the format /api/locations/{city}/?days={number_of_days}
* API must fetch weather data from some public API of your choice
* API must compute min, max, average, and median temperature
* Response format must be in the following structure:

```json
{
  "maximum": "value",
  "minimum": "value",
  "average": "value",
  "median": "value"
}
```

## Site Map
      - Home: index.md
      - API Guide:
            - Introduction: api-guide/1.introduction.md
            - How to use the API: api-guide/2.how_to_use.md
      - Test Guide
            - How to test the API: test/1.how_to_test.md
      - Jobs: community/jobs.md
