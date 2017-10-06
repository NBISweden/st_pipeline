""" 
This module contains some functions and utilities for ST SAM/BAM files
"""

import pysam
        
def convert_to_AlignedSegment(header, sequence, quality, 
                              barcode_sequence, umi_sequence):
    """
    This function converts the input variables 
    (header,sequence,quality,barcode_sequence,umi_sequence)
    to a pysam.AlignedSegment with the umi and barcode 
    informations as the following tags:
        Tag  Value
        "B0" barcode_sequence
        "B3" umi_sequence
    :param header: string with the header information
    :param sequence: string with the DNA/RNA sequence
    :param quality: string with the base calling quality values
    :param barcode_sequence: string with the barcode sequence
    :param umi_sequence: string with the unique molecular identifier sequence
    """

    # create
    aligned_segment = pysam.AlignedSegment()

    # Set the standard values
    aligned_segment.query_name = header
    aligned_segment.query_sequence = sequence
    aligned_segment.query_qualities = quality

    # Set the tags
    aligned_segment.set_tag('B0',barcode_sequence)
    aligned_segment.set_tag('B3',umi_sequence)

    return aligned_segment