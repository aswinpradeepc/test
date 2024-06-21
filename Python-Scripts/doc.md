To suggest an optimised path to delivery agents with up to 150 [waypoints](https://www.notion.so/Route-Optimization-Docs-959fea46041f43b390f8ecc264a00539?pvs=21).

Route Optimisation is a classic algorithmic problem studied by many under the topic [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), [Vehicle Routing Problem](https://en.wikipedia.org/wiki/Vehicle_routing_problem) etc.

Lot of corporations, startups and open source projects based on logistics optimisation exist. 

| Proprietary | OpenSource |
| --- | --- |
| Mapbox | OpenRouteService |
| Circuit | Graphhopper |
| RouteXL | Vroom Project |

The one most apt for our use case is [OpenRouteService](https://openrouteservice.org/) . They have a comparatively liberal [pricing plan](https://openrouteservice.org/plans/) and our requirements should be satisfied with free plan itself. They have a limit of 70 locations per request for the optimization API request. I used it and was able to optimize routes with less than 50 locations only.  

The Workaround - Process in batches. However batching should be done according to the places that are close to each other. This can be done by clustering them with distance as the parameter. In ideal case this should be done with distances from each points as the distance to them through road. This requires the calculation of Distance Matrix and API calls to G maps or similar services. 

An optimal workaround is to use euclidean distance to cluster points. The algorithm used here is K means clustering algorithm. It is an unsupervised machine learning algorithm where K denotes the number of clusters to be made. Limit has been implemented to ensure that all clusters made are below 50 in size. I used [Scikit-learn](https://scikit-learn.org/stable/) library to implement this. 

The clusters are then send to ORS optimization api → [Link to documentation](https://openrouteservice.org/dev/#/api-docs/optimization). 

[ORS Backend Docs](https://giscience.github.io/openrouteservice/)

I implemented this model with the help of this [tutorial](https://syntaxbytetutorials.com/vehicle-route-optimization-in-python-with-openrouteservice/). It uses a [python wrapper for ORS](https://github.com/GIScience/openrouteservice-py) and [folium](https://python-visualization.github.io/folium/latest/) (library to integrate [leaflet](https://leafletjs.com/) with python).

Testing was done with 150 locations in UAE that I mapped in using Google earth. The project file exported is 

[150locations_UAE.kml](https://prod-files-secure.s3.us-west-2.amazonaws.com/2ca3e28c-98bc-4cd6-85ef-ea874edbfb12/9a49266d-61ca-4425-87a2-28c6673cf13d/150locations_UAE.kml)

Script to extract location coordinates from .kml file is [parse_kml_coords.py](https://github.com/aswinpradeepc/Route_Optimisation/blob/main/parse_kml_coords.py). The jupyter notebook code used for test is available at [github](https://github.com/aswinpradeepc/Route_Optimisation/blob/main/OpenRouteService.ipynb).

** waypoints - an intermediate point or place on a route or line of travel
