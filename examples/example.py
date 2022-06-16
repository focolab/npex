import os
from npex.npex import NPExtractor

### first pass: peakfinding, curation, alignment and extraction
params = dict(
    f='/home/gbubnis/prj/FOCO_FCD_v0.2/rainbow/col03-6-crop.tif',
    pixel_size={"X":0.2, "Y":0.2, "Z":1},
    rgbw_channels=[0,1,2,3],
    data_tag='FCD-col03-6-crop',
    output_folder='anl-example'
)
npe = NPExtractor(**params)
npe.find_peaks()
npe.launch_gui()
npe.align_to_ref()
npe.extract_rgbw(view_napari=True)
npe.export()


# #### RELOAD an existing extractor, continue curation
# npe2 = NPExtractor.load('anl-example_npextractor/npextractor.json')
# npe2.launch_gui()
