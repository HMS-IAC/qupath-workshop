Cell detection and measurements
===============================

.. raw:: html

   <iframe src="_static/2024_09_16/04_cell_detection_and_measurements.pdf" width="100%" height="600px"></iframe>


**Practice**
------------

3. QuPath cell detection

   a. Threshold-based cell detection

      1. Within the ROI created in 2, detect nuclei in the DAPI channel using QuPath’s built-in cell detection method

         - Use default parameters: how many nuclei are detected?
         - Change sigma used for the Gaussian method: how does the number of detected nuclei change?
         - Change the intensity threshold: how does the number of detected nuclei change?
         - Change the cell expansion (in microns): do you notice a difference in cell size?


      Tip 1: Re-running cell detection will overwrite existing detections.  

      Tip 2: Start with default, make small changes then larger changes until obtaining a satisfying segmentation.

   b. Machine learning-based cell detection

      1. Within the ROI created in 2, detect nuclei in the DAPI channel using StarDist’s extension in QuPath

         - Use default parameters: how many nuclei are detected?
         - Change detection probability: how many nuclei are detected?
         - Compare segmentation results between threshold-based and ML-based cell detection (one way to do this is to run threshold-based nuclei detection in another ROI).
