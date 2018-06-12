import networkx as nx
import numpy as np
import igraph as ig
import shapefile
import csv
import qgis.core
qgis.utils.iface
import matplotlib.pyplot as plt
import processing

from PyQt4.QtCore import QVariant
from qgis.core import QgsField, QgsExpression, QgsFeature

#Clear Canvas
QgsMapLayerRegistry.instance().removeAllMapLayers()

#Set CRS
canvas = iface.mapCanvas()
selectedcrs="EPSG:2163"
target_crs = QgsCoordinateReferenceSystem()
target_crs.createFromUserInput(selectedcrs)
canvas.setDestinationCrs(target_crs)

#Set Paths
boundarypath = "/Volumes/GoogleDrive/My Drive/RRAbandonment/Additional Maps/County_Boundaries/"
statapath ="/Volumes/GoogleDrive/My Drive/RRAbandonment/Additional Maps/Highways/"
hwypath = "/Users/dustball/Dropbox/gis files/interstates/annualHighwayFinalFiles/annualHwyFinalCountyDissolved/"

#Add County Base Shapefile - Year 2000
mastercountylayer = iface.addVectorLayer(boundarypath+"Master20001231Boundaries.shp", "Master2000Boundaries", "ogr")
if not mastercountylayer:
  print "Layer failed to load!"

#1954
#Add Dissolved Highway Files
IHS1954final_dissolved = iface.addVectorLayer(hwypath + "IHS1954final_dissolved.shp", "IHS1954final_dissolved", "ogr")
if not IHS1954final_dissolved:
  print "Layer failed to load!"  
  
#Intersect Hwy Layer and County Boundary Layer
Interstate1954_2000Boundary = processing.runalg('qgis:intersection', IHS1954final_dissolved, mastercountylayer, hwypath+"Interstate1954_2000Boundary.shp")

Interstate1954_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1954_2000Boundary.shp","Interstate1954_2000Boundary", "ogr")
if not Interstate1954_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1954_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1954_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1954_2000Boundary.updateFields()
idx = Interstate1954_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1954_2000Boundary.pendingFields() )

for f in Interstate1954_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1954_2000Boundary.updateFeature( f )

Interstate1954_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1954_2000Boundary,statapath+"Interstate1954_2000Boundary.csv", "utf-8", None, "CSV")

#1956
#Add Dissolved Highway Files
IHS1956final_dissolved = iface.addVectorLayer(hwypath + "IHS1956final_dissolved.shp", "IHS1956final_dissolved", "ogr")
if not IHS1956final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1956_2000Boundary = processing.runalg('qgis:intersection', IHS1956final_dissolved, mastercountylayer, hwypath+"Interstate1956_2000Boundary.shp")

Interstate1956_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1956_2000Boundary.shp","Interstate1956_2000Boundary", "ogr")
if not Interstate1956_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1956_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1956_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1956_2000Boundary.updateFields()
idx = Interstate1956_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1956_2000Boundary.pendingFields() )

for f in Interstate1956_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1956_2000Boundary.updateFeature( f )

Interstate1956_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1956_2000Boundary,statapath+"Interstate1956_2000Boundary.csv", "utf-8", None, "CSV")

#1958
#Add Dissolved Highway Files
IHS1958final_dissolved = iface.addVectorLayer(hwypath + "IHS1958final_dissolved.shp", "IHS1958final_dissolved", "ogr")
if not IHS1958final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1958_2000Boundary = processing.runalg('qgis:intersection', IHS1958final_dissolved, mastercountylayer, hwypath+"Interstate1958_2000Boundary.shp")

Interstate1958_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1958_2000Boundary.shp","Interstate1958_2000Boundary", "ogr")
if not Interstate1958_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1958_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1958_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1958_2000Boundary.updateFields()
idx = Interstate1958_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1958_2000Boundary.pendingFields() )

for f in Interstate1958_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1958_2000Boundary.updateFeature( f )

Interstate1958_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1958_2000Boundary,statapath+"Interstate1958_2000Boundary.csv", "utf-8", None, "CSV")

#1959
#Add Dissolved Highway Files
IHS1959final_dissolved = iface.addVectorLayer(hwypath + "IHS1959final_dissolved.shp", "IHS1959final_dissolved", "ogr")
if not IHS1959final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1959_2000Boundary = processing.runalg('qgis:intersection', IHS1959final_dissolved, mastercountylayer, hwypath+"Interstate1959_2000Boundary.shp")

Interstate1959_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1959_2000Boundary.shp","Interstate1959_2000Boundary", "ogr")
if not Interstate1959_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1959_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1959_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1959_2000Boundary.updateFields()
idx = Interstate1959_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1959_2000Boundary.pendingFields() )

for f in Interstate1959_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1959_2000Boundary.updateFeature( f )

Interstate1959_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1959_2000Boundary,statapath+"Interstate1959_2000Boundary.csv", "utf-8", None, "CSV")

#1963
#Add Dissolved Highway Files
IHS1963final_dissolved = iface.addVectorLayer(hwypath + "IHS1963final_dissolved.shp", "IHS1963final_dissolved", "ogr")
if not IHS1963final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1963_2000Boundary = processing.runalg('qgis:intersection', IHS1963final_dissolved, mastercountylayer, hwypath+"Interstate1963_2000Boundary.shp")

Interstate1963_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1963_2000Boundary.shp","Interstate1963_2000Boundary", "ogr")
if not Interstate1963_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1963_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1963_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1963_2000Boundary.updateFields()
idx = Interstate1963_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1963_2000Boundary.pendingFields() )

for f in Interstate1963_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1963_2000Boundary.updateFeature( f )

Interstate1963_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1963_2000Boundary,statapath+"Interstate1963_2000Boundary.csv", "utf-8", None, "CSV")

#1964
#Add Dissolved Highway Files
IHS1964final_dissolved = iface.addVectorLayer(hwypath + "IHS1964final_dissolved.shp", "IHS1964final_dissolved", "ogr")
if not IHS1964final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1964_2000Boundary = processing.runalg('qgis:intersection', IHS1964final_dissolved, mastercountylayer, hwypath+"Interstate1964_2000Boundary.shp")

Interstate1964_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1964_2000Boundary.shp","Interstate1964_2000Boundary", "ogr")
if not Interstate1964_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1964_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1964_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1964_2000Boundary.updateFields()
idx = Interstate1964_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1964_2000Boundary.pendingFields() )

for f in Interstate1964_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1964_2000Boundary.updateFeature( f )

Interstate1964_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1964_2000Boundary,statapath+"Interstate1964_2000Boundary.csv", "utf-8", None, "CSV")

#1967
#Add Dissolved Highway Files
IHS1967final_dissolved = iface.addVectorLayer(hwypath + "IHS1967final_dissolved.shp", "IHS1967final_dissolved", "ogr")
if not IHS1967final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1967_2000Boundary = processing.runalg('qgis:intersection', IHS1967final_dissolved, mastercountylayer, hwypath+"Interstate1967_2000Boundary.shp")

Interstate1967_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1967_2000Boundary.shp","Interstate1967_2000Boundary", "ogr")
if not Interstate1967_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1967_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1967_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1967_2000Boundary.updateFields()
idx = Interstate1967_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1967_2000Boundary.pendingFields() )

for f in Interstate1967_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1967_2000Boundary.updateFeature( f )

Interstate1967_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1967_2000Boundary,statapath+"Interstate1967_2000Boundary.csv", "utf-8", None, "CSV")

#1969
#Add Dissolved Highway Files
IHS1969final_dissolved = iface.addVectorLayer(hwypath + "IHS1969final_dissolved.shp", "IHS1969final_dissolved", "ogr")
if not IHS1969final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1969_2000Boundary = processing.runalg('qgis:intersection', IHS1969final_dissolved, mastercountylayer, hwypath+"Interstate1969_2000Boundary.shp")

Interstate1969_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1969_2000Boundary.shp","Interstate1969_2000Boundary", "ogr")
if not Interstate1969_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1969_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1969_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1969_2000Boundary.updateFields()
idx = Interstate1969_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1969_2000Boundary.pendingFields() )

for f in Interstate1969_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1969_2000Boundary.updateFeature( f )

Interstate1969_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1969_2000Boundary,statapath+"Interstate1969_2000Boundary.csv", "utf-8", None, "CSV")

#1972
#Add Dissolved Highway Files
IHS1972final_dissolved = iface.addVectorLayer(hwypath + "IHS1972final_dissolved.shp", "IHS1972final_dissolved", "ogr")
if not IHS1972final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1972_2000Boundary = processing.runalg('qgis:intersection', IHS1972final_dissolved, mastercountylayer, hwypath+"Interstate1972_2000Boundary.shp")

Interstate1972_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1972_2000Boundary.shp","Interstate1972_2000Boundary", "ogr")
if not Interstate1972_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1972_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1972_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1972_2000Boundary.updateFields()
idx = Interstate1972_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1972_2000Boundary.pendingFields() )

for f in Interstate1972_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1972_2000Boundary.updateFeature( f )

Interstate1972_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1972_2000Boundary,statapath+"Interstate1972_2000Boundary.csv", "utf-8", None, "CSV")

#1974
#Add Dissolved Highway Files
IHS1974final_dissolved = iface.addVectorLayer(hwypath + "IHS1974final_dissolved.shp", "IHS1974final_dissolved", "ogr")
if not IHS1974final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1974_2000Boundary = processing.runalg('qgis:intersection', IHS1974final_dissolved, mastercountylayer, hwypath+"Interstate1974_2000Boundary.shp")

Interstate1974_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1974_2000Boundary.shp","Interstate1974_2000Boundary", "ogr")
if not Interstate1974_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1974_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1974_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1974_2000Boundary.updateFields()
idx = Interstate1974_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1974_2000Boundary.pendingFields() )

for f in Interstate1974_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1974_2000Boundary.updateFeature( f )

Interstate1974_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1974_2000Boundary,statapath+"Interstate1974_2000Boundary.csv", "utf-8", None, "CSV")

#1976
#Add Dissolved Highway Files
IHS1976final_dissolved = iface.addVectorLayer(hwypath + "IHS1976final_dissolved.shp", "IHS1976final_dissolved", "ogr")
if not IHS1976final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1976_2000Boundary = processing.runalg('qgis:intersection', IHS1976final_dissolved, mastercountylayer, hwypath+"Interstate1976_2000Boundary.shp")

Interstate1976_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1976_2000Boundary.shp","Interstate1976_2000Boundary", "ogr")
if not Interstate1976_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1976_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1976_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1976_2000Boundary.updateFields()
idx = Interstate1976_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1976_2000Boundary.pendingFields() )

for f in Interstate1976_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1976_2000Boundary.updateFeature( f )

Interstate1976_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1976_2000Boundary,statapath+"Interstate1976_2000Boundary.csv", "utf-8", None, "CSV")

#1977
#Add Dissolved Highway Files
IHS1977final_dissolved = iface.addVectorLayer(hwypath + "IHS1977final_dissolved.shp", "IHS1977final_dissolved", "ogr")
if not IHS1977final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1977_2000Boundary = processing.runalg('qgis:intersection', IHS1977final_dissolved, mastercountylayer, hwypath+"Interstate1977_2000Boundary.shp")

Interstate1977_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1977_2000Boundary.shp","Interstate1977_2000Boundary", "ogr")
if not Interstate1977_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1977_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1977_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1977_2000Boundary.updateFields()
idx = Interstate1977_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1977_2000Boundary.pendingFields() )

for f in Interstate1977_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1977_2000Boundary.updateFeature( f )

Interstate1977_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1977_2000Boundary,statapath+"Interstate1977_2000Boundary.csv", "utf-8", None, "CSV")

#1978
#Add Dissolved Highway Files
IHS1978final_dissolved = iface.addVectorLayer(hwypath + "IHS1978final_dissolved.shp", "IHS1978final_dissolved", "ogr")
if not IHS1978final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1978_2000Boundary = processing.runalg('qgis:intersection', IHS1978final_dissolved, mastercountylayer, hwypath+"Interstate1978_2000Boundary.shp")

Interstate1978_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1978_2000Boundary.shp","Interstate1978_2000Boundary", "ogr")
if not Interstate1978_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1978_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1978_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1978_2000Boundary.updateFields()
idx = Interstate1978_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1978_2000Boundary.pendingFields() )

for f in Interstate1978_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1978_2000Boundary.updateFeature( f )

Interstate1978_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1978_2000Boundary,statapath+"Interstate1978_2000Boundary.csv", "utf-8", None, "CSV")

#1979
#Add Dissolved Highway Files
IHS1979final_dissolved = iface.addVectorLayer(hwypath + "IHS1979final_dissolved.shp", "IHS1979final_dissolved", "ogr")
if not IHS1979final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1979_2000Boundary = processing.runalg('qgis:intersection', IHS1979final_dissolved, mastercountylayer, hwypath+"Interstate1979_2000Boundary.shp")

Interstate1979_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1979_2000Boundary.shp","Interstate1979_2000Boundary", "ogr")
if not Interstate1979_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1979_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1979_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1979_2000Boundary.updateFields()
idx = Interstate1979_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1979_2000Boundary.pendingFields() )

for f in Interstate1979_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1979_2000Boundary.updateFeature( f )

Interstate1979_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1979_2000Boundary,statapath+"Interstate1979_2000Boundary.csv", "utf-8", None, "CSV")

#1981
#Add Dissolved Highway Files
IHS1981final_dissolved = iface.addVectorLayer(hwypath + "IHS1981final_dissolved.shp", "IHS1981final_dissolved", "ogr")
if not IHS1981final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1981_2000Boundary = processing.runalg('qgis:intersection', IHS1981final_dissolved, mastercountylayer, hwypath+"Interstate1981_2000Boundary.shp")

Interstate1981_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1981_2000Boundary.shp","Interstate1981_2000Boundary", "ogr")
if not Interstate1981_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1981_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1981_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1981_2000Boundary.updateFields()
idx = Interstate1981_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1981_2000Boundary.pendingFields() )

for f in Interstate1981_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1981_2000Boundary.updateFeature( f )

Interstate1981_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1981_2000Boundary,statapath+"Interstate1981_2000Boundary.csv", "utf-8", None, "CSV")

#1982
#Add Dissolved Highway Files
IHS1982final_dissolved = iface.addVectorLayer(hwypath + "IHS1982final_dissolved.shp", "IHS1982final_dissolved", "ogr")
if not IHS1982final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1982_2000Boundary = processing.runalg('qgis:intersection', IHS1982final_dissolved, mastercountylayer, hwypath+"Interstate1982_2000Boundary.shp")

Interstate1982_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1982_2000Boundary.shp","Interstate1982_2000Boundary", "ogr")
if not Interstate1982_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1982_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1982_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1982_2000Boundary.updateFields()
idx = Interstate1982_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1982_2000Boundary.pendingFields() )

for f in Interstate1982_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1982_2000Boundary.updateFeature( f )

Interstate1982_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1982_2000Boundary,statapath+"Interstate1982_2000Boundary.csv", "utf-8", None, "CSV")

#1986
#Add Dissolved Highway Files
IHS1986final_dissolved = iface.addVectorLayer(hwypath + "IHS1986final_dissolved.shp", "IHS1986final_dissolved", "ogr")
if not IHS1986final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1986_2000Boundary = processing.runalg('qgis:intersection', IHS1986final_dissolved, mastercountylayer, hwypath+"Interstate1986_2000Boundary.shp")

Interstate1986_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1986_2000Boundary.shp","Interstate1986_2000Boundary", "ogr")
if not Interstate1986_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1986_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1986_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1986_2000Boundary.updateFields()
idx = Interstate1986_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1986_2000Boundary.pendingFields() )

for f in Interstate1986_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1986_2000Boundary.updateFeature( f )

Interstate1986_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1986_2000Boundary,statapath+"Interstate1986_2000Boundary.csv", "utf-8", None, "CSV")

#1987
#Add Dissolved Highway Files
IHS1987final_dissolved = iface.addVectorLayer(hwypath + "IHS1987final_dissolved.shp", "IHS1987final_dissolved", "ogr")
if not IHS1987final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1987_2000Boundary = processing.runalg('qgis:intersection', IHS1987final_dissolved, mastercountylayer, hwypath+"Interstate1987_2000Boundary.shp")

Interstate1987_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1987_2000Boundary.shp","Interstate1987_2000Boundary", "ogr")
if not Interstate1987_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1987_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1987_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1987_2000Boundary.updateFields()
idx = Interstate1987_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1987_2000Boundary.pendingFields() )

for f in Interstate1987_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1987_2000Boundary.updateFeature( f )

Interstate1987_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1987_2000Boundary,statapath+"Interstate1987_2000Boundary.csv", "utf-8", None, "CSV")

#1989
#Add Dissolved Highway Files
IHS1989final_dissolved = iface.addVectorLayer(hwypath + "IHS1989final_dissolved.shp", "IHS1989final_dissolved", "ogr")
if not IHS1989final_dissolved:
    print "Layer failed to load!"

#Intersect Hwy Layer and County Boundary Layer
Interstate1989_2000Boundary = processing.runalg('qgis:intersection', IHS1989final_dissolved, mastercountylayer, hwypath+"Interstate1989_2000Boundary.shp")

Interstate1989_2000Boundary=iface.addVectorLayer(hwypath+"Interstate1989_2000Boundary.shp","Interstate1989_2000Boundary", "ogr")
if not Interstate1989_2000Boundary:
    print "Layer failed to load!"

#Calculate Distance of Each Segment
Interstate1989_2000Boundary.startEditing()

#step 1
seglength = QgsField( 'seglength', QVariant.Double )
Interstate1989_2000Boundary.dataProvider().addAttributes([seglength])
Interstate1989_2000Boundary.updateFields()
idx = Interstate1989_2000Boundary.fieldNameIndex( 'seglength' )

#step 2
e = QgsExpression( '$length' )
e.prepare( Interstate1989_2000Boundary.pendingFields() )

for f in Interstate1989_2000Boundary.getFeatures():
    f[idx] = e.evaluate( f )
    Interstate1989_2000Boundary.updateFeature( f )

Interstate1989_2000Boundary.commitChanges()

QgsVectorFileWriter.writeAsVectorFormat(Interstate1989_2000Boundary,statapath+"Interstate1989_2000Boundary.csv", "utf-8", None, "CSV")







