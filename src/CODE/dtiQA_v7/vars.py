# dtiQA v7.1.3: Shared Variables
# Leon Cai and Qi Yang
# MASI Lab
# July 1, 2020

# Set Up

import os

# Define class to hold shared variables

class SharedVars():

    def __init__(self):

        # Define necessary directories (CHANGE IF IN SINGULARITY)

        supplemental_dir = '/SUPPLEMENTAL'
        app_dir = '/APPS'
        
        # Define FA atlas variables

        self.STANDARD_FA_FILE = os.path.join(supplemental_dir, 'JHU-ICBM-FA-1mm.nii.gz')
        self.ATLAS_FILE = os.path.join(supplemental_dir, 'JHU-ICBM-labels-1mm.nii.gz')
        self.ROI_NAMES_FILE = os.path.join(supplemental_dir, 'JHU_label.txt')

        # Define Synb0-DisCo variables

        self.SYNB0_EXEC_FILE = os.path.join(app_dir, 'synb0', 'synb0.sh')

        # Define threading variable

        self.NUM_THREADS = 1 # Note: This value must be >= 1. Use 1 for spider on ACCRE. In MRTrix3, nthreads = 0 disables multithreading, so we use NUM_THREADS-1 for MRTrix3 commands

        # Define MD variables

        self.ADC_WATER = 0.0030377 # mm^2/s at 37C

        # Define visualization variables

        self.PAGESIZE = (10.5, 8)
        self.TITLE_FONTSIZE = 16
        self.LABEL_FONTSIZE = 12
        self.PDF_DPI = 600
        self.VIS_PERCENTILE_MAX = 99.9

# Define instance of SharedVars class that will be accessible to (and editable by) other modules

SHARED_VARS = SharedVars()