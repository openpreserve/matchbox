#!/usr/bin/env python

'''
# ======================================================== #
# Module  : FindDuplicates                                 #
#                                                          #
# @author : Alexander Schindler                            #
# @contact: Alexander.Schindler@ait.ac.at                  #
#                                                          #
# @version: 1.0.0                                          # 
#                                                          #
# -------------------------------------------------------- #
#                                                          #
# @summary:                                                # 
#                                                          #
# -------------------------------------------------------- #
#                                                          #
# @license:                                                #
#                                                          #
# ======================================================== #
'''

# === imports ===================================

import argparse
import MatchboxLib

# === definitions ===============================

configuration = "Linux"

configs = {}

# Linux is the standard configuration
# all binaries should be installed on the target machine through "make install"
configs["Linux"] = {}
configs["Linux"]["BIN_EXTRACTFEATURES"] = "mb_extractfeatures"
configs["Linux"]["BIN_COMPARE"]         = "mb_compare"
configs["Linux"]["BIN_TRAIN"]           = "mb_train"

# === Classes ===================================


if __name__ == '__main__':

    # ===============================================================================
    # Command line argument parsing
    # ===============================================================================
    parser = argparse.ArgumentParser()
    #
    # mandatory arguments
    #
    parser.add_argument('dir',          help='directory containing image files')
    parser.add_argument('action',       help='define which step of the workflow shouold be executed', 
                        choices=['all', 'extract', 'compare', 'train', 'bowhist', 'clean'])
    #
    # optional arguments
    #
    parser.add_argument('--threads',    help='number of concurrent threads',                                type=int, default=1)
    parser.add_argument('--featdir',    help='Alternative directory for storing feature files',             type=str, default="")
    parser.add_argument('--precluster', help='Number of Preclustering centers (0 = no preclustering)',      type=int, default=100)
    parser.add_argument('--config',     help='Configuration Parameter',                                     type=str, default="Linux")
    parser.add_argument('--bowsize',    help='Size of Bag of Words',                                        type=int, default=1000)
    parser.add_argument('--sdk',        help='Number of Spatial Distincitve Keypoints',                     type=int, default=0)
    parser.add_argument('--clahe',      help='Value of adaptive contrast enhancement (1 = no enhancement)', type=int, default=1)
    parser.add_argument('--downsample', help='Downsample to a certain number of pixels',                    type=int, default=1000000)
    parser.add_argument('--update',     help='Update and overwrite existing feature files', action='store_true')
    parser.add_argument('--binary',     help='Store feature data in binary archives',       action='store_true')
    parser.add_argument('--binaryonly', help='Store feature data in binary archives',       action='store_true')
    #
    parser.add_argument('-v',           help="Print verbose messages", dest='verbose', action='store_true')

    # parse arguments
    args   = vars(parser.parse_args())

    # assign configuration
    config = configs[args['config']]

    if (args['binaryonly']):
        args['binary'] = True
        
    collection_directory = args['dir']
    feature_directory    = collection_directory
        
    if len(args['featdir']) > 0:
        feature_directory = args['featdir']

    # ===============================================================================
    # action: clean
    # ===============================================================================
    # 
    # clean all automatically generated files.
    #
    if (args['action'] == 'clean'):

        print "\n=== deleting generated files from directory {0} ===\n".format(feature_directory)
        
        MatchboxLib.clearDirectory(feature_directory, args['verbose'])
        
    # ===============================================================================
    # action: extract
    # ===============================================================================
    #
    # extract all relevant features for the duplicate detection task
    #
    if (args['action'] == 'extract') or (args['action'] == 'all'):
        
        print "\n=== extracting features from directory {0} ===\n".format(collection_directory)
        
        MatchboxLib.extractFeatures(config, 
                                    collection_directory, 
                                    args['sdk'], 
                                    args['threads'], 
                                    args['clahe'], 
                                    feature_directory, 
                                    "SIFTComparison", 
                                    args['downsample'], 
                                    args['verbose'], 
                                    args['binary'], 
                                    args['binaryonly'],
                                    args['update'])
    
    # ===============================================================================
    # action: train
    # ===============================================================================
    #
    # calculate the bag of words based on the extracted features
    #
    if (args['action'] == 'train') or (args['action'] == 'all'):
        
        print "\n=== calculating Visual Bag of Words ===\n"
        
        MatchboxLib.calculateBoW(config, 
                                 feature_directory, 
                                 ".SIFTComparison.feat.xml.gz", 
                                 args['precluster'], 
                                 args['bowsize'], 
                                 args['verbose'], 
                                 args['binary'])
    
    # ===============================================================================
    # action: bowhist
    # ===============================================================================
    #
    # extract bow histograms
    #
    if (args['action'] == 'bowhist') or (args['action'] == 'all'):
        
        print "\n=== extract BoW Histograms from directory {0} ===\n".format(collection_directory)
        
        MatchboxLib.extractBoWHistograms(config, 
                                         collection_directory, 
                                         args['threads'], 
                                         feature_directory, 
                                         args['binary'])

    # ===============================================================================
    # action: compare
    # ===============================================================================
    #
    # compare bow histograms and display duplicates
    #
    if (args['action'] == 'compare') or (args['action'] == 'all'):
        
        print "\n=== compare images from directory {0} ===\n".format(args['dir'])

        MatchboxLib.pyFindDuplicates_SpatialVerification_fast(config, 
                                                              feature_directory, 
                                                              args['threads'], 
                                                              args['binary'], 
                                                              args['verbose'])
