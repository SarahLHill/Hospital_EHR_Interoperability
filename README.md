# Hospital_EHR_Interoperability

---

**Objective**: This project will explore how characteristics of U.S. healthcare facilities influence electronic health record (EHR) adoption and regulatory compliance. By analyzing the 2023 datasets from the Centers for Medicare & Medicaid Services (CMS) and the Office of the National Coordinator for Health IT, it will highlight trends in EHR interoperability and its impact on healthcare quality.

## Project Overview

This project investigates how hospital characteristics and geographic factors influence the adoption of electronic health record (EHR) systems and compliance with federal interoperability standards. Using publicly available datasets from CMS and ONC, the analysis integrates three key sources:

- Hospital General Information: Includes facility demographics, ownership type, and CMS quality measures and ratings.

- Promoting Interoperability: Details hospitals’ engagement in the Medicare program aimed at advancing EHR-based data exchange.

- Certified EHR Technology: Listing of all certified health information technology developers that have been successfully tested and certified by the ONC Health IT Certification program.
- 
## Dataset 1: Hospital General Information

***(hospital_general_info.csv)***

### Data Dictionary - Hospital General Information

| **Column Name**                         | **Description**                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| `facility_id`                       | CMS Certification Number (CCN) uniquely identifying the hospital or facility.              |
| `facility_name`                     | Official name of the hospital or healthcare facility.                                      |
| `state`                             | Two-letter state abbreviation where the hospital is located.                               |
| `zip_code`                          | 5-digit ZIP code of the hospital’s address.                                                |
| `hospital_type`                     | Category of hospital (e.g., Acute Care, Critical Access, Psychiatric).                     |
| `hospital_ownership`                | Entity that owns the hospital (e.g., Government - Federal, Proprietary, Voluntary Non-Profit). |  
| `hospital_overall_rating`          | Overall hospital quality star rating (1 to 5 stars) as assessed by CMS.                    |


#### Data Summary - Hospital General Information

- **Data Types**: Mix of categorical (hospital type, ownership, state) and numerical (ratings, performance counts, dates)
- **Missing Data**: Several columns contain a high volume of missing values. However, many of these are labeled as "Not Available" and have been consistently standardized during cleaning. Others are considered non-essential for analysis and have been removed to streamline the dataset.
- **Total Rows:** 5384
- **Total Columns:** 7

#### Data Source - Hospital General Information

Hospital General Information - Centers for Medicare & Medicaid Services (CMS) :

[https://data.cms.gov/provider-data/dataset/xubh-q36u](https://data.cms.gov/provider-data/dataset/xubh-q36u)

## Dataset 2: Promoting Interoperability - Hospital

***(hospital_interoperability_data.csv)***

### Data Dictionary - Promoting Interoperability

|**Column Name**                                                   | **Description**                                                                                        |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `facility_id`                                                 | Unique CMS Certification Number (CCN) identifying the hospital or facility.                           |
| `facility_name`                                               | Official name of the hospital or healthcare facility.                                               |
| `meets_criteria_for_promoting_interoperability_of_ehrs`       | Indicates whether the facility meets CMS-defined criteria for promoting EHR interoperability.  |


#### Data Summary - Promoting Interoperability

- **Data Types**: Mix of categorical (hospital name, geographics) and numerical (dates)
- **Missing Data**: No missing values
- **Total Rows:** 4593
- **Total Columns:** 

#### Data Source - Promoting Interoperability

Promoting Interoperability - Hospital - Centers for Medicare & Medicaid Services (CMS) :

[https://data.cms.gov/provider-data/dataset/f4ga-b9gx](https://data.cms.gov/provider-data/dataset/f4ga-b9gx)

## Dataset 3: Certified EHR Technology (CEHRT)

***(cehrt.csv)***

### Data Dictionary - Certified Health IT Product List (CEHRT)

| **Column Name**                     | **Description**                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| `facility_id`                       | Unique CMS Certification Number (CCN) identifying the hospital or facility.                        |
| `cehrt_id`                          | Unique identifier for the certified EHR technology (CEHRT)                                        |
| `developer_name`                    | Name of product developer                                                                         |

#### Data Summary - Certified EHR Technology (CEHRT)

- **Data Types**: Mix of categorical and numerical (facility ID, CEHRT ID, developer name)
- **Missing Data**: Missing values for `cehrt_id` and `developer_name` are present, but these are not essential for overall analysis and have been handled appropriately.
- **Total Rows:** 4593
- **Total Columns:** 3

#### Data Source - Certified EHR Technology (CEHRT)

- [https://chpl.healthit.gov/#/resources/download](https://chpl.healthit.gov/#/resources/download)
