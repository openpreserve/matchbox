Matchbox Installation & Use
===========================
*The duplicate image detection tool*

Installation Guide
------------------

### Requirements

To install you need:

* Latest version of OpenCV
* Python 2.7
* Git

### Download

| Version | Size   | SHA1                                                    |                      |
|---------|--------|---------------------------------------------------------|----------------------|
| v1.0    | 23.6 MB| <small>1b34d11f66fe4b847f271a5aaaabb02c7917690c</small> |[download](https://github.com/openplanets/matchbox/archive/master.zip)            |

### Installing Matchbox

Please refere to the INSTALL file in the source directory [1].

Using Matchbox
--------------

### Matchbox Tools

* extractfeatures

This tool extracts features from images. The set of features implemented  contains  the basic image metadata extraction, the basic image processing features Color Histograms and Image Profiles, as well as more complex features based on interest point detection.
	
Features can be either extracted all at once or by distinctively specifiyng the required feature. Extracted features are either stored to the same directory of the corresponding image, or to a specified directory.  Features  can  be  stored in gzipped xml format or in binary  format. Binary storage  enables  faster processing while xml provides more flexibility for data processing with third party tools.
	
The stored feature filenames have the format:
	
<original_image_filename>.<featurename>.<dat|xml.gz>
e.g. img00001.tif.ImageHistogram.xml.gz
	
* compare

The compare tool compares two extracted features and  calculates a similarity estimation.
	
Input files have to be of the same feature set. Comparison between different feature sets is not possible. Also only two files can be compared with each other, not a set of files.
	
The resulting similarity estimation is written in xml format to standard output (e.g. the command line interface).
	
* train

The train tool is a specialized tool to create visual vocabularies based on visual bag-of-words. A visual bag-of-words is a pendant to the bag-of-words in classical information retrieval, where each text document is represented as a histogram of its distinctive word occurnces. This approach  has  been  adopted  in image processing based on features from interest point detectors - especially SIFT features.
	
The train tool takes a list of SIFT descriptors and applies a clustering algorithm onto it. The calculated centroids represent the visual vocabulary that will be used in further processing of certain workflows.
	

### Basic Workflows

#### Duplicate Detection

Duplicate detection is the task of detecting duplicates within an image collection.
	
1. extract SIFTComaparison features of all images
2. train a visual vocabulary on the extracted features
3. extract BoWHistograms using the vocabulary and all extracted SIFTCompairison features
4. create a similarity matrix for the collection using compare on all BoWHistogram features
5. take the top-most similar images for each image and compare their SIFTComparison features.
6. Set a threshold based on the retrieved data.
7. images with an SSIM exceeding the threshold are considered to be duplicates.

Command line use
----------------

### Sample usage

	python2.7 ./FindDuplicates.py /home/matchbox/matchbox-data/ all

### Output of duplicates detection script is a list of possible duplicates (e.g. document 10 is a duplicate candidat for page 2)

	[1 of 20] 1
	[2 of 20] 2 => [10]
	[3 of 20] 3

### SSIM comparison sample

	extractfeatures.exe <bild1>
	extractfeatures.exe <bild2>
	compare <bild1>.feat.xml <bild2>.feat.xml

### Output of SSIM comparison with value between 0 and 1, where 1 means high similarity

	<SIFTCompairison>
	   <SSIM>0.889990</SSIM>
	   ...
	</SIFTCompairision>

## Features and roadmap

### Version 1.0

* Duplicate detection in a digital document collection
* SSIM image comparison
