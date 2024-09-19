Tissue annotation and spatial measurements
==========================================

.. raw:: html

   <iframe src="_static/2024_09_16/06_tissue_annotation_and_spatial.pdf" width="100%" height="600px"></iframe>


**Practice**
------------

5. Automating tissue annotation

   a. Pixel-based classification

      1. Create a pixel classifier on the TRITC channel and apply it with default parameters.

         - What is the area of the annotated region?

      2. Adapt the parameters of the pixel classifier to yield coherent regions.

         - How does the area of the annotated region change with smoothing sigma?
         - How does the area of the annotated region change with intensity threshold?

   b. Machine learning pixel classifier

      1. Based on what you have learned by creating a machine learning classifier for cell objects, create training annotations for whole regions (akin to tissues) using the paint brush.

      2. Train a pixel classifier on these training data to identify regions of high signal intensity in the TRITC channel.
