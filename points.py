from PyQt5.QtGui import QColor

def CenterPoint(x_coord, y_coord):
    point = QgisPointXY(x_coord, y_coord)
    iface.mapCanvas().setCenter(point)

def add_original_points(generalID):
    
    Point1 = [-68.57616, -31.54081]
    Point2 = [-68.57780, -31.54158]
    Point3 = [-68.57861, -31.54041]
    points = [Point1, Point2, Point3]

    layer = iface.activeLayer()
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(255,0,0))

    layer.startEditing()
    for p in points:
        point = QgsPointXY(p[0],p[1])
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(point))
        feature.setAttributes([generalID])
       
        generalID+=1
        layer.dataProvider().addFeatures([feature])

    layer.commitChanges()

def obtained_points(generalID):
    Point1 = [-68.57618, -31.54081]
    Point2 = [-68.57627, -31.54102]
    Point3 = [-68.57858, -31.54040]
    points = [Point1, Point2, Point3]
    
    layer = iface.activeLayer()
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(0,255,0))

    layer.startEditing()
    for p in points:
        point = QgsPointXY(p[0],p[1])
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(point))
        feature.setAttributes([generalID])
        
        generalID+=1
        layer.dataProvider().addFeatures([feature])

    layer.commitChanges()

def delete_all_points():
    layer.startEditing()
    for f in layer.getFeatures():
        layer.dataProvider().deleteFeatures([f.id()])

    layer.commitChanges()
