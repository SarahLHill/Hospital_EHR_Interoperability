## ***EHR_Interoperability_Analysis***

---

### <ins>Project Overview</ins>

This study investigates potential correlations between U.S. hospital overall ratings, as published by the Centers for Medicare & Medicaid Services (CMS), and the implementation of Certified Electronic Health Record (EHR) Systems.
By merging hospital demographic and rating data with ONC-certified EHR developer information, the project seeks to identify patterns in technology adoption and assess potential links between EHR systems and hospital performance.

The goal of this project is to provide actionable insights into how certified EHR technologies may influence or reflect hospital quality, ownership models, and care delivery standards while supporting broader efforts in healthcare interoperability and digital transformation.

___

#### Setup Instructions:

#### 1. Open a Terminal or Command Prompt

On Windows: Press the Windows key, type cmd, and press Enter to open the Command Prompt.
On Mac: Open the Terminal app (found in Applications > Utilities).
On Linux: Open your Terminal from the Applications menu.

#### 2. Clone the Project Repository
This downloads the repository onto your local computer.

Type the following commands into terminal:

      git clone https://github.com/SarahLHill/Hospital_EHR_Interoperability
      cd EHR_Interoperability_Analysis

#### 3. Create a Virtual Environment

This will keep the project’s packages separate from other programs. 

##### In the terminal window, enter:

On Windows:

    python -m venv venv
    venv\Scripts\activate
      
On Mac/Linux:

    python3 -m venv venv
    source venv/bin/activate

#### 4. Install Required Packages

##### Enter commands into terminal:

      pip install -r requirements.txt

#### 5. Launch the Project in Jupyter Notebook

##### In the same terminal or command prompt, enter the following command:

       jupyter notebook

##### You should see your project shortly after.

___

#### <ins>Technologies Used</ins>

- ##### Jupyter Notebook
   Tool for documenting and organizing project.
- ##### Python
   Used to create programming functions to analyze data.
- ##### Pandas
   Used to extract, transform and load data.
- ##### SQLite
   Used to store cleaned data and join datasets efficiently
- ##### Typing
   Helped label what kind of input each function expects, which makes the code easier to understand
- ##### NumPy
   Used for mathmatical operations.
- ##### Matplotlib 
- ##### Seaborn
   Used for plotting and visualizations.
- ##### OS
   Tool for managing access to specific file paths.
- ##### Sys
   Tool for accessing functions in separate file path.

___

### Dataset 1: Hospital General Information

***(hospital_general_info.csv)***

#### Data Dictionary - Hospital General Information

| **Column Name**                         | **Description**                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| `facility_id`                       | CMS Certification Number (CCN) uniquely identifying the hospital or facility.              |
| `facility_name`                     | Official name of the hospital or healthcare facility.                                      |
| `city_town`                         | City or town where the hospital is located.                                                |
| `state`                             | Two-letter state abbreviation where the hospital is located.                               |
| `zip_code`                          | 5-digit ZIP code of the hospital’s address.                                                |
| `hospital_type`                     | Category of hospital (e.g., Acute Care, Critical Access, Psychiatric).                     |
| `hospital_ownership`                | Entity that owns the hospital (e.g., Government - Federal, Proprietary, Voluntary Non-Profit). | 
| `hospital_overall_rating`          | Overall hospital quality star rating (1 to 5 stars) as assessed by CMS.                    |


#### Data Summary - Hospital General Information

- **Data Types**: Mix of categorical (hospital type, ownership, state) and numerical (ratings)
- **Missing Data**: Several columns contain a high volume of missing values. However, many of these are labeled as "Not Available" and have been consistently standardized during cleaning. Others are considered non-essential for analysis and have been removed to streamline the dataset.
- **Total Rows:** 5384
- **Total Columns:** 8

#### Data Source - Hospital General Information

Hospital General Information - Centers for Medicare & Medicaid Services (CMS) :

[https://data.cms.gov/provider-data/dataset/xubh-q36u](https://data.cms.gov/provider-data/dataset/xubh-q36u)

### Dataset 2: Certified EHR Technology (CEHRT)

***(cehrt.csv)***

#### Data Dictionary - Certified EHR Technology

|  **Column Name**            |  **Description**                                                                                  |
|-----------------------------|-----------------------------------------------------------------------------------------------|
| `facility_id`               | Unique CMS Certification Number (CCN) identifying the hospital or facility. |
| `cehrt_id`                  | Unique identifier for the certified EHR technology (CEHRT) |
| `developer_name`            | Entity or organization that created or designed the software or technology of Certified EHR.|
| `product_name`               | Software or system that met ONC standards for Certified EHR.|


- **Data Types**: Mix of categorical and numerical (facility ID, CEHRT ID, developer name)
- **Missing Data**: Missing values for `cehrt_id` and `developer_name` are present, but these are not essential for overall analysis and have been handled appropriately.
- **Total Rows:** 4593
- **Total Columns:** 4

### Data Source - Certified EHR Technology

- [HealthIT.gov - Certified Health Information Technology](https://www.healthit.gov/data/datasets/certified-health-information-technology-reported-hospitals-promoting-interoperability)

---

### Summary of Analysis:

<ins>Developer Performance Trends:</ins> Certain EHR developers are consistently associated with hospitals that have higher overall ratings. This suggests potential alignment between developer offerings and hospital quality metrics.

<ins>Hospital Count Distribution:</ins> A few developers dominate the landscape, with a large number of hospitals using their systems. Smaller vendors show more variability in associated ratings, possibly due to niche implementations or regional focus.

<ins>Rating Clusters:</ins> Hospitals using top-performing developers tend to cluster around ratings of 4 and 5, while others show a wider spread, including more 1s and 2s. This may reflect differences in usability, support, or integration capabilities.

<ins>Data Completeness:</ins> The majority of hospitals in the general info dataset had matching CEHRT entries, enabling a robust join. However, a small subset lacked developer data, which could indicate reporting gaps or non-certified systems.

---

### Limitations: 

While the merged dataset provides valuable insights into the relationship between EHR developers and hospital ratings, several    limitations must be acknowledged. First, the analysis is correlational and does not establish causation. Higher ratings may be influenced by factors unrelated to the EHR system, such as staffing, funding, or regional policies.
Second, missing or inconsistent data in either source can skew results, especially if certain hospitals or developers are underrepresented. 
Third, the hospital_overall_rating metric itself is a composite score that may not fully capture nuances in care quality or interoperability.
Lastly, developer names may vary slightly across records, requiring careful normalization to avoid misclassification.

---
