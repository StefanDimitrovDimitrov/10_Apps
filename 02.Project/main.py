import folium

location = [42.698334,23.319941]
location_marker = [42.698350,23.319950]
map = folium.Map(location=location, zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=location_marker, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")