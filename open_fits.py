from astropy.io import fits

def read_file(fits_fname):
    with fits.open(fits_fname) as hdul:
        print(hdul.info())
        hdr = hdul[0].data
        return hdr
