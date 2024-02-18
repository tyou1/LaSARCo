STK.V.9.0
WrittenBy    StandardObjectCatalog
BEGIN Facility
Name        Wettzell
	BEGIN CentroidPosition
		DisplayCoords         Geodetic
		EcfLatitude           49.145
		EcfLongitude          12.8772
		EcfAltitude           657
		DisplayAltRef         Ellipsoid
		AzElMask              AzElMaskFile: Wettzell.aem
	END CentroidPosition
BEGIN Extensions
	BEGIN Graphics
		BEGIN Graphics
			ShowAzElAtRangeMask       On
			MinDisplayRange           0.0
			MaxDisplayRange           1000000.0
			NumAzElAtRangeMaskSteps   10
		END Graphics
	END Graphics
	BEGIN AccessConstraints
			LineOfSight     IncludeIntervals
			AzElMask        IncludeIntervals
	END AccessConstraints
	BEGIN Desc
		ShortText    8
Wettzell
		LongText    254
Name:           Wettzell
Country:        Germany
Location:       Wettzell
Status:         Active
Type:           GroundStation
Notes:          

Sources:                       http://ilrs.gsfc.nasa.gov/stations/index.html
Last updated:   2009-10-13
	END Desc
END Extensions
END Facility
