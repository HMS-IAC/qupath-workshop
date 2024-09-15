Cell classification
===================

.. raw:: html

   <iframe src="_static/05_cell_classification.pdf" width="100%" height="600px"></iframe>


**Practice**
------------

4. QuPath cell classification

   a. Single-measurement classifier

      1. Create a class for Ki67 positive cells: Ki67+
      2. Create a single measurement classifier on Nucleus: CY5 mean
      3. Start with a threshold of 1000

         - How many cells are classified as Ki67+?

      4. Fine-tune parameters to improve your classification

         - How many cells are classified as Ki67+?

      5. Do the same for the FITC channel (Keratin).

   b. Composite classifiers

      1. Combine the two single-measurement classifiers into a composite classifier.
      2. Populate classes from objects
      
         - Which classes do you now observe?
         - How did the number of Ki67+ cells change?
