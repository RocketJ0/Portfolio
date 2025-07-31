# Academic Calendar OCR Pipeline
An end-to-end computer vision and OCR system that extracts course codes, names, and period data from academic timetable images. Planned to be used in a larger project, Syllabuss, to help students plan their courses.

[Link to code](5.Syllabuss/main.ipynb)

[Link to output](5.Syllabuss/Output)

The output has some course names containing partial data. This is intended to be fixed using an API to obtain data from the university website.


## Tools used
- Pandas and Numpy for data handling, with some help from regex
- OpenCV for preprocessing (thresholding, denoising, inpainting, contour detection, etc)
- Pytesseract for OCR
- DBSCAN from scikit-learn for unsupervised spatial grouping

## Key steps
1. Preprocessing - binarisation, object removal, text cleanup
2. Image segmentation
3. OCR and data processing
4. Filters to periods
5. Exports to a CSV file

## What did I learn?
- Preprocessing data for OCR: Pytesseract is prone to many problems in text detection, so processing the image before reading the image was a very crucial step.
- Solidified my understanding of regex
- Importance of modular design: Each function solved a sub problem. This helped me to check each small part in isolation, so that I was able to piece together the entire project seamlessly at the end.
