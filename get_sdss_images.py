'''
Query SDSS Galaxy Zoo 2 database, getting corresponding info from Galaxy table, using that information
to pass into SDSS.get_images
'''

from astroquery.sdss import SDSS
from astropy.io import fits
from astropy.visualization import make_lupton_rgb
from PIL import Image
import json

'''
GETTING LABELED GALAXIES PRODUCED BY get_labels.py
'''
f = open("galaxy_class_labels.json")
labeled_galaxies = json.load(f)

# '''
# QUERYING DATABASE
# '''
# ex = SDSS.query_sql("select top 10 specobjid, dr8objid, rastring, decstring from zoo2MainSpecz")
# # print(len(ex))
# # ex.write("top_10.data", format="ascii")

'''
QUERYING DATABASE
'''
for galaxy_id in labeled_galaxies.keys():
    gr = SDSS.query_sql(f"select objid, run, rerun, camcol, field from Galaxy where objid={galaxy_id}") # gr = galaxy_result; result from Galaxy table
    if gr:
        id = gr["objid"][0]
        run = gr["run"][0]
        rerun = gr["rerun"][0]
        camcol = gr["camcol"][0]
        field = gr["field"][0]
        fits_imgs = SDSS.get_images(run=run,rerun=rerun,camcol=camcol,field=field,band=['r','g','i'],timeout=120)
        # print(len(fits_imgs))

        r_img_write = fits_imgs[0]
        r_img_write.writeto(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/fits/{id}-r.fits", overwrite=True)

        g_img_write = fits_imgs[1]
        g_img_write.writeto(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/fits/{id}-g.fits", overwrite=True)

        i_img_write = fits_imgs[2]
        i_img_write.writeto(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/fits/{id}-i.fits", overwrite=True)

        r_img = fits.open(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/fits/{id}-r.fits")[0].data
        g_img = fits.open(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/fits/{id}-g.fits")[0].data
        i_img = fits.open(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/fits/{id}-i.fits")[0].data

        # ALIGN BANDS

        rgb_img = make_lupton_rgb(i_img, r_img, g_img, Q=10, stretch=0.5) # ordering taken from: https://docs.astropy.org/en/stable/visualization/rgb.html#astropy-visualization-rgb

        wimage = Image.fromarray(rgb_img)
        wimage.save(f"D:/Michael Cleversley/Pictures/Galaxy Detection & Identification/jpg/{id}.jpg",'jpeg',quality=97) # 97% best background 350k

        break # only download 1 image for now

# https://github.com/astroCV/astroCV/blob/master/galaxy_detection/training/jpg_filters.ipynb

