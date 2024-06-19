import xml.etree.ElementTree as ET

def extract_coordinates(kml_file):
    coordinates = []
    tree = ET.parse(kml_file)
    root = tree.getroot()

    for placemark in root.iter("{http://www.opengis.net/kml/2.2}Placemark"):
        coords = placemark.find("{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates")
        if coords is not None:
            lon, lat, _ = coords.text.split(",")
            coordinates.append([float(lon), float(lat)])

    return coordinates

if __name__ == "__main__":
    kml_file = "150locations(1).kml"
    coords = extract_coordinates(kml_file)
    print("coords =", coords)
