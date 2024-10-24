import geopandas as gpd
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape

def vectorize_raster(raster_path, output_shapefile):
    # Abrir el archivo raster
    with rasterio.open(raster_path) as src:
        image = src.read(1)  # Leer la primera banda
        mask = image != src.nodata  # Crear una máscara para los valores no nulos

        # Generar las geometrías y atributos
        results = (
            {'properties': {'raster_val': v}, 'geometry': s}
            for i, (s, v) in enumerate(
                shapes(image, mask=mask, transform=src.transform))
        )

        # Convertir a GeoDataFrame
        geoms = list(results)
        gdf = gpd.GeoDataFrame.from_features(geoms)

        # Guardar como shapefile
        gdf.to_file(output_shapefile, driver='ESRI Shapefile')

# Uso de la función
raster_path = './img/monitoreo_meteorologico_tmax_1.tif'
output_shapefile = './shp/monitoreo_meteorologico_tmax_1.shp'
vectorize_raster(raster_path, output_shapefile)