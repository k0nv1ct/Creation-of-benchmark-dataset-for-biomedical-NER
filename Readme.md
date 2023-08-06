# Prescription NER and Drug Dosage Extraction Project

This project aims to extract Named Entity Recognition (NER) entities, drugs, and dosage plans from various medical documents such as doctor prescriptions, medical reports, medical advice, diagnoses, and discharge reports. The Google Cloud Healthcare API was utilized to achieve this goal, enabling the extraction of valuable information from medical texts.

## Project Overview

The project involves the following main steps:

1. Utilizing the Google Cloud Healthcare API to perform Named Entity Recognition (NER) on medical documents.
2. Processing the API's JSON responses to extract NER entities, linked entities with UMLS codes, and the relationships between the tagged entities.
3. Structuring the extracted data into three CSV files: one for NER entities, one for linked entities with UMLS codes, and one for relationships between tagged entities.
4. Using a Jupyter Notebook to document and showcase the entire process, from API usage to data structuring.

## Google Cloud Healthcare API

The [Google Cloud Healthcare API](https://cloud.google.com/healthcare-api) was a crucial tool in this project. It facilitated the extraction of NER entities, linked entities with UMLS codes, and entity relationships from medical documents. The API's responses were in JSON format, containing valuable information about the recognized entities and their characteristics.

## Data Processing and Structuring

After receiving the JSON responses from the Google Cloud Healthcare API, the following data processing steps were undertaken:

1. Extracting NER entities: Parsing the JSON to retrieve NER entities identified in the medical documents.
2. Extracting linked entities with UMLS codes: Collecting information about entities that are linked to UMLS codes, enriching the extracted data.
3. Extracting entity relationships: Capturing the relationships between different tagged entities within the text.
4. Structuring data into CSV files: The processed data was organized into three CSV files - one for NER entities, one for linked entities with UMLS codes, and one for entity relationships. These CSV files enable easy access and analysis of the extracted information.

## Dataset

For this project, a biomedical dataset was used. The choice of the dataset can vary based on the specific requirements and availability of suitable data. The project's implementation is designed to work with a wide range of biomedical datasets, allowing for flexibility in its application.

## Jupyter Notebook

The entire process, from utilizing the Google Cloud Healthcare API to data structuring, is well-documented in a Jupyter Notebook. This notebook provides a step-by-step walkthrough of the code implementation, data manipulation, and result visualization. It serves as a comprehensive guide for anyone interested in understanding and replicating the project.

## Conclusion

This project demonstrates how to leverage the Google Cloud Healthcare API to extract valuable information from medical documents, specifically focusing on NER entities, drugs, and dosage plans. The use of the API, along with the data processing and structuring techniques, showcases an efficient approach to handling medical text data for further analysis and research. The provided Jupyter Notebook ensures transparency and reproducibility, making it a valuable resource for those interested in similar endeavors.
